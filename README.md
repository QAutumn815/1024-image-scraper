### **`README.md`**

```markdown
# 1024 Image Scraper

**1024 Image Scraper** 是一个用于爬取 1024 论坛分区帖子中的图片的 Python 脚本。该脚本通过模拟浏览器请求，从指定的分区爬取帖子并下载其中的图片。支持分页抓取、跳过已下载的帖子、多线程加速下载，并且能够自动处理文件名中的非法字符。

## 功能简介

- **分区选择**：支持从不同的分区爬取图片，如 "盖达尔的旗帜"、"新时代的我们" 等。
- **分页控制**：用户可以指定要爬取的页面范围。
- **图片下载**：脚本能够从帖子中提取所有图片链接并下载到本地。
- **跳过已下载帖子**：避免重复下载已下载过的帖子。
- **多线程支持**：使用多线程加速图片下载，提高下载效率。


```
```markdown
## 项目目录结构

1024-image-scraper/
│
├── data/
│   ├── processed.txt              # 存储已下载的帖子标题
│   └── skipped_posts.log         # 存储跳过的帖子标题
│
├── scraper/
│   ├── __init__.py                # 包的初始化文件
│   ├── config.py                  # 配置文件，包含常量和设置
│   ├── fetcher.py                 # 获取网页内容相关函数
│   ├── parser.py                  # 解析网页内容相关函数
│   ├── downloader.py              # 下载图片相关函数
│   ├── logger.py                  # 日志记录相关函数
│   └── processor.py               # 处理帖子标题和避免重复下载的函数
│
├── main.py                        # 主程序入口
├── requirements.txt               # 依赖库列表
└── README.md                      # 项目说明
```

## 环境要求

- Python 3.x 版本
- 安装以下 Python 库：

```bash
pip install -r requirements.txt
```

依赖项：

- `requests`：用于发送 HTTP 请求。
- `beautifulsoup4`：用于解析 HTML 页面。
- `tqdm`：用于显示进度条。

## 安装与运行

1. **下载或克隆项目**：

   从 GitHub 克隆此项目：

   ```bash
   git clone https://github.com/QAutumn815/1024-image-scraper.git
   cd 1024-image-scraper
   ```

2. **安装依赖**：

   在项目目录下，通过 `pip` 安装项目依赖：

   ```bash
   pip install -r requirements.txt
   ```

3. **运行脚本**：

   运行 `main.py` 来启动程序：

   ```bash
   python main.py
   ```

   在脚本运行过程中，程序会提示你选择要爬取的分区、输入页面范围、设置线程数等参数。

## 使用教程

### 1. 启动程序

运行脚本后，程序会要求你选择需要爬取的分区。输入数字选择你想爬取的分区。例如：


>请选择需要爬取的分区：
>1. 盖达尔的旗帜
>2. 新时代的我们
>3. 成人文学交流区
>输入对应数字选择分区：1
><br><font color=Blue>2和3暂未实现</font>



### 2. 输入分页范围

选择好分区后，程序会要求你输入爬取的页面范围：

```
请输入开始页面（数字）：1
请输入结束页面（数字）：5
请输入下载线程数（推荐 5-20）：10
```

这里的 `开始页面` 和 `结束页面` 控制爬取的具体页面范围，`下载线程数` 用来设置并行下载的线程数，推荐设置为 5-20 个。

### 3. 图片下载与保存

程序会开始下载选定页面范围内所有帖子中的图片，并按照帖子标题创建文件夹，将图片保存在本地。图片默认保存路径为 `D:/1024p`，如果需要更改保存路径，可以在 `config.py` 文件中修改 `SAVE_FOLDER` 配置项。

### 4. 进度显示

程序会显示当前下载的进度，通过 `tqdm` 库的进度条实时展示：

```
正在下载帖子:  50%|███████████████████████████████ | 5/10 [00:10<00:10, 5.00s/帖]
```

### 5. 跳过已下载的帖子

如果某些帖子已经被下载过，程序会自动跳过这些帖子，并将跳过的帖子标题记录在 `skipped_posts.log` 文件中。例如：

```
帖子 "某帖标题" 已经下载过，跳过。
```

## 配置

### 配置分区和链接

在 `scraper/config.py` 中，你可以配置要爬取的论坛分区及其对应的 URL 模板。例如：

```python
PARTITIONS = {
    "盖达尔的旗帜": "https://和谐/thread0806.php?fid=16&page={}",
    "新时代的我们": "https://和谐/thread0806.php?fid=15&page={}",
    "成人文学交流区": "https://和谐/thread0806.php?fid=20&page={}",
}
```

### 配置跳过的帖子

在 `config.py` 文件中，你还可以配置需要跳过的帖子链接。例如：

```python
SKIPPED_URLS = [
    "https://和谐/notice.php?fid=-1#1",
    "https://和谐/htm_data/2408/16/6444784.html",
    "https://和谐/htm_data/2310/16/344501.html",
]
```

### 配置保存路径

默认情况下，图片保存在 `D:/1024p` 路径下。你可以在 `config.py` 文件中修改 `SAVE_FOLDER` 路径，以指定保存图片的位置。

```python
SAVE_FOLDER = "D:/1024p"
```

## 注意事项

- **请遵守目标网站的爬虫政策**，避免对服务器造成过大压力。
- **不要频繁请求**，建议使用合理的线程数（5-20 个线程），并避免过高的请求频率。
- **根据需求修改配置文件**，包括分区选择、保存路径等。
- **合法的网页内容提取**：如果有更新或者网页结构变化，可能需要调整解析逻辑。

## 许可

本项目遵循 [MIT 许可协议](https://opensource.org/licenses/MIT)