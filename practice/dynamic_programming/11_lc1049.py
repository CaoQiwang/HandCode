# 最后一块石头的重量

# 有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。
# 每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
# 最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0

# 将石头分为尽可能相同的两堆
# 01 背包，尽可能接近一半，即求一半的容量下最大重量
def lastStoneWeightII(stones):
    n = len(stones)
    total = sum(stones)
    target = total // 2
    dp = [[0] * (target+1) for _ in range(n)]
    for j in range(target+1):
        if j >= stones[0]:
            dp[0][j] = stones[0]
    for i in range(1, n):
        for j in range(1, target+1):
            if j >= stones[i]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-stones[i]] + stones[i])
            else:
                dp[i][j] = dp[i-1][j]
    return total - 2 * dp[n-1][target]

stones1 = [2,7,4,1,8,1]
stones2 = [31,26,33,21,40]

print(lastStoneWeightII(stones1))
print(lastStoneWeightII(stones2))
