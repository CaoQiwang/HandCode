# 岛屿数量
import sys

def numIland(grid):
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return
        grid[r][c] = 0
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)
    
    count = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                count += 1
                dfs(i, j)
    return count


data = list(map(int, sys.stdin.readline().strip().split()))
rows = data[0]
cols = data[1]
grid = []
for i in range(rows):
    row = list(map(int, sys.stdin.readline().strip().split()))
    grid.append(row)
result = numIland(grid)
print(result)
    

