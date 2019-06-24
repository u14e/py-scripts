# @Author: u14e
# @Time  : 2019/6/15 14:42
# @description: 判断线程是否已经启动
import threading
import time

def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(3)

def check_thread():
    # 默认初始信号为 False
    started_evt = threading.Event()
    t = threading.Thread(target=countdown, args=(5, started_evt))
    t.start()

    # 阻塞等待信号变为 True, 才执行后续操作
    # started_evt.set() 将信号变为 True
    started_evt.wait()
    print('countdown is truly running')

def worker(n, sema):
    sema.acquire()
    print('working', n)

def sema_test():
    """使用信号量唤醒单个线程"""
    sema = threading.Semaphore(0)
    nworkers = 10
    for n in range(nworkers):
        t = threading.Thread(target=worker, args=(n, sema))
        t.start()

    while True:
        print('sema release')
        sema.release()
        time.sleep(1)

def run():
    # check_thread()
    sema_test()

if __name__ == '__main__':
    run()
