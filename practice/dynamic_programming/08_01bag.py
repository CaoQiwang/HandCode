# 01背包问题
# 有n件物品和一个最多能背重量为w 的背包。
# 第i件物品的重量是weight[i]，得到的价值是value[i]。每件物品只能用一次
# 求解将哪些物品装入背包里物品价值总和最大。

# 暴力求解时间复杂度O(2^n)

# 动态规划
# n * w, dp[i][j]只有前i个物品在容量为j时的最大价值
# dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight[i]] + value[i])


weight = [1, 3, 4]
value = [15, 20, 30]
w = 4

def max_value(weight, value, w):
    n = len(weight)
    
    dp = [[0] * (w + 1) for _ in range(n)]
    for j in range(weight[0], w+1):
        dp[0][j] = value[0]
    for i in range(1, n):
        for j in range(1, w + 1):
            if j - weight[i] >= 0:
                # 够放物品i，对比相同存量下放i-1的价值 与 放了i再看j-weight[i]的容量放i-1最大价值
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
            else:
                # 不够放物品i,继承只放i-1的价值
                dp[i][j] = dp[i-1][j]   
    return dp[n-1][w]

print(max_value(weight, value, w))

weight2 = [1, 2, 3]
value2 = [6, 10, 12]
w2 = 5
print(max_value(weight2, value2, w2))



