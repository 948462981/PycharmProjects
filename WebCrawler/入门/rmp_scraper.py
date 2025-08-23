import requests
from bs4 import BeautifulSoup
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
professor_id = input("请输入教授ID：")

content = requests.get(f"https://www.ratemyprofessors.com/professor/{professor_id}", headers=headers)
response = content.text

soup = BeautifulSoup(response, "html.parser")

block = soup.find_all("div", attrs = {"class": "Rating__RatingBody-sc-1rhvpxz-0 hRXbIu"})
for block in block:
    rating_tag = block.find("div", class_ = re.compile("^CardNumRating__CardNumRatingNumber"))
    rating = rating_tag.text.strip()
    print(f"整体评分:{rating}")
    comment_tag = block.find("div", class_=re.compile("^Comments__StyledComments"))
    comment = comment_tag.text.strip()
    print(f"评论内容:\n{comment}\n")




# for r in rating:
#     rate = soup.find_all("div", attrs = {"class": "RatingValues__RatingContainer-sc-6dc747-WebCrawler dnVGEm"})
#     print(rate[0].string)

# for title in all_titles:
#     title_string = title.string
#     if "/" not in title_string:
#         print(title_string)

# CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 oNTzE
# CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 ERCLc
# CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 cmIXQn