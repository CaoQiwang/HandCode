# 最大子数组和
# 常考，常用动态规划
# 这里展示贪心做法


def maxSubArray(nums):
    result = float('-inf')
    count = 0
    for i in range(len(nums)):
        count += nums[i]
        result = max(result, count)
        if count < 0:
            count = 0
    return result


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))