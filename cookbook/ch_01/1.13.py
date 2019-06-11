# @Author: u14e
# @Time  : 2019/3/2 10:47
# @description: 通过某个关键字排序一个字典列表
from operator import itemgetter
from pprint import pprint


def itemgetter_test():
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
    pprint(rows_by_fname)
    pprint(rows_by_uid)
    pprint(rows_by_lfname)


def self_test():
    rows_by_fname = sorted(rows, key=lambda r: r['fname'])
    rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
    pprint(rows_by_fname)
    pprint(rows_by_lfname)


def run():
    itemgetter_test()
    self_test()


if __name__ == '__main__':
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    run()
