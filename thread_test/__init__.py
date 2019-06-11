# @Author: u14e
# @Time  : 2019/2/14 15:31
# @description:
import threading
import time

threads = []
lock = threading.Lock()

g_num = 1
semaphore = threading.Semaphore(0)


class Num:
    def __init__(self):
        lock.acquire()
        self.num = g_num
        lock.release()

    def echo(self):
        print(self.num)


def init_num():
    num = Num()
    while True:
        num.echo()
        time.sleep(2)


def thread_1():
    init_num()
    while True:
        semaphore.acquire()
        init_num()


def change_g_num(num):
    lock.acquire()
    global g_num
    g_num = num
    lock.release()


def thread_2():
    """修改全局变量 g_num, 并重启thread_1"""
    for i in range(10, 15):
        change_g_num(i)
        semaphore.release()
        time.sleep(2)


def run():
    t1 = threading.Thread(name='thread_1', target=thread_1)
    threads.append(t1)
    t1.start()

    t2 = threading.Thread(name='thread_2', target=thread_2)
    threads.append(t2)
    t2.start()


if __name__ == '__main__':
    run()
