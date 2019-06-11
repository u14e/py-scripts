# @Author: u14e
# @Time  : 2019/1/22 16:31
# @description: 随机字符串
import os
import base64


def gen_urandom(n=10):
    s = os.urandom(n).hex()
    return s


def gen_base64():
    """
    base64编码
    echo -n "Aladdin:open sesame" | base64
    echo -n "QWxhZGRpbjpvcGVuIHNlc2FtZQ==" | base64 -d
    :return:
    """
    b = base64.b64encode(b'1232')
    d = base64.b64decode(b)
    print(b)
    print(d)


if __name__ == '__main__':
    r = gen_urandom(10)
    print(r)

    gen_base64()
