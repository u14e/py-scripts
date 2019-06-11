# @Author: u14e
# @Time  : 2019/5/27 10:43
# @description: 默认情况下，我们自己定义的类的实例总被认为是真的，
#   除非这个类对 __bool__ 或者 __len__ 函数有自己的实现。
#   bool(x) 的背后是调用 x.__bool__() 的结果；
#   如果不存在 __bool__ 方法，那么 bool(x) 会 尝试调用 x.__len__()。
#   若返回 0，则 bool 会返回 False；否则返回 True。


class MyObject(object):
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __bool__(self):
        return bool(self.n)


if __name__ == '__main__':
    m1 = MyObject(0)
    m2 = MyObject(1)
    print(bool(m1), bool(m2))
