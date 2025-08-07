
# https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224356290733%22}
#                                                    {"book_id": "4356290733"}  ==> （章节,price_status和CID）

# https://dushu.baidu.com/api/pc/getChapterContent?data={%22book_id%22:%224356290733%22,%22cid%22:%224356290733|1570569342%22,%22need_bookinfo%22:1}
                                                        #{"book_id":"4356290733","cid":"4356290733|1570569342","need_bookinfo":"1"}

import asyncio
import aiohttp
import requests
import json
import aiofiles
# 1. 同步访问getCatalog拿到所有章节的cid
# 2. 异步访问getChapterContent下载拿到章节内容



async def get_Catalog(url):
    resp = requests.get(url)
    # print(resp.json())
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        # print(title, cid)
        # 准备异步任务
        task = asyncio.create_task(aiodownload(cid, book_ID, title))
        tasks.append(task)
    await asyncio.wait(tasks)

async def aiodownload(cid, book_ID, title):
    data = {
        "book_id":book_ID,
        "cid":f"{book_ID}|{cid}",
        "need_bookinfo":"1"
    }
    data = json.dumps(data)
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            async with aiofiles.open(title, mode="w", encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])
                print(title, "Done")


if __name__ == '__main__':
    book_ID = "4356290733"
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + book_ID + '"}'
    asyncio.run(get_Catalog(url))
