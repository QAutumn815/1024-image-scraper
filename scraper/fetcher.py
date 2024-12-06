import requests
from scraper.config import HEADERS

# 请求网页内容，处理异常情况
def fetch_html(url, session):
    try:
        response = session.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            print(f"无法获取页面 {url}: {response.status_code}")
            return None
    except Exception as e:
        print(f"获取页面 {url} 时出错: {e}")
        return None
