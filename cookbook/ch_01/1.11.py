# @Author: u14e
# @Time  : 2019/3/2 10:07
# @description: 命名切片


def slice_test():
    """slice 切片对象"""
    items = [0, 1, 2, 3, 4, 5, 6]
    a = slice(2, 4)
    print(items[a])
    print(items[2:4])
    print(f'start: {a.start}; stop: {a.stop}; step: {a.step}')


def slice_indices_test():
    """
    indices(size)
    返回一个三元组 (start, stop, step) ，所有的值都会被缩小，直到适合这个已知序列的边界为止
    这样，使用的时就不会出现 IndexError 异常
    :return:
    """
    s = 'HelloWorld'
    a = slice(5, 50, 2)
    result = a.indices(len(s))  # (5, 10, 2)
    print(result)
    print(s[a])

    for i in range(*result):
        print(s[i])


def run():
    slice_test()
    slice_indices_test()


if __name__ == '__main__':
    run()
