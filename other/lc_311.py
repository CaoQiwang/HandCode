# 稀疏矩阵的乘法
# A: m * k
# B: k * n
A = [
    [1, 0, 0],
    [-1, 0, 3]
]

B = [
    [7, 0, 0],
    [0, 0, 0],
    [0, 0, 1]
]

# 我面试的写法
def my_mat(A, B):
    m = len(A)
    k = len(A[0])
    n = len(B[0])
    result = []
    
    for _ in range(m):
        line = [] 
        for _ in range(n):
            line.append(0)
        result.append(line)
    # 简洁的初始化写法：
    # result = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            a = 0
            for l in range(k):
                if A[i][l] == 0 or B[l][j] == 0:
                    continue
                a += A[i][l] * B[l][j]
            result[i][j] = a
    return result

# 更好的写法
def mat(A, B):
    m = len(A)
    k = len(A[0])
    n = len(B[0])
    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for l in range(k):
            if A[i][l] == 0: continue
            for j in range(n):
                if B[l][j] == 0: continue
                result[i][j] += A[i][l] * B[l][j]
    return result

print(my_mat(A, B))
print(mat(A, B))
