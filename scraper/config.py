# 配置文件 config.py

# 分区 URL 模板
PARTITIONS = {
    "盖达尔的旗帜": "https://cb.3696x.xyz/thread0806.php?fid=16&page={}",
    "新时代的我们": "https://cb.3696x.xyz/thread0806.php?fid=8&page={}",
    #"成人文学交流区": "https://cb.3696x.xyz/thread0806.php?fid=20&page={}",
}

# 跳过的帖子链接
SKIPPED_URLS = [
    "https://cb.3696x.xyz/notice.php?fid=-1#1",
    "https://cb.3696x.xyz/htm_data/2408/16/6444784.html",
    "https://cb.3696x.xyz/htm_data/2310/16/344501.html",
    "https://cb.3696x.xyz/htm_data/2206/16/4218114.html",
    "https://cb.3696x.xyz/htm_data/1106/16/524942.html",
    "https://cb.3696x.xyz/htm_data/2207/16/3892864.html",
    "https://cb.3696x.xyz/htm_data/1110/16/622028.html"
]

# 图片保存路径
SAVE_FOLDER = "D:/1024p"

# 请求头，模拟浏览器请求
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
