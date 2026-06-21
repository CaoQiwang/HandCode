# 分发饼干


def findContentChildren(g, s):
    g.sort()
    s.sort()
    index = len(s) - 1
    result = 0
    for i in range(len(g) - 1, -1, -1):
        if index < 0:
            break
        if s[index] >= g[i]:
            result += 1
            index -= 1
        
    return result


g = [1,2]
s = [1,2,3]
print(findContentChildren(g, s))