# 目标和
# 给你一个非负整数数组 nums 和一个整数 target 。
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

# 加法总和为x ,减法总和为total-x
# x-(total-x) = target
# x = (total + target) / 2
# 用nums 装满容量为x的背包，有多少种方法


def findTargetSumWays(nums, target):
    total = sum(nums) 
    if abs(target) > total:
        return 0
    if (total + target) % 2 == 1:
        return 0
    x = (total + target) // 2
    n = len(nums)
    # dp[i][j]用0到i凑成和为j的方法数量
    dp = [[0] * (x+1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    if nums[0] <= x:
        dp[0][nums[0]] += 1   # 注意不能直接赋值1，因为nums[0]=0有两种,用与不用
    for i in range(1, n):
        for j in range(x+1):
            if j >= nums[i]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n-1][x]
    

nums = [1,1,1,1,1]
target = 3
print(findTargetSumWays(nums, target))

nums2 = [0,0,0,0,0,0,0,0,1]
target2 = 1
print(findTargetSumWays(nums2, target2))