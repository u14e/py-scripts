# @Author: u14e
# @Time  : 2019/1/18 9:22
# @description: 打印错误
import traceback
import logging


def print_error():
    try:
        1 / 0
    except Exception as e:
        print('=' * 30, print_error.__name__, '=' * 30)
        print(traceback.format_exc())


def log_error():
    try:
        1 / 0
    except Exception as e:
        print('=' * 30, log_error.__name__, '=' * 30)
        logging.exception(e)


if __name__ == '__main__':
    print_error()
    log_error()
    print('-' * 30, 'end', '-' * 30)

