# @Author: u14e
# @Time  : 2019/6/27 10:01
# @description: https://www.liaoxuefeng.com/wiki/1016959663602400/1017968846697824
def consumer():
    r = ''
    print('--- start generator ---')
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    print('starting generator')
    c.send(None)    # 启动生成器
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

def run():
    c = consumer()
    produce(c)

if __name__ == '__main__':
    run()
