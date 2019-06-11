# @Author: u14e
# @Time  : 2019/4/19 15:51
# @description:
import hashlib
import base64
import hmac


def sign(source, secret):
    if not isinstance(source, bytes):
        source = source.encode('utf-8')
    if not isinstance(secret, bytes):
        secret = secret.encode('utf-8')
    h = hmac.new(secret, source, hashlib.sha256)
    signature = base64.encodebytes(h.digest()).decode('utf-8')
    return signature


if __name__ == '__main__':
    dic = {'a': 1}
    s = sign('helkkl', 'my')
    print(s)
    dic['s'] = s
    print(dic)