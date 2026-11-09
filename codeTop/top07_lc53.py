# 最大子数组和
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组是数组中的一个连续部分。
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

def max_subarray2(nums):
    n = len(nums)
    count = 0
    result = float('-inf')
    for i in range(n):
        count += nums[i]
        result = max(result, count)
        if count < 0:
            count = 0
    return result


nums = list(map(int, sys.stdin.readline().split()))
nums2 = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))
print(max_subarray2(nums))

print(max_subarray(nums2))
print(max_subarray2(nums2))