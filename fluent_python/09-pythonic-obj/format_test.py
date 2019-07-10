# @Author: u14e
# @Time  : 2019/6/26 9:50
# @description:
from datetime import datetime

def run():
    brl = 1 / 2.43
    print(format(brl, '0.4f'))

    print(format(42, 'b'))
    print(format(2/3, '.1%'))

    now = datetime.now()
    print(format(now, '%H:%M:%S'))

if __name__ == '__main__':
    run()