from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

opt = Options()
opt.add_experimental_option('detach', True)
web = Chrome(options=opt)
web.get("https://m.bqgl.cc/")
# el = web.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[4]/div[2]')
# el.click()

time.sleep(1) # 让浏览器缓一下

# 找到输入框，输入pvthon => 論入回车/点击搜索按钮
web.find_element(By.XPATH, '/html/body/div[4]/form/input[1]').send_keys('斗罗大陆', Keys.ENTER)
items = web.find_elements(By.XPATH, '/html/body/div[3]/div/div') #/html/body/div[3]/div/div
for item in items:
    book_name = item.find_element(By.XPATH, './div[1]/dl/dt/span').text
    print(book_name)