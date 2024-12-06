import os
import re

# 读取已下载的帖子标题，避免重复下载
def load_processed_posts():
    processed_file = os.path.join("data", "processed.txt")
    if os.path.exists(processed_file):
        with open(processed_file, "r", encoding="utf-8") as f:
            return set(f.read().splitlines())
    return set()


# 清理标题中的非法字符
def sanitize_filename(title):
    return re.sub(r'[\\/:*?"<>|]', "_", title)
