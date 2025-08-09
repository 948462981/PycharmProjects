from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time



# opt.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
opt = Options()
opt.add_argument("--no-sandbox")
# opt.add_argument('--proxy-server=http://118.178.197.213:3128')
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_experimental_option("detach", True)
web = Chrome(options=opt)
web.get("https://www.91porn.com/v.php?category=hot&viewtype=basic")
time.sleep(3)
html = web.page_source

page = BeautifulSoup(html, "html.parser")
tables = page.find_all("div", attrs={"class": "col-xs-12 col-sm-4 col-md-3 col-lg-3"})
# print(tables)
for table in tables:
    title = table.find_all("span", attrs={"class": "video-title title-truncate m-t-5"})
    # print(title[0].text)
    video_links = table.find_all("a")
    print(video_links[0]["href"])
    videos = [video_links[0]["href"]]
    for video in videos:
        web.get(video)
        try:
            source_elem = WebDriverWait(web, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "source"))
            )
            video_url = source_elem.get_attribute("src")
        except Exception as e:
            print("Does not find the url",e)
