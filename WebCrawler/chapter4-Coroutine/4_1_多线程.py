# 线程，进程
# 进程是资源单位，每一个进程至少要有一个线程
# 线程是执行单位
from threading import Thread

class MyThread(Thread):  # 继承Thread类
    def run(self):
        for i in range(1000):
            print("子线程", i)

if __name__ == '__main__':
    t = MyThread()
    # t.run() # wrong
    t.start()

    for i in range(1000):
        print("主线程", i)