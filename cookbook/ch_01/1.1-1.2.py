# @Author: u14e
# @Time  : 2019/2/25 11:12
# @description: 解压可迭代对象赋值给多个变量


def simple_unzip():
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    print(name, shares, price, date)

    name, shares, price, (year, mon, day) = data
    print(name, shares, price, year, mon, day)

    # _ 忽略部分元素
    _, shares, price, _ = data
    print(shares, price)


def multi_unzip():
    # *表达式包含不确定个数的元素，组成列表(包括0个)
    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    name, email, *phones = record
    print(name, email, phones)

    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, *_, (*_, year) = data
    print(name, year)


def unzip_mutable_length():
    """*表达式应用于可变长元组序列"""
    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4),
    ]

    def echo_foo(x, y):
        print('foo', x, y)

    def echo_bar(s):
        print('bar', s)

    for tag, *args in records:
        if tag == 'foo':
            echo_foo(*args)
        elif tag == 'bar':
            echo_bar(*args)


if __name__ == '__main__':
    print('--- {} ---'.format(simple_unzip.__name__))
    simple_unzip()

    print('--- {} ---'.format(multi_unzip.__name__))
    multi_unzip()

    print('--- {} ---'.format(unzip_mutable_length.__name__))
    unzip_mutable_length()
