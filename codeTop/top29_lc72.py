# 编辑距离
# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符

import sys

def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    # dp[i][j]为将word1的前i个字符变为word2的前j个字符的最少操作数
    dp = [[0] * (n+1) for _ in range(m+1)]
    for j in range(n+1):
        dp[0][j] = j
    for i in range(m+1):
        dp[i][0] = i
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                # 如果相同，相当于就是二者前面所有字符的最小操作数
                dp[i][j] = dp[i-1][j-1]
            else:
                # 如果不同，取插入、删除、替换操作的最小值，并加1表示一次操作
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
    return dp[m][n]


print(minDistance("intention", "execution"))

word1 = sys.stdin.readline().strip()
word2 = sys.stdin.readline().strip()
print(minDistance(word1, word2))