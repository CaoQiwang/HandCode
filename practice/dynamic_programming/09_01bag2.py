# 01背包问题
# 有n件物品和一个最多能背重量为w 的背包。
# 第i件物品的重量是weight[i]，得到的价值是value[i]。每件物品只能用一次
# 求解将哪些物品装入背包里物品价值总和最大。

# 动态规划方法2，用一维dp数组
# dp[j]：容量为j的背包，所背的物品价值可以最大为dp[j]
# 去掉二维数组中的i的维度
# dp[j] = max(dp[j], dp[j-weight[i]] + value[i])

weight = [1, 3, 4]
value = [15, 20, 30]
w = 4

def max_value(weight, value, w):
    n = len(weight)
    dp = [0] * (w + 1)
    dp[0] = 0
    for i in range(n):   # 先遍历物品
        for j in range(w, weight[i]-1, -1):    
        # 倒序遍历容量,保证物品i只被放入一次，因为dp[j-weight[i]]还没放i，但是已经考虑了i-1等之前的物品
            dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
    return dp[w]

print(max_value(weight, value, w))
