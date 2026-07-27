# 最长有效括号
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号 子串 的长度。
# 左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如 "(()())"

# 法1:栈,存放下标
def longestValidParentheses(s: str) -> int:
    stack = [-1]
    result = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                # 不合法
                stack.append(i)
            else:
                # 合法,当前下标i，stack[-1]栈顶元素，为有效字符串开始的前一个位置
                result = max(result, i - stack[-1])

    return result


# 法2:动态规划，dp[i]为以 s[i] 结尾的最长有效括号长度
def longestValidParentheses2(s: str) -> int:
    dp = [0] * len(s)
    result = 0
    for i in range(1, len(s)):
        if s[i] == ')':
            # 只有右括号才做处理
            if s[i-1] == '(':
                # 直接与上一个抵消
                dp[i] = dp[i - 2] + 2 if i >= 2 else 2
            else:
                # 与上一个不抵消，出现"))"
                left = i - dp[i-1] - 1   # 中间有效串的前一个
                if left >= 0 and s[left] == '(':
                    dp[i] = dp[i-1] + 2
                    if left >= 1:
                        dp[i] += dp[left-1]   # 补上前面的
        result = max(result, dp[i])
    return result


print(longestValidParentheses(")()())"))
print(longestValidParentheses2(")()())"))