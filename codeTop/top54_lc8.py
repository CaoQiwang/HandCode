# 字符串转换整数 (atoi)


def myAtoi(s: str) -> int:
    n = len(s)
    sign = 1
    i = 0
    result = 0
    while i < n and s[i] == " ":
        i += 1
    if i < n and s[i] == '-':
        sign = -1
        i += 1
    elif i < n and s[i] == '+':
        i += 1
    while i < n and '0' <= s[i] <= '9':
        result = 10 * result + int(s[i])
        i += 1
    result = result * sign
    if result < - 2**31:
        return - 2**31
    if result > 2**31 - 1:
        return 2**31 - 1
    return result

print(myAtoi("1337c0d3"))