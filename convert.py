# @Author: u14e
# @Time  : 2019/7/9 10:19
# @description: 进制转换
import string

c = string.digits + string.ascii_letters

def dec_to_62(n):
    """十进制转换为其他进制"""
    r = []
    print(c)
    while n:
        r.insert(0, c[n % 62])
        n = n // 62
    return ''.join(r)

class Duck():
    def __init__(self):
        self.__name = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self):
        self.__name = '1'

if __name__ == '__main__':
    s = dec_to_62(201314)
    print(s == 'Qn0')
