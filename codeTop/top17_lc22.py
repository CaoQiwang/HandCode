# 合并两个有序数组
import sys

def merge(nums1, nums2, m, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    while p2 >= 0 :
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


data = list(map(int, sys.stdin.readline().strip().split()))
m, n = data[0], data[1]
nums1 = list(map(int, sys.stdin.readline().strip().split()))
nums2 = list(map(int, sys.stdin.readline().strip().split()))
merge(nums1, nums2, m, n)
print(nums1)
