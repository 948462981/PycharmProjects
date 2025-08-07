import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from chaojiying import Chaojiying_Client


opt = Options()
opt.add_experimental_option('detach', True)

# 如果你的程序被识别到了怎么办?
#1.chrome的版本号如果小于88 在你启动浏览器的时候(此时没有加载任何网页内容)，向页面嵌入js代码. 去掉webdriver
# web = Chrome()
# web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#   "source": """
#   window.navigator.webdriver = undefined
#     Object.defineProperty(navigator, 'webdriver', {
#         get: () => undefined
#     })
#   """
# })
# web.get(xxxxx)

# 2.chrome的版本大于等于88
# opt = Options()
# opt.add_experimental_option('excludeSwitches', ['enable-automation'])
# opt.add_argument('--disable-blink-features=AutomationControlled')
# web = Chrome(options=opt)

web = Chrome(options=opt)
web.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(2)
# web.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[2]/div[2]/ul/li[2]/a').click()
# time.sleep(3)

# 图像验证识别
# verify_img_elem = web.find_element(By.XPATH, '...')
# chaojiying = Chaojiying_Client('948462981', '7ngzs2y1', '972175')
# dic = chaojiying.PostPic(verify_img_elem.screenshot_as_png, 9004)
# result = dic['pic_str']
# rs_list = result.split('|')
# for rs in rs_list:
#     p_temp = rs.split(',')
#     x = int(p_temp[0])
#     y = int(p_temp[1])
#     #要让鼠标移动到某一个位置，然后进行点击
#     ActionChains(web).move_to_element_with_offset(verify_img_elem, x, y).click().perform()

time.sleep(2)
web.find_element(By.XPATH, '// *[ @ id = "J-userName"]').send_keys('123455657889')
web.find_element(By.XPATH, '//*[@id="J-password"]').send_keys('213456787')
web.find_element(By.XPATH, '//*[@id="J-login"]').click()

time.sleep(2)

# 拖拽验证
btn = web.find_element(By.XPATH, 'XXXXX')
ActionChains(web).drag_and_drop_by_offset(btn, 300, 0).perform()