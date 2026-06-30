# 长度最小的子数组
# 滑动窗口

def minSubArrayLen(target, nums):
    left = 0
    right = 0
    result = len(nums) + 1
    cur_sum = 0
    while right < len(nums):
        cur_sum += nums[right]
        while cur_sum >= target and left <= right:
            cur_sum -= nums[left]
            result = min(result, right - left + 1)
            left += 1
            
        right += 1
    
    return result if result <= len(nums) else 0