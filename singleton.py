# @Author: u14e
# @Time  : 2019/7/5 15:20
# @description: 单例
import functools

# 1. 使用 __new__
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

def single_test_1():
    class MyClass(Singleton):
        a = 1
    one = MyClass()
    two = MyClass()
    print(one == two)
    print(one is two)

# 2. 使用装饰器
def singleton(cls):
    instances = {}
    @functools.wraps(cls)
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

def single_test_2():
    @singleton
    class MyClass(object):
        a = 1

# 3. 元类
class Singleton1(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]

def single_test_3():
    class MyClass(metaclass=Singleton1):
        a = 1

if __name__ == '__main__':
    single_test_1()