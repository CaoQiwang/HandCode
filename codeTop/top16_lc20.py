# 有效的括号
import sys


def is_valid(s):
    n = len(s)
    if n % 2 == 1:
        return False
    stack = []
    char_map = {"(": 1, "[": 2, "{": 3, ")": 4, "]": 5, "}": 6}
    for i in range(n):
        if char_map[s[i]] <= 3:
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            bracket = stack.pop()
            if char_map[s[i]] - char_map[bracket] != 3:
                return False
        
    if len(stack)!= 0:
        return False
    return True

s = sys.stdin.readline().strip()
print(is_valid(s))