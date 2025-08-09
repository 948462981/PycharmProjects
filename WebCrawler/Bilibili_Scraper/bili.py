import requests
import subprocess
video_url = "https://upos-sz-mirroraliov.bilivideo.com/upgcxcode/84/10/31130651084/31130651084-1-100027.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&mid=172355420&deadline=1752905160&os=aliovbv&uipk=5&oi=1645069194&platform=pc&trid=14e483373953413299daedb7ef3dbaeu&nbs=1&gen=playurlv3&og=hw&upsig=a683f3bc0351b38777e044791ecca798&uparams=e,mid,deadline,os,uipk,oi,platform,trid,nbs,gen,og&bvc=vod&nettype=0&bw=1293261&buvid=AFE9CBBF-53A3-3DA4-74F4-20F9D44C2FB861359infoc&build=0&dl=0&f=u_0_0&agrr=0&orderid=0,2"
audio_url = "https://upos-hz-mirrorakam.akamaized.net/upgcxcode/84/10/31130651084/31130651084-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&os=akam&mid=172355420&deadline=1752905160&nbs=1&trid=14e483373953413299daedb7ef3dbaeu&og=hw&uipk=5&oi=1645069194&platform=pc&gen=playurlv3&upsig=3a2f4d080266766943120aee870dbae5&uparams=e,os,mid,deadline,nbs,trid,og,uipk,oi,platform,gen&hdnts=exp=1752905160~hmac=543f149f7b0095ec094380283211a5f255bdc243eb95cbcffb5fcebd92fe03f6&bvc=vod&nettype=0&bw=172932&agrr=0&buvid=AFE9CBBF-53A3-3DA4-74F4-20F9D44C2FB861359infoc&build=0&dl=0&f=u_0_0&orderid=0,2"

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    'referer': "https://www.bilibili.com/video/BV1cguUzVECy/?spm_id_from=333.1365.list.card_archive.click&vd_source=6830a2f6f6e0d5685cbdb777631ede58"
}

# 下载视频
res = requests.get(video_url, headers=headers)
if res.status_code == 200:
    with open("video.mp4", "wb") as f:
        f.write(res.content)
else:
    print("视频下载失败", res.status_code)

# 下载音频
res = requests.get(audio_url, headers=headers)
if res.status_code == 200:
    with open("audio.mp3", "wb") as f:
        f.write(res.content)
else:
    print("音频下载失败", res.status_code)

# 合并音视频

cmd = [
    "ffmpeg",
    "-i", "video.m4s",
    "-i", "audio.m4s",
    "-c:v", "copy",       # 视频流直接拷贝（不转码）
    "-c:a", "aac",        # 音频转为 AAC
    "-strict", "experimental",
    "-y",                 # 如果已存在，自动覆盖
    "output.mp4"
]

subprocess.run(cmd)

print("✅ 合并完成！已保存为 output.mp4")