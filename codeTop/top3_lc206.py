# 反转链表
import sys


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    if head == None:
        return head
    prev = None
    cur = head
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    
    return prev

def build(nums):
    dummy = ListNode()
    cur = dummy
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def to_list(head):
    ans = []
    cur = head
    while cur:
        ans.append(cur.val)
        cur = cur.next

    return ans

s = sys.stdin.readline()
nums = list(map(int, s.split()))
head = build(nums)
head = reverse_list(head)
answer = to_list(head)
print(answer)