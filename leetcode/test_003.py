###############################################################################
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
###############################################################################
from collections import defaultdict

def longest_sub_str(string):
    """滑动窗口法"""
    count_map = defaultdict(int)
    ans, start, end = 0, 0, 0
    for c in string:
        end += 1
        count_map[c] = count_map[c] + 1
        while count_map[c] > 1:
            count_map[string[start]] -= 1
            start += 1
        ans = max(ans, end - start)
    return ans



def test_longest_sub_str():
    assert longest_sub_str('abcabcbb') == 3
    assert longest_sub_str('bbbbb') == 1
    assert longest_sub_str('pwwkew') == 3