# 跳跃游戏2


def jump(nums):
    if len(nums) == 1:
        return 0
    
    cur_distance = 0 # 当前覆盖最远
    next_distance = 0  # 下一步覆盖最远
    result = 0

    for i in range(len(nums)):
        next_distance = max(next_distance, i + nums[i])
        if i == cur_distance:
            result += 1
            cur_distance = next_distance
            if cur_distance >= len(nums) - 1:
                break
    return result

nums1 = [2,3,1,1,4]
nums2 = [2,3,0,1,4]
print(jump(nums1), jump(nums2))