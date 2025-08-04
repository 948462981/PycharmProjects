import requests

url = "https://www.pearvideo.com/video_1801321"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Referer": url # 防盗链
}

contId = url.split("_")[1]

videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.36663787406461057"

resp = requests.get(url=videoStatusUrl, headers=headers)

dic = resp.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']

# "https://video.pearvideo.com/mp4/short/20250714/1753839233553-16056973-hd.mp4"
srcUrl = srcUrl.replace(systemTime, "cont-" + contId)

with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)

resp.close()