# 合并区间
import sys

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for l in intervals:
        if len(merged) == 0:
            merged.append(l)
            continue
        if l[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], l[1])
        else:
            merged.append(l)
    return merged

intervals1 = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[1,4],[4,5]]
print(merge(intervals1))
print(merge(intervals2))
