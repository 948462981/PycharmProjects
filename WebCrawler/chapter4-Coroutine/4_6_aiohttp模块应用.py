# requests get()同步的代码-> 异步操作

import aiohttp
import asyncio

urls = [
    "https://vcg01.cfp.cn/creative/vcg/800/new/VCG211553848274-EUS.jpg",
    "https://vcg00.cfp.cn/creative/vcg/800/new/VCG41N1427804808.jpg",
    "https://vcg03.cfp.cn/creative/vcg/800/new/VCG211525391899.jpg"
]

async def aiodownload(url):
    name = url.rsplit("/", 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
                                                # resp.content.read()  # ==> resp.content
            with open(name, mode="wb") as f:
                f.write(await resp.content.read())  # 读取是异步的需要await
    print(name, "Done")
    # s = aiohttp.ClientSession() # <==> requests
    # requests.get()  .post()
    # s.get()   s.post()
    # 发送请求
    # 得到图片内容
    # 保存到文件


async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(aiodownload(url))
        tasks.append(task)
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())