import os
import re
import time
from DrissionPage import ChromiumPage
from bs4 import BeautifulSoup
import requests

# 创建 ChromiumPage 的当前标签页实例
google = ChromiumPage().latest_tab

# 开始监听页面加载（监听包含 category=hot&viewtype=basic 的请求）
google.listen.start("category=hot&viewtype=basic")

# 打开目标视频列表页
google.get("https://www.91porn.com/v.php?category=hot&viewtype=basic")
time.sleep(3)
google.ele('/html/body/div[2]/div[2]/div/div/ul/li[3]/a').click()

# 等待监听到的第一个匹配请求响应
sjb = google.listen.wait()

# 获取响应的 HTML 内容
html_content = sjb.response.body

# 用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, "html.parser")

# 用 set() 存储视频页面链接，自动去重
video_links = set()
for a in soup.find_all('a', href=True):
    href = a['href']
    # 筛选符合视频页格式的链接
    if href.startswith('https://www.91porn.com/view_video.php?viewkey='):
        video_links.add(href)  # set 自动去重

print(f"Found {len(video_links)} unique video pages to visit.")
print("-" * 20)


def save_video(video_url, video_title):
    """
    下载视频并保存到本地文件，如果文件已存在则跳过

    参数:
        video_url (str): 视频文件的下载链接
        video_title (str): 视频标题，用于生成保存的文件名
    """
    # 清理标题中的非法字符
    save_title = re.sub(r'[\\/:*?"<>|]', '', video_title).strip()

    # 创建保存目录
    os.makedirs("videos2", exist_ok=True)

    # 拼接保存路径
    filename = f"videos2/{save_title}.mp4"

    # 如果文件已存在，直接跳过
    if os.path.exists(filename):
        print(f"⏭ 已存在文件，跳过下载：{filename}")
        return

    print(f"开始下载：{filename}")

    try:
        # 下载视频文件
        with open(filename, "wb") as f:
            f.write(requests.get(video_url).content)
        print(f"✅ 下载完成：{filename}")
    except Exception as e:
        print(f"❌ 下载失败：{filename}，原因：{e}")


# 用于记录已下载的视频 URL，防止重复下载
downloaded_urls = set()

# 遍历所有视频页链接
for idx, link in enumerate(video_links, 1):
    google.get(link)
    try:
        # 找到视频播放的 <source> 标签
        source_ele = google.ele('xpath=//*[@id="player_one_html5_api"]/source')
        # 找到视频标题
        title_ele = google.ele('xpath=//*[@id="videodetails"]/h4')

        video_url = source_ele.attrs['src']
        video_title = title_ele.text

        # 如果地址为空或已下载过，跳过
        if not video_url or video_url in downloaded_urls:
            print(f"{idx}. ⏭ 跳过重复视频")
            continue

        # 记录已下载的 URL
        downloaded_urls.add(video_url)

        # 打印视频 URL
        print(f"{idx}. {video_url}")

        # 保存视频到本地（内部有本地文件存在检查）
        save_video(video_url, video_title)

    except Exception as e:
        print(f"{idx}. Error: {e}")

print("=" * 30)
print(f"共提取到 {len(downloaded_urls)} 个唯一视频下载地址。")
