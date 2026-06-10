# 无重复字符最长字串
import sys


def length_of_longest_substring(s):
    if len(s) == 0:
        return 0
    result = 0
    left, right = 0, 0
    char_map = {}
    for right in range(len(s)):
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
        char_map[s[right]] = right
        result = max(result, right - left + 1)
    
    return result


if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    result = length_of_longest_substring(s)
    print(result)

