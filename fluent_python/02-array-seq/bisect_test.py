# @Author: u14e
# @Time  : 2019/5/27 15:33
# @description:
import bisect

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]


def bisect_index(item):
    return bisect.bisect_left(HAYSTACK, item)


if __name__ == '__main__':
    r = bisect_index(4)
    print(r)

    bisect.insort_left(HAYSTACK, 9)
    print(HAYSTACK)
