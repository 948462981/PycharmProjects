#1.定位到2020必看片
#2.从2020必看片中提取到子页面的链接地址
#3.请求子页面的链接地址，拿到我们想要的下载地址...

import requests
import re

domain = "https://dytt8.com/index.htm"
resp = requests.get(url=domain, verify=False)
resp.encoding = 'gb2312'

# 拿到ul里面的tr
obj1 = re.compile(r'2023新片精品.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2 = re.compile(r'\[<a.*?</a>]<a href=\'(?P<href>.*?)\'>', re.S)
obj3 = re.compile(r'<div class="title_all"><h1><font color=#07519a>(?P<movie_Title>.*?)</font>.*?'
                  r'" target="_blank" href="(?P<download>.*?)">', re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []
for i in result1:
    ul = i.group('ul')
    # print(ul)

    # 提取子页面连接
    result2 = obj2.finditer(ul)
    for j in result2:
        # 拼接子页面连接
        child_href = domain.replace("/index.htm", "") + j.group('href')
        child_href_list.append(child_href)
        # print(child_href_list)

# 提取子页面内容

for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = 'gb2312'
    # print(child_resp.text)
    result3 = obj3.search(child_resp.text)
    print(result3.group('movie_Title'))
    print(result3.group('download'))
    child_resp.close()

resp.close()