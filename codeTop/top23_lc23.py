# 合并k个升序链表
import heapq
import sys

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    dummy = ListNode(0)
    cur = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if cur.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next


def build_link_list(nums):
    dummy = ListNode()
    cur = dummy
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def to_list(head):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

k = int(sys.stdin.readline().strip())
lists = []
for _ in range(k):
    arr = (list(map(int, sys.stdin.readline().strip().split())))
    head = build_link_list(arr)
    lists.append(head)
merged_head = mergeKLists(lists)
print(to_list(merged_head))


