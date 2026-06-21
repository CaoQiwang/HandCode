# 整数拆分
# 动态规划或贪心
# 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
# 返回 你可以获得的最大乘积 。


import sys

def integerBreak(n):
    dp = [0] * (n+1)
    dp[2] = 1
    for i in range(3, n+1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * (i - j), j * dp[i-j])
    return dp[n]


print(integerBreak(10))


n = int(sys.stdin.readline().strip())
print(integerBreak(n))


