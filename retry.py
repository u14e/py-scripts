# @Author: u14e
# @Time  : 2019/1/14 13:39
# @description: 代码重试

import time
import traceback
import random


def retry(max_retries: int):
    random.seed(1560)   # 使得结果如预期
    print('-----开始执行-----')
    for i in range(max_retries):
        if i > 0:
            print('第{0}次重试: {1}'.format(i, time.strftime('%Y-%m-%d %H:%M:%S')))
        time.sleep(i * 2)

        try:
            result = random.randint(0, 1) / random.randint(0, 1)
        except ZeroDivisionError:
            print('>>>error happened<<<', time.strftime('%Y-%m-%d %H:%M:%S'))
            print(traceback.format_exc())
            if i == max_retries - 1:
                raise
            continue
        else:
            return result


if __name__ == '__main__':
    r = retry(10)
    print(r)
