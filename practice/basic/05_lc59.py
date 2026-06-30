# 螺旋矩阵2
# 仔细

def generateMatrix(n: int):
    nums = [[0] * n for _ in range(n)]
    startx, starty = 0, 0
    count = 1
    loop = n // 2 # 迭代次数
    for l in range(1, loop+1):
        for i in range(starty, n - l):
            nums[startx][i] = count 
            count += 1
        for i in range(startx, n - l):
            nums[i][n-l] = count
            count += 1
        for i in range(n - l, startx, -1):
            nums[n-l][i] = count 
            count += 1
        for i in range(n - l, starty, -1):
            nums[i][starty] = count 
            count += 1
        startx += 1
        starty += 1
    if n % 2 == 1:
        nums[n//2][n//2] = n * n 
    return nums

print(generateMatrix(2))
print(generateMatrix(3))
print(generateMatrix(4))
print(generateMatrix(7))