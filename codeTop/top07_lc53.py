# 最大子数组和
import sys


def max_subarray(nums):
    n = len(nums)
    result = nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        result = max(dp[i], result)
    return result


nums = list(map(int, sys.stdin.readline().split()))
print(max_subarray(nums))