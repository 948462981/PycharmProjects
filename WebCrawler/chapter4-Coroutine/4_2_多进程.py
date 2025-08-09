from  multiprocessing import Process
from  threading import Thread

# def func():
#     for i in range(1000):
#         print("子进程", i)
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()
#     for i in range(1000):
#         print("主进程", i)

def func(name):
    for i in range(1000):
        print("子进程", name, i)

if __name__ == '__main__':
    t1 = Thread(target=func, args=("a",)) # 传参必须是tuple
    t1.start()

    t2 = Thread(target=func, args=("b",))
    t2.start()