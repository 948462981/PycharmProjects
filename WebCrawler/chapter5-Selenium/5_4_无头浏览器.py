import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

opt = Options()
opt.add_argument('--headless') # 无头模式
opt.add_argument('--disable-gpu') # 禁用gpu加速
opt.add_experimental_option('detach', True)
web = Chrome(options=opt)
web.get('http://www.boxofficecn.com/the-red-box-office')

# sel_el = web.find_element(By.XPATH, '//*[@id="tablepress-4_length"]/label/select')
# # 包装成下拉菜单
# sel = Select(sel_el)
# # 选择下拉菜单的选项
# for i in range(len(sel.options)): # 每一个下拉框的option
#     sel.select_by_index(i)  # 按索引切换
#     time.sleep(2)
#     table = web.find_element(By.XPATH, '//*[@id="tablepress-4"]/tbody')
#     # print(table.text)
#     # print("=================")


print(web.page_source)