# 反转链表2

import sys

class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_between(head, left, right):
    if left == right:
        return head
    dummy_head = ListNode(-1, head)
    pre = dummy_head
    for _ in range(left - 1): 
        pre = pre.next
    cur = pre.next
    for _ in range(right - left):
        next_node = cur.next
        cur.next = next_node.next
        next_node.next = pre.next
        pre.next = next_node
    return dummy_head.next

def build_list(nums):
    dummy_head = ListNode(-1)
    cur = dummy_head
    for i in range(len(nums)):
        node = ListNode(nums[i])
        cur.next = node
        cur = cur.next
    return dummy_head.next

def print_list(head):
    cur = head
    li = []
    while cur:
        li.append(cur.val)
        cur = cur.next
    return li

nums = list(map(int, sys.stdin.readline().strip().split()))
data = list(map(int, sys.stdin.readline().strip().split()))
left, right = data[0], data[1]
head = build_list(nums)
reverse_between(head, left, right)
result = print_list(head)
print(result)
