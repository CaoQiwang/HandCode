# 有序数组的平方
# 双指针

def sortedSquares(nums):
    result = [0] * len(nums)
    left, right = 0, len(nums)-1
    for i in range(len(nums)-1, -1, -1):
        a = nums[left] * nums[left]
        b = nums[right] * nums[right]
        if a < b:
            result[i] = b
            right -= 1
        else:
            result[i] = a
            left += 1
    return result