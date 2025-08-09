# 如何提取单个页面的数据
# 上线程池，多个页面同时抓取

import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f = open("data.csv", mode="w", encoding='utf-8')
csvwriter = csv.writer(f)

def download_one_page(url):
    resp = requests.get(url)
    # print(resp.text)
    tree = etree.HTML(resp.text)
    table = tree.xpath("/html/body/div[4]/div/div[2]/div[1]/div/table")[0]
    # print(table)
    trs = table.xpath("./tr")
    # print(len(trs))
    for tr in trs:
        tds = tr.xpath("./td/text()")
        # print(tds)
        csvwriter.writerow(tds)
    print(url, "提取完毕")

if __name__ == '__main__':
    # download_one_page("http://www.ygzapm.com/web/dailyPrice?totalPageCount=14239&pageNow=1&product=&typeCode=")

    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):
            t.submit(download_one_page, f"http://www.ygzapm.com/web/dailyPrice?totalPageCount=14239&pageNow={i}&product=&typeCode=")

    print("全部下载完毕")