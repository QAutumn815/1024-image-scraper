from bs4 import BeautifulSoup
from scraper.config import SKIPPED_URLS

# 解析分区页面，获取所有帖子链接
def parse_thread_links(html):
    soup = BeautifulSoup(html, "html.parser")
    thread_links = []
    for link in soup.find_all("a", href=True):
        href = link.get("href")
        if href and "htm_data" in href:
            full_url = f"https://cb.3696x.xyz/{href}"
            if full_url not in SKIPPED_URLS:  # 如果链接不在跳过列表中
                thread_links.append(full_url)
    return thread_links


# 解析帖子页面，获取图片链接
def parse_image_links(html):
    soup = BeautifulSoup(html, "html.parser")
    img_links = []
    for img_tag in soup.find_all("img"):
        img_url = img_tag.get("ess-data")
        if img_url and (img_url.startswith("http") or img_url.startswith("//")):
            if img_url.startswith("//"):
                img_url = "http:" + img_url
            img_links.append(img_url)
    return img_links


# 解析帖子标题
def parse_title(html):
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.select("h4.f16")
    if title_tag:
        return title_tag[0].get_text().strip()
    return "Untitled"
