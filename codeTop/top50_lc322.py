# 零钱兑换
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount，表示总金额。
# 计算并返回可以凑成总金额所需的 最少 的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1 。
# 你可以认为每种硬币的数量是无限的。

# coins = [1, 2, 5], amount = 11,输出3

def coin_change(coins, amount):
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i-coin] + 1)
    if dp[amount] == float('inf'):
        return -1
    return dp[amount]


print(coin_change([1,2,5], 11))
print(coin_change([2], 3))