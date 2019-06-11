# @Author: u14e
# @Time  : 2019/2/15 11:45
# @description:
import threading
import time


class Count:
    def __init__(self):
        self.num = 0


count = Count()
lock = threading.Lock()


def thread_1():
    while True:
        lock.acquire()
        print(threading.current_thread().getName(),
              count.num)
        lock.release()
        time.sleep(2)


def thread_2():
    num = 0
    while True:
        lock.acquire()
        if num % 5 == 0:
            count.num = 0
        else:
            count.num += 1
        lock.release()
        num += 1
        time.sleep(1)


def run():
    t1 = threading.Thread(target=thread_1, name='thread_1')
    t1.setDaemon(True)
    t1.start()

    t2 = threading.Thread(target=thread_2, name='thread_2')
    t2.setDaemon(True)
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    run()
