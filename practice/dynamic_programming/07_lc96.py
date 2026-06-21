# 不同的二叉搜索树
# 二叉搜索树：左子节点比他小，右子节点比他大
# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

# 比如n=3的情况，先分为3种，头节点分别为1 2 3。
# 头节点为1，左边就是dp[0], 右边就是dp[2],
# 头节点为2，左边就是dp[1], 右边就是dp[1],
# 头节点为3，左边就是dp[2], 右边就是dp[0],

import sys


def numTrees(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            dp[i] = dp[i] + dp[j-1] * dp[i-j]
    return dp[n]

n = int(sys.stdin.readline().strip())
print(numTrees(n))