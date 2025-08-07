import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

url = "https://m.bqgl.cc/"

resp = requests.get(url=url, headers=headers)

# 1. 把页面源代码交给BS处理，生成bs对象
page = BeautifulSoup(resp.text, "html.parser")
# 2. 从bs对象中查找数据
# find 和 find_all
with open("books.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    # 可选：写入表头
    writer.writerow(["分类1", "书名1", "作者1", "分类2", "书名2", "作者2"])

    tables = page.find_all("div", attrs={"class": "block"})
    for table in tables:
        uls = table.find_all("ul")
        for ul in uls:
            lis = ul.find_all("li")
            if len(lis) >= 6:
                row = [li.text.strip() for li in lis[:6]]
                writer.writerow(row)

print("over!")
resp.close()