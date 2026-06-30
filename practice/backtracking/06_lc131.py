# 分割回文串
# 给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

def partition(s: str):
    result = []
    path = []

    def back_tracking(start_id):
        if start_id == len(s):
            result.append(path[:])
            return
        for i in range(start_id, len(s)):
            if is_huiwen(s, start_id, i):
                path.append(s[start_id:i+1])
                back_tracking(i+1)
                path.pop()
    back_tracking(0)
    return result

def is_huiwen(s, start, end):
    i = start
    j = end
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


print(partition("aab"))