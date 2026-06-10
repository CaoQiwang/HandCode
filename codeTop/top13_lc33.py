# 搜索旋转排序数组
import sys

def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[left]:
            if nums[left] <= target and nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        if nums[mid] <= nums[right]:
            if nums[right] >= target and nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return -1


nums = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())
print(search(nums, target))