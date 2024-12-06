import os
import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from scraper.config import PARTITIONS, SAVE_FOLDER
from scraper.fetcher import fetch_html
from scraper.parser import parse_thread_links, parse_image_links, parse_title
from scraper.downloader import download_image
from scraper.logger import log_skipped_post, save_processed_post
from scraper.processor import load_processed_posts, sanitize_filename

def main():
    # 读取已下载的帖子标题
    processed_posts = load_processed_posts()

    # 用户选择分区
    print("请选择需要爬取的分区：")
    for i, partition in enumerate(PARTITIONS.keys(), 1):
        print(f"{i}. {partition}")
    partition_choice = int(input("输入对应数字选择分区：")) - 1
    selected_partition = list(PARTITIONS.keys())[partition_choice]
    partition_url_template = PARTITIONS[selected_partition]

    # 在 D:/1024p 下创建分区文件夹
    partition_folder = os.path.join(SAVE_FOLDER, selected_partition)
    if not os.path.exists(partition_folder):
        os.makedirs(partition_folder)

    # 用户输入爬取范围和线程数
    start_page = int(input("请输入开始页面（数字）："))
    end_page = int(input("请输入结束页面（数字）："))
    threads = int(input("请输入下载线程数（推荐 5-20）："))

    print(f"开始爬取分区：{selected_partition}，范围：第 {start_page} 页到第 {end_page} 页，线程数：{threads}")

    total_images = 0
    skipped_posts = 0
    downloaded_images = 0

    with requests.Session() as session:
        all_thread_links = []
        for page in range(start_page, end_page + 1):
            print(f"正在获取第 {page} 页...")
            page_url = partition_url_template.format(page)
            page_html = fetch_html(page_url, session)
            if not page_html:
                print(f"无法获取页面 {page}. 跳过该页。")
                continue

            thread_links = parse_thread_links(page_html)
            all_thread_links.extend(thread_links)
            print(f"第 {page} 页：共找到 {len(thread_links)} 个帖子。")

        print(f"总共找到 {len(all_thread_links)} 个帖子。")

        for thread_url in tqdm(all_thread_links, desc="正在下载帖子", unit="帖"):
            thread_html = fetch_html(thread_url, session)
            if not thread_html:
                print(f"无法获取帖子：{thread_url}")
                continue

            title = sanitize_filename(parse_title(thread_html))

            if title in processed_posts:
                print(f"帖子 {title} 已经下载过，跳过。")
                skipped_posts += 1
                log_skipped_post(title)
                continue

            thread_folder = os.path.join(partition_folder, title)
            if not os.path.exists(thread_folder):
                os.makedirs(thread_folder)

            img_links = parse_image_links(thread_html)
            print(f"帖子 {title} 中共找到 {len(img_links)} 张图片。")

            with ThreadPoolExecutor(max_workers=threads) as executor:
                successful_downloads = list(executor.map(lambda img_url: download_image(img_url, thread_folder, session), img_links))

            downloaded_images += successful_downloads.count(True)
            total_images += len(img_links)

            save_processed_post(title)

    print("\n下载统计信息：")
    print(f"总图片数量：{total_images}")
    print(f"成功下载的图片数量：{downloaded_images}")
    print(f"跳过的帖子数量：{skipped_posts}")
    print(f"所有图片已保存到：{partition_folder}")

if __name__ == "__main__":
    main()
