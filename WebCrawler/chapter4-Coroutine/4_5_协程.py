# import time
#
# def func():
#     print("我爱黎明")
#     time.sleep(3)# 让当前的线程处于阻塞状态。CPU是不为我工作的
#     print("我真的爱黎明")
#
#
# if __name__ == '__main__':
#     func()

# input()程序也是处于阻塞状态
# requests.get(bilibili)在网络请求返回数据之前，程序也是处于阻塞状态的
# 一般情况下，当程序处于 I0操作的时候。线程都会处于阻塞状态

import asyncio
import time
from itertools import takewhile


# async def func():
#     print("s123")
#
#
# if __name__ == '__main__':
#     g = func()
#     asyncio.run(g)  #协程程序运行需要asyncio模块的支持


# async def func1():
#     print("1")
#     # time.sleep(2) 当程序出现了同步操作的时候，异步就中断了
#     await asyncio.sleep(2)  # 异步操作的代码
#     print("2")
# async def func2():
#     print("3")
#     await asyncio.sleep(3)
#     print("4")
# async def func3():
#     print("5")
#     await asyncio.sleep(5)
#     print("6")
#
# async def main():
#     tasks = [
#         asyncio.create_task(func1()),
#         asyncio.create_task(func2()),
#         asyncio.create_task(func3()),
#     ]
#     await asyncio.wait(tasks)
#
# if __name__ == '__main__':
#     t1 = time.time()
#     asyncio.run(main())
#     t2 = time.time()
#     print(t2-t1)
#


# 爬虫应用
async def download(url):
    print("ready to download")
    await asyncio.sleep(2)
    print("download successfully")

async def main():
    urls = [
        "https://www.bilibili.com/",
        "https://www.baidu.com/",
        "https://yandex.com/",
    ]

    tasks = []
    for url in urls:
        d = download(url)
        task = asyncio.create_task(d) # ✅ 创建任务
        tasks.append(task) # n 个协程对象 # ✅ 加入任务列表
    # tasks = [asyncio.create_task(download(url)) for url in urls]

    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())

# # 使用 gather()：
# import asyncio
#
# async def foo(i):
#     await asyncio.sleep(i)
#     return f"done {i}"
#
# async def main():
#     results = await asyncio.gather(foo(2), foo(1), foo(3))
#     print(results)  # ['done 2', 'done 1', 'done 3']
#
# asyncio.run(main())
#
# # 使用 wait()：
# import asyncio
#
#
# async def foo(i):
#     await asyncio.sleep(i)
#     return f"done {i}"
#
#
# async def main():
#     tasks = [asyncio.create_task(foo(i)) for i in [2, 1, 3]]
#     done, pending = await asyncio.wait(tasks)
#
#     for task in done:
#         print(task.result())  # 输出顺序不保证
#
#
# asyncio.run(main())
