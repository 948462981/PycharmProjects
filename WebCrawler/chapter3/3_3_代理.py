import requests

# 112.126.68.169:8384

proxies = {
    "http": "http://112.126.68.169:8384"
}

resp = requests.get("https://www.baidu.com", proxies=proxies)

resp.encoding = 'utf-8'

print(resp.text)