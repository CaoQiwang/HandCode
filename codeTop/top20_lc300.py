# 最长递归子序列
import sys

def lengthOfLIS_dp(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)



nums = list(map(int, sys.stdin.readline().strip().split()))
print(lengthOfLIS_dp(nums))