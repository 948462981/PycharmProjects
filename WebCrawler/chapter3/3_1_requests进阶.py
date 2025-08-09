# 带着cookie 去请求到书架url书架上的内容
#必须得把上面的两个操作连起来# 我们可以使用session进行请求session你可以认为是一连串的请求，在这个过程中的cookie不会丢失
import requests
# 会话
# session =requests.session()
# data ={
#     "loginName":"1861407597",
#     "password":"q6035945"
# }
# # 1.登录
# url = "https://passport.17k.com/ck/user/login"
# session.post(url,data=data)
#
# # print(resp.text)
# # print(resp.cookies)#看cookie
#
# # 2.拿书架上的数据
# # 刚才的那个session中是有cookie的
# resp = session.get('https://user.17k,com/ck/author/shelf?page=1&appKey=2406394919')
# print(resp.json())


resp = requests.get("https://user.17k,com/ck/author/shelf?page=1&appKey=2406394919", headers = {
    "Cookie": "..."
}) # 和上面一个效果

print(resp.text)