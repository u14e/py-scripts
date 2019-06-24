# @Author: u14e
# @Time  : 2019/6/15 14:29
# @description: 启动和停止线程
import threading
import time

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(3)

def check_alive(thread):
    while True:
        if thread.is_alive():
            print('still running')
            time.sleep(1)
        else:
            print('completed')
            break

def setup_thread():
    """启动线程并检查运行状态"""
    t = threading.Thread(target=countdown, args=(10,), daemon=True)
    t.start()
    check_alive(t)

class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        """通过编程在某个特定点轮询来退出线程"""
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(3)

def exit_thread():
    """手动终止线程"""
    c = CountdownTask()
    t = threading.Thread(target=c.run, args=(5,), daemon=True)
    t.start()
    time.sleep(10)
    c.terminate()


def run():
    # setup_thread()
    exit_thread()

if __name__ == '__main__':
    run()
