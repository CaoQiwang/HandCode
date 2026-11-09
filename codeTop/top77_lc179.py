# 最大数

# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

# 示例
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"

from functools import cmp_to_key


def largestNumber(nums):
    # 转为字符串
    nums_str = list(map(str, nums))

    # 比较函数，返回负值即a<<<b，a排在b前
    def cmp(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0

    nums_str.sort(key=cmp_to_key(cmp))

    # 处理所有字符都为0的情况
    if nums_str[0] == '0':
        return "0"

    return "".join(nums_str)

nums = [3,30,34,5,9]
print(largestNumber(nums))