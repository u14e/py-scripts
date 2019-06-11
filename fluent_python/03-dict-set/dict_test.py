# @Author: u14e
# @Time  : 2019/5/27 17:03
# @description:
import re
from collections import defaultdict

WORD_RE = re.compile(r'\w+')


def print_word(index):
    for word in sorted(index, key=str.upper):
        print(word, index[word])


def map_word():
    """统计单词出现的频率"""
    index = {}
    with open('zen.txt', encoding='utf-8') as f:
        for line_no, line in enumerate(f, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)

                # occurrences = index.get(word, [])
                # occurrences.append(location)
                # index[word] = occurrences

                index.setdefault(word, []).append(location)

    print_word(index)


def map_word_2():
    index = defaultdict(list)
    with open('zen.txt', encoding='utf-8') as f:
        for line_no, line in enumerate(f, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)

                index[word].append(location)

    print_word(index)


def immutable_map():
    """不可变映射"""
    from types import MappingProxyType
    d = {1: 'A'}
    d_proxy = MappingProxyType(d)   # 会返回一个只读的映射视图
    print(d_proxy)
    print(d_proxy[1])
    # d_proxy[2] = 'B'  # 不能通过这个视图对原映射做出修改
    d[2] = 'B'          # 对原映射做出了改动, 视图也改变
    print(d_proxy)


if __name__ == '__main__':
    # map_word()
    # map_word_2()
    immutable_map()
