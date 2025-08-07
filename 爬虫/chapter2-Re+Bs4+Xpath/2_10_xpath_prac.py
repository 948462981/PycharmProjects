import requests
from lxml import etree
import os
import time

url = "https://pic.netbian.com/4kdongman/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

resp = requests.get(url=url, headers=headers)
resp.encoding = "gbk"

# print(resp.text)

# 解析
html = etree.HTML(resp.text)

divs = html.xpath("/html/body/div[2]/div/div[4]/ul/li")

os.makedirs("img2", exist_ok=True)

for div in divs:
    img_title = div.xpath("./a/b/text()")
    # print(img_title)
    img_url = 'https://pic.netbian.com' + div.xpath("./a/img/@src")[0]
    print(img_url)

    img_resp = requests.get(url=img_url, headers=headers)

    file_path = f"img2/{img_title}.jpg"

    with open(file_path, 'wb') as f:
        f.write(img_resp.content)
        print(img_title, "下载成功")

    time.sleep(1)

print("All over!")
resp.close()