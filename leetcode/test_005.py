###############################################################################
# https://leetcode.com/problems/longest-palindromic-substring/
###############################################################################
def longest_palindromic_substr(s):
    m = ''
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if len(m) > j - i:
                break
            if s[i:j] == s[i:j][::-1]:
                print(i, j)
                m = s[i:j]
                break
    return m


def test_longest_palindromic_substr():
    assert longest_palindromic_substr('babad') == 'aba'
    assert longest_palindromic_substr('cbbd') == 'bb'