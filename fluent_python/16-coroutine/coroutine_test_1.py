# @Author: u14e
# @Time  : 2019/6/27 15:00
# @description:
from inspect import getgeneratorstate
import coroutil

def simple_coroutine_1():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)

def test_simple_coroutine_1():
    cor = simple_coroutine_1()
    print(cor)
    cor.send(None)  # 激活协程
    print(cor.send(42))

def simple_coroutine_2(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)

def test_simple_coroutine_2():
    cor = simple_coroutine_2(14)
    print(getgeneratorstate(cor))   # GEN_CREATED
    r = cor.send(None)
    print(r)
    print(getgeneratorstate(cor))   # GEN_SUSPENDED
    r = cor.send(28)
    print(r)
    r = cor.send(99)
    print(r)

@coroutil.coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

@coroutil.coroutine
def averager_2():
    """在最后返回一个值(计算累积值)"""
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return count, average

def test_averager():
    cor_avg = averager()
    print(getgeneratorstate(cor_avg))
    print(cor_avg.send(10))
    print(cor_avg.send(30))
    print(cor_avg.send(5))
    cor_avg.close()

    cor_avg_2 = averager_2()
    cor_avg_2.send(10)
    cor_avg_2.send(30)
    cor_avg_2.send(6.5)
    try:
        cor_avg_2.send(None)
    except StopIteration as exec:
        # 捕获异常, 获取返回值
        r = exec.value
    print(r)

if __name__ == '__main__':
    # test_simple_coroutine_1()
    # test_simple_coroutine_2()
    test_averager()
