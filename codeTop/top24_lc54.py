# 螺旋矩阵

import sys

def spiralOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])
    top = 0
    bottem = m - 1
    left = 0
    right = n - 1
    result = []
    while top <= bottem and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        if top <= bottem and left <= right:
            for i in range(top, bottem + 1):
                result.append(matrix[i][right])
            right -= 1
        if top <= bottem and left <= right:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottem][i])
            bottem -= 1
        if top <= bottem and left <= right:
            for i in range(bottem, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiralOrder(A))