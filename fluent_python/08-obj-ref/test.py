def f(a, b):
    a += b
    return a


def param_share_test():
    """
    Python 唯一支持的参数传递模式是共享传参
    共享传参指函数的各个形式参数获得实参中各个引用的副本
    感觉就是浅复制
    """
    x1, y1 = 1, 2
    print(f(x1, y1))  # 3
    print(x1, y1)     # 1 2

    x2, y2 = [1, 2], [3, 4]
    print(f(x2, y2))    # [1, 2, 3, 4]
    print(x2, y2)       # [1, 2, 3, 4] [3, 4]

    x3, y3 = (10, 20), (30, 40)
    print(f(x3, y3))    # (10, 20, 30, 40)
    print(x3, y3)       # (10, 20) (30, 40)


if __name__ == '__main__':
    param_share_test()
