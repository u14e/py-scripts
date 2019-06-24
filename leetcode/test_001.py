###############################################################################
# https://leetcode.com/problems/two-sum/
###############################################################################
def two_sum(numbers, target):
    map = {}
    for index, num in enumerate(numbers):
        rest = target - num
        if rest in map:
            return [map[rest], index]
        else:
            map[num] = index

def test_two_sum():
    numbers = [2, 7, 11, 15]
    target = 9
    assert two_sum(numbers, target) == [0, 1]
