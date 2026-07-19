# 寻找两个正序数组的中位数
# 二分法难题
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
# 算法的时间复杂度应该为 O(log (m+n))
# 直接遍历的复杂度是O(m+n)

def findMedianSortedArrays(nums1, nums2):
    # 要在短数组上二分，j = left_size - i不会超出范围
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    left_size = (m + n + 1) // 2   
    # 奇数长度左边多一个，所以最后最大值是左边的最大max(nums1_left, nums2_left)
    low, high = 0, m
    while low <= high:
        i = (low + high) // 2
        j = left_size - i
        # 注意处理边界防止越界
        nums1_left = float('-inf') if i == 0 else nums1[i-1]
        nums1_right = float('inf') if i == m else nums1[i]
        nums2_left = float('-inf') if j == 0 else nums2[j-1]
        nums2_right = float('inf') if j == n else nums2[j]
        if nums1_left <= nums2_right and nums2_left<=nums1_right:
            if (m+n) % 2 == 1:
                return max(nums1_left, nums2_left)
            else:
                left_max = max(nums1_left, nums2_left)
                right_min = min(nums1_right, nums2_right)
                return (left_max + right_min) / 2
        elif nums1_left > nums2_right:
            # 表1左边大了
            high = i - 1
        else:
            # 表1左边小了
            low = i + 1

print(findMedianSortedArrays([1, 3], [2]))
print(findMedianSortedArrays([1, 2], [3, 4]))