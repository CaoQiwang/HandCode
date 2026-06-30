# 移除元素
# 快慢指针

def removeElement(nums, val):
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow

print(removeElement([0,1,2,2,3,0,4,2], 2))