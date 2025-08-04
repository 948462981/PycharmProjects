from lxml import etree

tree = etree.parse("a.html")
# result = tree.xpath("/html")

# result = tree.xpath("/html/body/ul/li[1]/a/text()") # 从1开始数

# result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()") # [@xxx=xxx]

# result = tree.xpath("/html/body/ol/li")
#
# # print(result)
#
# for li in result:
#     res = li.xpath("./a/text()") # 相对查找
#     print(res)
#     res2 = li.xpath("./a/@href")
#     print(res2)
#
#
# print(tree.xpath("/html/body/ul/li/a/@href"))

print(tree.xpath("/html/body"))