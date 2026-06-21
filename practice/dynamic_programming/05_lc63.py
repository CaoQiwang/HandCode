# 不同路径2


def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        if obstacleGrid[i][0] == 1:
            break
        dp[i][0] = 1
    for j in range(n):
        if obstacleGrid[0][j] == 1:
            break
        dp[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

obstacleGrid1 = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid2 = [[0,1],[0,0]]
print(uniquePathsWithObstacles(obstacleGrid1))
print(uniquePathsWithObstacles(obstacleGrid2))