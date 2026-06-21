# 跳跃游戏
# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false


def canJump(nums) -> bool:
    if len(nums) == 1:
        return True
    cover = 0
    i = 0
    while i <= cover:
        cover = max(cover, i + nums[i])
        if cover >= len(nums) - 1:
            return True
        i += 1
    return False

nums1 = [2,3,1,1,4]
nums2 = [3,2,1,0,4]

print(canJump(nums1), canJump(nums2))