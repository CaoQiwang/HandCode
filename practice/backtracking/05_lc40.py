# 组合总和3
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用 一次 。
# candidatesa中可能有重复的数字，如candidates = [10,1,2,7,6,1,5]，但每个只能用一次

# 排序
def combinationSum(candidates, target):
    path = []
    result = []
    cur_sum = 0
    candidates.sort()
    def back_tracking(start_id, cur_sum):
        if cur_sum == target:
            result.append(path[:])
            return
        if cur_sum > target:
            return
        for i in range(start_id, len(candidates)):
            if i > start_id and candidates[i] == candidates[i-1]:
                continue
            if cur_sum + candidates[i] > target:
                break
            cur_sum += candidates[i]
            path.append(candidates[i])
            back_tracking(i+1, cur_sum)
            cur_sum -= candidates[i]
            path.pop()
    back_tracking(0, cur_sum)
    return result

print(combinationSum([10,1,2,7,6,1,5], 8))


