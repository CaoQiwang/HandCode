# 删除链表中的重复元素2
# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
import sys

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    dummy_head = ListNode(0, head)
    pre = dummy_head
    cur = head
    while cur:
        if cur.next and cur.next.val == cur.val:
            dup_val = cur.val
            while cur and cur.val == dup_val:
                cur = cur.next
            pre.next = cur
        else:
            pre = pre.next
            cur = cur.next
    return dummy_head.next


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

print(to_list(deleteDuplicates(build([1, 1, 1, 2, 3]))))
nums = list(map(int, sys.stdin.readline().strip().split()))
head = build(nums)
head = deleteDuplicates(head)

print(to_list(head))
