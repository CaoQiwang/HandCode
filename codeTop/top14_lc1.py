import sys

def two_sum(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        x = target - nums[i]
        if x in hash_map:
            return[i, hash_map[x]]
        else:
            hash_map[nums[i]] = i
    return []


target = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
print(two_sum(nums, target))
