# @Author: u14e
# @Time  : 2019/6/27 15:39
# @description:

# 对 yield from 结构来说, 解释器不仅会捕获 StopIteration 异常，
# 还会把 value 属性的值变成 yield from 表达式的值。

def chain(*iterables):
    for it in iterables:
        # 调用 iter(it)，从 中获取迭代器
        yield from it

def test_chain():
    s = 'ABC'
    t = tuple(range(3))
    print(list(chain(s, t)))

# 子生成器
def averager():
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

# 委派生成器
def grouper(results, key):
    while True:
        results[key] = yield from averager()

# 调用方
def client(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)
    report(results)

# 输出报告
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result[0],
            group,
            result[1],
            unit
        ))

def test_client():
    data = {'girls;kg': [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
            'girls;m': [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
            'boys;kg': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
            'boys;m': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46], }
    client(data)

if __name__ == '__main__':
    # test_chain()
    test_client()
