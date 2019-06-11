# @Author: u14e
# @Time  : 2019/2/25 14:55
# @description: 字典的相关操作
from collections import defaultdict, OrderedDict


def dict_multi_value():
    """
    实现一个键对应多个值的字典
    :return:
    """
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)

    print(d)


def dict_order():
    """
    字典排序
    :return:
    """
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4

    # 在迭代操作的时候它会保持元素被插入时的顺序
    for key in d:
        print(key, d[key])


def dict_max_and_min():
    """
    字典的运算(求最小值、最大值、排序)
    :return:
    """
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    # 使用 zip() 函数先将键和值反转过来
    # 注意: zip() 函数创建的是一个只能访问一次的迭代器
    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))
    print(min_price, max_price)

    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    print(prices_sorted)

    # 不用 zip
    min_key = min(prices, key=lambda k: prices[k])
    min_value = prices[min_key]
    print(min_key, min_value)


def dict_common():
    """
    在两个字典中寻寻找相同点（比如相同的键、相同的值等等）
    :return:
    """
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    print(a.keys() & b.keys())

    # 以现有字典构造一个排除几个指定键的新字典
    c = {key: a[key]
         for key in a.keys() - {'z', 'w'}}
    print(c)


def run():
    # dict_multi_value()
    # dict_order()
    # dict_max_and_min()
    dict_common()


if __name__ == '__main__':
    run()
