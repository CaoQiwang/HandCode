# 1和0
# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

# 请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。

# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。


def findMaxForm(strs, m, n):
    # dp[i][j]：最多有i个0和j个1的strs的最大子集的大小为
    dp = [[0] * (n+1) for _ in range(m+1)]
    for s in strs:
        zero_num = s.count('0')
        one_num = s.count('1')
        # 倒序可以保证：dp[i-zero_num][j-one_num]用的是上一轮字符串处理完之后的结果，而不是当前字符串刚更新出来的结果。
        for i in range(m, zero_num-1, -1):
            for j in range(n, one_num-1, -1):
                dp[i][j] = max(dp[i][j], dp[i-zero_num][j-one_num] + 1)
    return dp[m][n]

strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(findMaxForm(strs, m, n))