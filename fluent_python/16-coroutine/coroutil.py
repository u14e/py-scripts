# @Author: u14e
# @Time  : 2019/6/27 15:17
# @description:
from functools import wraps

def coroutine(func):
    """
    激活协程的装饰器
    :param func: 生成器函数
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        gen.send(None)  # 激活协程
        return gen
    return wrapper