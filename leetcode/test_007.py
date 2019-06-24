###############################################################################
# https://leetcode.com/problems/reverse-integer/
###############################################################################
def reverse(x):
    res = 0
    while x:
        res = res * 10 + x % 10
        x = x // 10
    return res

def test_reverse():
    assert reverse(123) == 321
    # assert reverse(-123) == -321
    assert reverse(120) == 21