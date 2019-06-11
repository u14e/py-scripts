# @Author: u14e
# @Time  : 2019/3/2 10:37
# @description: 序列中出现次数最多的元素
from collections import Counter, defaultdict


def counter_test():
    word_counts = Counter(words)
    # 出现频率最高的三个单词
    print(word_counts.most_common(3))
    # 元素出现的次数
    print(word_counts['eyes'])


def self_test():
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1
    print(word_counts)


def run():
    counter_test()
    self_test()


if __name__ == '__main__':
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    run()
