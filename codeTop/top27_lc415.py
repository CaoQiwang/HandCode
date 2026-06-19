# 字符串相加
import sys

def add_strings(num1, num2):
    i = len(num1) - 1
    j = len(num2) - 1
    result = []
    carry = 0
    while i >= 0 or j >= 0 or carry > 0:
        x = ord(num1[i]) - ord('0') if i >= 0 else 0
        y = ord(num2[j]) - ord('0') if j >= 0 else 0
        cur = x + y + carry
        result.append(str(cur % 10))
        carry = cur // 10
        i -= 1
        j -= 1
    result = result[::-1]
    result = "".join(result)
    return result

num1 = sys.stdin.readline().strip()
num2 = sys.stdin.readline().strip()
print(add_strings(num1, num2))