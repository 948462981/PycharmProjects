import requests

word = input("Input the word you want to translate: ")

dic = {
    "kw": word
}

url = "https://fanyi.baidu.com/sug"

content = requests.post(url, data=dic)

print(content.json())

content.close()