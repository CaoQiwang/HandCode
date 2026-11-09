# 三数之和

import sys


def three_sum(nums):
    n = len(nums)
    if n < 3:
        return None
    result = []
    nums.sort()
    for i in range(n):
        if nums[i] > 0:
            break
        if i != 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            sums = nums[i] + nums[left] + nums[right]
            if sums == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif sums > 0:
                right -= 1
            else:
                left += 1
    return result



nums = list(map(int, sys.stdin.readline().split()))
print(three_sum(nums))