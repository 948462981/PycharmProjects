import re

# # # findall: 寻找所有符合的内容
# lst = re.findall(r"\d+", "电影名称：肖申克的救赎，豆瓣评分：9.7，上映时间：1994-09-10")
#
# print(lst)
#
# #
# # # finditer: 找到所有符合的内容，返回一个迭代器
# it = re.finditer(r"\d+", "电影名称：肖申克的救赎，豆瓣评分：9.7，上映时间：1994-09-10")
# for i in it:
#     print(i.group())
#
# # # search:找到一个结果就返回，返回的结果是match对象，都需要.group()拿数据
# s = re.search(r"\d+", "电影名称：肖申克的救赎，豆瓣评分：9.7，上映时间：1994-09-10")
# print(s.group())
#
# # # match: 从头开始匹配，如果开头不符合，则返回None
# m = re.match(r"\d+", "电影名称：肖申克的救赎，豆瓣评分：9.7，上映时间：1994-09-10")
# # print(m.group())
#
# # 预加载regex
# obj = re.compile(r"\d+")
#
# ret = obj.finditer("电影名称：肖申克的救赎，豆瓣评分：9.7，上映时间：1994-09-10")
# for i in ret:
#     print(i.group())

s = """
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋铁</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡说八道</span></div>
"""
# (?P<name>regex)：给匹配到的内容起一个名字
obj = re.compile(r"<div class='(.*?)'><span id='(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>", re.S) #re.S：让.能匹配换行符

res = obj.finditer(s)
for i in res:
    print(i.group("id"))
    print(i.group("wahaha"))
