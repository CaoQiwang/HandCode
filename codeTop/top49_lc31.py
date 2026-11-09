# 例如，arr = [1, 2, 3] ，以下这些都可以视作 arr 的排列：[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
# 找下一个排列，在原数组上修改

# 思路提示：
# 交换前：[1, 3, 5, 4, 2]
# 交换后：[1, 4, 5, 3, 2]
# 反转后：[1, 4, 2, 3, 5]

def nextPermutation(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从右往左找到第一个 nums[i] < nums[i+1]
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # 找到，需要和后面比它大的第一个交换
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i+1, n-1
        # 反转后面的
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

nums1 = [1, 3, 5, 4, 2]
nextPermutation(nums1)
print(nums1)