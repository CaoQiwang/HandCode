# 最长回文字串

import sys

def expand(s, left, right):
    n = len(s)
    while left >= 0 and right < n and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


def longestPalindrome(s):
    if not s:
        return ""
    max_length = 1
    for i in range(len(s)):
        len1 = expand(s, i, i)
        len2 = expand(s, i, i+1)
        cur_max = max(len1, len2)
        if cur_max > max_length:
            max_length = cur_max
            start = i - (cur_max - 1) // 2
    
    return s[start: start + max_length]


s = sys.stdin.readline().strip()
print(longestPalindrome(s))
