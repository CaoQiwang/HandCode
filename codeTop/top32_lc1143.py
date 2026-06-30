# 最长公共子序列
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

# 动态规划
# 递推公式解释：
# 当前字符不相同，说明这两个字符不能同时作为公共子序列的最后一个字符，丢掉一个，答案 = 上边和左边取最大
import sys

def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    # dp[i][j] 表示 text1[0:i] 和 text2[0:j] 的最长公共子序列长度
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                # 当前字符相同，公共子序列长度加1
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # 当前字符不相同，取两个可能情况的最大值
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

print(longestCommonSubsequence("abcde", "ace"))
text1 = sys.stdin.readline().strip()
text2 = sys.stdin.readline().strip()
print(longestCommonSubsequence(text1, text2))