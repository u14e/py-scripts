# @Author: u14e
# @Time  : 2019/2/25 11:24
# @description: 保留最后 N 个元素
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


def run():
    """返回文本匹配所在行的最后 N 行"""
    with open('somefile.txt', 'rt', encoding='utf-8') as f:
        for line, prevlines in search(f, 'Python', 5):
            for pline in prevlines:
                print(pline, end='')
            print('匹配的行:', line, end='')
            print('-' * 20)


if __name__ == '__main__':
    run()
