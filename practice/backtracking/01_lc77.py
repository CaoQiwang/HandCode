# 组合
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 你可以按 任何顺序 返回答案。

def combine(n: int, k: int):
    result = []
    path = []
    

    def back_track(start_index, n, k):
        if len(path) == k:
            result.append(path[:])
            return 
        for i in range(start_index, n+1):
            path.append(i)
            back_track(i+1, n, k)
            path.pop()
    back_track(1, n, k)
    return result

print(combine(4, 2))