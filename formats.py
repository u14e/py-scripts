# @Author: u14e
# @Time  : 2019/1/17 15:28
# @description: 数据格式化 (https://realpython.com/python-string-formatting/)
from string import Template


def format_1():
    """
    % 格式化
    https://docs.python.org/3/library/stdtypes.html#old-string-formatting
    """
    result = 'Hey %s, there is a 0x%x error!' % (name, errno)
    print(result)

    result = 'Hey %(name)s, there is a 0x%(errno)x error!' % {"name": name,
                                                              "errno": errno}
    print(result)


def format_2():
    """
    str.format 格式化
    https://docs.python.org/3/library/stdtypes.html#str.format
    """
    result = 'Hey {}, there is a 0x{:x} error!'.format(name, errno)
    print(result)

    result = 'Hey {name}, there is a 0x{errno:x} error!'.format(name=name,
                                                                errno=errno)
    print(result)


def format_3():
    """
    f-strings 格式化(Python3.6)
    https://realpython.com/python-f-strings/
    """
    result = f'Hey {name}, there is a 0x{errno:#x} error!'
    print(result)

    a, b = 5, 10
    result = f'Five plus ten is {a + b} and not {2 * (a + b)}.'
    print(result)


def format_4():
    """
    Template strings 格式化
    功能有限，只用于处理用户输入的数据
    """
    templ_string = 'Hey $name, there is a $error error!'
    result = Template(templ_string).substitute(name=name,
                                               error=hex(errno))
    print(result)


def attack():
    """
    利用format安全漏洞通过全局作用域读取密钥
    :return:
    """
    user_input = '{error.__init__.__globals__[SECRET]}'
    err = Error()
    result = user_input.format(error=err)
    print(result)


def fix_attack():
    """
    使用 Template strings 修复安全漏洞
    :return:
    """
    user_input = '${error.__init__.__globals__[SECRET]}'
    err = Error()
    try:
        result = Template(user_input).substitute(error=err)
        print(result)
    except Exception:
        import traceback
        print('=' * 30, 'Exception', '=' * 30)
        print(traceback.format_exc())


class Error:
    def __init__(self):
        pass


if __name__ == '__main__':
    name = 'Bob'
    errno = 50159747054
    SECRET = 'this-is-a-secret'     # 密钥

    print('=' * 30, format_1.__name__, '=' * 30)
    format_1()
    print('=' * 30, format_2.__name__, '=' * 30)
    format_2()
    print('=' * 30, format_3.__name__, '=' * 30)
    format_3()
    print('=' * 30, format_4.__name__, '=' * 30)
    format_4()

    print('=' * 30, attack.__name__, '=' * 30)
    attack()
    print('=' * 30, fix_attack.__name__, '=' * 30)
    fix_attack()