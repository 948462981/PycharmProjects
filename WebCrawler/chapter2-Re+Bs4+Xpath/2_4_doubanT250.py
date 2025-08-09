import re
import requests
import csv

f = open("douban_data.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)
for i in range(0, 250, 25):
    url = f"https://movie.douban.com/top250?start={i}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    res = requests.get(url=url, headers=headers)

    page_content = res.text

    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<movie_Name>.*?)</span>.*?'
                     r'<p>.*?<br>(?P<movie_Year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<movie_Rating>.*?)</span>'
                     r'.*?<span>(?P<review_Num>.*?)人评价</span>', re.S)

    result = obj.finditer(page_content)


    for i in result:
        # print(i.group("movie_Name").strip())
        # print(i.group("movie_Year").strip())
        # print(i.group("movie_Rating").strip())
        # print(i.group("review_Num").strip())
        dic = i.groupdict()
        dic['movie_Year'] = dic['movie_Year'].strip()
        csvwriter.writerow(dic.values())


    res.close()

f.close()
print("over!")