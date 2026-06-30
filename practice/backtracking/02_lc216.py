# 组合总和3
# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
# 只使用数字1到9
# 每个数字 最多使用一次 
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

def combinationSum3(k: int, n: int):
    result = []
    path = []
    cur_sum = 0
    def back_tracking(start_id, cur_sum):
        if len(path) == k:
            if cur_sum == n:
                result.append(path[:])
            return
        for i in range(start_id, 10):
            path.append(i)
            cur_sum += i
            back_tracking(i+1, cur_sum)
            cur_sum -= i
            path.pop()
    back_tracking(1, cur_sum)
    return result

print(combinationSum3(3, 7))
print(combinationSum3(3, 9))
