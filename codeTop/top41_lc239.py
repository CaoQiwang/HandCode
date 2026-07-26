# 滑动窗口最大值
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# 返回 滑动窗口中的最大值 。
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]

# 双端队列，存储滑动窗口中元素的下标，保持队首为最大值，从高到低排列。
# O(n)
# 对比用最大堆的方法，
# O(nlog(k))

import time

from collections import deque
import heapq


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    queue = deque()
    result = []
    for i in range(len(nums)):
        # 最大值超出滑动窗口范围要出队
        if queue and queue[0] < i - k + 1:
            queue.popleft()
        
        # 调整顺序,比当前新入队元素小的直接不要了，因为又比他新又比他大
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()
        
        # 新的进来
        queue.append(i)

        # 更新结果
        if i >= k - 1:
            result.append(nums[queue[0]])
    return result

def maxSlidingWindow2(nums, k):
    heap = []
    result = []
    for i in range(len(nums)):
        heapq.heappush(heap, (-nums[i], i))
        if i >= k - 1:
            while heap[0][1] < i - k + 1:
                heapq.heappop(heap)
            result .append(-heap[0][0])
    return result

start = time.perf_counter()
print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
time1 = time.perf_counter() - start
start = time.perf_counter()
print(maxSlidingWindow2([1,3,-1,-3,5,3,6,7], 3))
time2 = time.perf_counter() - start

print(f"双端队列运行时间：{time1:.10f} 秒")

print(f"最大堆运行时间：{time2:.10f} 秒")