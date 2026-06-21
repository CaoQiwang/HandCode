# k次取反后最大化的数组和
# 简单

def largestSumAfterKNegations(nums, k):
    nums.sort(key = lambda x: abs(x), reverse=True)
    for i in range(len(nums)):
        if nums[i] < 0 and k > 0:
            nums[i] = - nums[i]
            k -= 1
    if k % 2 == 1:
        nums[-1] = - nums[-1]
    result = 0
    for i in range(len(nums)):
        result += nums[i]
    return result

nums = [2,-3,-1,5,-4]
k = 2

print(largestSumAfterKNegations(nums, k))