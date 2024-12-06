import os

# 记录跳过的帖子标题到日志文件
def log_skipped_post(title):
    skipped_log_file = os.path.join("data", "skipped_posts.log")
    with open(skipped_log_file, "a", encoding="utf-8") as log_file:
        log_file.write(title + "\n")


# 保存已下载的帖子标题，防止重复处理
def save_processed_post(title):
    processed_file = os.path.join("data", "processed.txt")
    with open(processed_file, "a", encoding="utf-8") as f:
        f.write(title + "\n")
