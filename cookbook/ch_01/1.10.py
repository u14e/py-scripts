# @Author: u14e
# @Time  : 2019/2/25 15:58
# @description: 序列去重


def dedupe(items):
    """
    删除序列相同元素并保持顺序 (hashable 类型)
    :param items:
    :return:
    """
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_plus(items, key=None):
    """
    删除序列相同元素并保持顺序 (不可 hashable 类型，eg. dict)
    :param items:
    :param key:
    :return:
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


def dedupe_simple():
    """简单去重(不保持顺序)"""
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    result = list(set(a))
    print(result)


def run():
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))

    b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(list(dedupe_plus(b, key=lambda d: (d['x'], d['y']))))
    print(list(dedupe_plus(b, key=lambda d: d['x'])))


if __name__ == '__main__':
    run()
    dedupe_simple()
