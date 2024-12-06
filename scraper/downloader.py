import os
import requests
from scraper.config import HEADERS

# 下载图片，采用流式下载以减少内存占用
def download_image(img_url, folder, session):
    try:
        response = session.get(img_url, headers=HEADERS, stream=True, timeout=10)
        if response.status_code == 200:
            file_name = os.path.join(folder, img_url.split("/")[-1])
            with open(file_name, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return True
        else:
            print(f"无法下载图片 {img_url}")
            return False
    except Exception as e:
        print(f"下载图片 {img_url} 时出错: {e}")
        return False
