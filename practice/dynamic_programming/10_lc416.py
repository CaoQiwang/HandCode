# 分割等和子集
# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 能否装满sum/2的背包,价值和重量为同一个数组


def canPartition(nums) -> bool:
    total_sum = sum(nums)
    if total_sum % 2 == 1:
        return False
    target = total_sum // 2
    n = len(nums)
    # 考虑数字0到i下target容量下装的最大容量
    dp = [[0] * (target+1) for _ in range(n)]
    for j in range(nums[0], target+1):
        dp[0][j] = nums[0]
    
    for i in range(1, n):
        for j in range(1, target+1):
            if j >= nums[i]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]] + nums[i])
            else:
                dp[i][j] = dp[i-1][j]
    if dp[n-1][target] == target:
        return True
    else:
        return False
    

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))