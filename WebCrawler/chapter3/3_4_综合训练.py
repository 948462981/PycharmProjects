# 1. 找到未加密参数   windows.arsea(...)
# 2. 想办法把参数加密 params  => encText, encSecKey => encSecKey
# 3. 发送请求, 拿到评论

from Crypto.Cipher import AES
from base64 import b64encode
import requests
import json

data = { # 字典
    "csrf_token": "65fffafe608c14540dc8eed7f02ec8f1",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_2610610209",
    "threadId": "R_SO_4_2610610209"
}


# 服务于d的
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
e = "010001"
i = "4CWLD8ERvcWa1v3U" # 手动固定， 人家是随机

def get_encSecKey():  # 由于i固定， 这个函数也是固定的
    return "26226134b5163683a015c84a198305a944de22bb21074d74ef90b1eb3085ec8b2cf117e90f6a6774942c1f242d37ebb56be31f201a067842e15200248a306c0b1fb15127a91d1497cd0291453813c22a8a8907cd0b7e681369f8312ec199807a7de7376f028fdb920472747988019847d72b000d2314cf94a7e1248832f02432"

def get_params(data):  # 默认收到的是字符串
    first_encode = enc_params(data, g)
    sec_encode = enc_params(first_encode, i)
    return sec_encode

def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

def enc_params(data, key):
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC) # 创建加密器
    bs = aes.encrypt(data.encode("utf-8")) # 加密, 内容必须16的倍数
    return str(b64encode(bs), "utf-8")  #转化成字符串返回


# 处理加密过程
"""
    function a(a) {  # 随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)  # 循环16次
            e = Math.random() * b.length,  # 随机数
            e = Math.floor(e),   # 向下取整
            c += b.charAt(e);   # 取字符串
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)  # e是数据
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,   # 偏移量
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {  # d = 数据, e = 010001, f = 很长, g = 0CoJUm6Qyw8W8jud
        var h = {}
          , i = a(16);   # 16位的随机值， 设置成定值
        return h.encText = b(d, g),  # 两次加密，第一次是数据和g，第二次是第一次和i， g是密钥
        h.encText = b(h.encText, i),  # 返回的是params                       i也是密钥
        h.encSecKey = c(i, e, f),   # 返回的是encSecKey, e和f是固定的，如果把i固定, 得到的key一定是固定的
        h
    }
"""

# headers = {
#
# }

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token=" #71978e74d33fc2338b10e9cbfd81c8bc

resp = requests.post(url=url, data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSecKey()
})

print(resp.text)