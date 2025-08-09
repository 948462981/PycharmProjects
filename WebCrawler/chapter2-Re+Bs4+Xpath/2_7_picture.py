import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

url = "https://www.vcg.com/"

resp = requests.get(url=url, headers=headers)

main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", attrs={"class": "_3Kq5K"}).find_all("a")

for a in alist:
    child_href = url.replace("//www.vcg.com/", "//www.vcg.com") + a.get('href')
    child_href_resp = requests.get(url=child_href, headers=headers)
    child_page = BeautifulSoup(child_href_resp.text, "html.parser")
    blist = child_page.find("div", attrs={"class": "relativePosition"})
    img_tag = blist.find("img")
    src = img_tag.get('src')
    if src.startswith("//"):
        src = "https:" + src
    img_resp = requests.get(src)
    # img_resp.content
    img_name = src.split("/")[-1]
    with open("img/" + img_name, "wb") as f:
        f.write(img_resp.content)

    print("over!!!", img_name)
    time.sleep(1)

print("All over!")
resp.close()
