# 快速排序
import sys

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = []
    right = []
    for i in range(1, len(nums)):
        if nums[i] < pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


nums = list(map(int, sys.stdin.readline().split()))
print(quick_sort(nums))