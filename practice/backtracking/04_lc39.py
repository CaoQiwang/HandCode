# 组合总和
# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，
# 找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。



def combinationSum(candidates, target):
    path = []
    result = []
    cur_sum = 0
    def back_tracking(start_id, cur_sum):
        if cur_sum == target:
            result.append(path[:])
            return
        if cur_sum > target:
            return
        for i in range(start_id, len(candidates)):
            if cur_sum + candidates[i] > target:   
                # 剪枝优化
                break
            path.append(candidates[i])
            cur_sum += candidates[i]
            back_tracking(i, cur_sum)
            cur_sum -= candidates[i]
            path.pop()
    back_tracking(0, cur_sum)
    return result



print(combinationSum([2, 3, 6, 7], 7))