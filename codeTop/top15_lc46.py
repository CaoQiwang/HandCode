# 全排列
import sys

def permute(nums):
    result = []
    path = []
    n = len(nums)
    used = [False] * n
    def back_track():
        if len(path) == n:
            result.append(path[:])    # 生成一个副本
            return
        for i in range(n):
            if used[i] == True:
                continue
            path.append(nums[i])
            used[i] = True
            back_track()
            used[i] = False
            path.pop()
    back_track()
    return result

        
nums = list(map(int, sys.stdin.readline().split()))
print(permute(nums))