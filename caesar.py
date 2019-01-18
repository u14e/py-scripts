# @Author: u14e
# @Time  : 2019/1/17 21:38
# @description: 凯撒密码


def convert(c, key, start='a', n=26):
    """将单个字母位移"""
    start_point = ord(start)
    offset = (ord(c) - start_point + key) % 26
    result = chr(start_point + offset)
    return result


def convert_lowercase(c, key):
    return convert(c, key, start='a')


def convert_uppercase(c, key):
    return convert(c, key, start='A')


def encrypt(msg, key):
    """加密"""
    o = ''
    for c in msg:
        if c.islower():
            o += convert_lowercase(c, key)
        elif c.isupper():
            o += convert_uppercase(c, key)
        else:
            o += c
    return o


def decrypt(msg, key):
    """解密"""
    return encrypt(msg, -key)


def decrypt_force(msg):
    """暴力解密"""
    for i in range(26):
        print(decrypt(msg, i))


if __name__ == '__main__':
    msg = 'Uhg fkxufk'
    decrypt_force(msg)
