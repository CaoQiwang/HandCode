# 二分查找
# 边界小于等于，如果不带等号，right = mid - 1和left相等，退出了循环，但是没被检查是不是等于target
import sys

def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1



print(search([-1,0,3,5,9,12], 9))