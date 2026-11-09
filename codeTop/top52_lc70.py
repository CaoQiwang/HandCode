# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
import sys


def climb_stairs(n):
    if n <= 2:
        return n

    dp = [0] * n
    dp[n-1], dp[n-2] = 1, 2
    for i in range(n-3, -1, -1):
        dp[i] = dp[i+1] + dp[i+2]

    return dp[0]

print(climb_stairs(2))
n = int(sys.stdin.readline().strip())
print(climb_stairs(n))