# 括号生成
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 回溯
# 条件：左括号数量=n，右括号数量=n，任意前缀左括号数量大于等于右括号数量

def generateParenthesis(n: int):
    path = []
    result = []

    def dfs(left, right):
        if left == n and right == n:
            result.append(''.join(path))
            return
        if left < n:
            path.append('(')
            dfs(left+1, right)
            path.pop()
        if right < left:
            path.append(')')
            dfs(left, right+1)
            path.pop()
    
    dfs(0, 0)
    return result

print(generateParenthesis(3))