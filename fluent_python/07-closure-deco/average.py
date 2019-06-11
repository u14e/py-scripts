# 计算平均值(面向对象)
class Average(object):

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


# 计算平均值(函数式)
def make_average():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


def make_average_plus():
    count = 0
    total = 0

    def averager(new_value):
        # nonlocal 把变量标记为自由变量
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


def avg_oop():
    avg = Average()
    print(avg(10))
    print(avg(11))
    print(avg(12))


def avg_func():
    avg = make_average()
    print(avg(10))
    print(avg(11))
    print(avg(12))

    print(avg.__code__)  # 返回函数定义体
    print(avg.__code__.co_varnames)  # 局部变量
    print(avg.__code__.co_freevars)  # 自由变量: 未在本地作用域中绑定的变量
    print(avg.__closure__[0])  # 第一个 cell 对象 (即 series)
    print(avg.__closure__[0].cell_contents) # 获取第一个自由变量的值 (即 [10, 11, 12])


if __name__ == '__main__':
    # avg_oop()
    avg_func()
