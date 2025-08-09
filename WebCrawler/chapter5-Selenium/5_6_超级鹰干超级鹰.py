import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client


opt = Options()
opt.add_experimental_option('detach', True)

web = Chrome(options=opt)
web.get('https://www.chaojiying.com/user/login/')
# /html/body/div[3]/div/div[3]/div[1]/form/p[1]/input
# 处理验证码
img = web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('948462981', '7ngzs2y1', '972175')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']

# 向页面填入验证码，用户名和密码登录
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("948462981")
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys("7ngzs2y1")
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)

time.sleep(5)
# 点击登录
web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()