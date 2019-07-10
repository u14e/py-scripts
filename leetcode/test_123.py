# @Author: u14e
# @Time  : 2019/6/26 14:52
# @description: 合并2个有序数组
def merge_arr(l1, l2):
    arr = []
    while len(l1) and len(l2):
        if l1[0] < l2[0]:
            arr.append(l1.pop(0))
        else:
            arr.append(l2.pop(0))
    if len(l1):
        arr.extend(l1)
    if len(l2):
        arr.extend(l2)
    return arr

def merge_arr_1(l1, l2):
    import heapq
    l = l1 + l2
    heapq.heapify(l)
    heap = []
    for _ in range(len(l)):
        heap.append(heapq.heappop(l))
    return heap


def test_merge_arr():
    l1 = [1, 3, 5, 7, 9]
    l2 = [2, 4, 6, 7, 8, 10, 11, 12]
    arr = merge_arr(l1, l2)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 11, 12]


if __name__ == '__main__':
    test_merge_arr()