import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
opt = Options()
opt.add_experimental_option('detach', True)
web = Chrome(options=opt)
web.get('https://www.exception.site/')
# web.find_element(By.XPATH, '//*[@id="kw"]').send_keys('小电拼', Keys.ENTER)
# time.sleep(1)
web.find_element(By.XPATH, '/html/body/main/section[1]/div/a[1]/div[2]/h3').click()
time.sleep(1)
# 切换到新窗口
web.switch_to.window(web.window_handles[-1])
a = web.find_element(By.XPATH, '//*[@id="content"]/p[9]/a').text
# print(a)

web.close()
web.switch_to.window(web.window_handles[0])
