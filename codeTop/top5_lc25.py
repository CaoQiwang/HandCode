# k个一组反转链表
import sys


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head, k):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while head:
        tail = prev
        for _ in range(k):
            tail = tail.next
            if tail == None:
                return dummy.next
    
        next_start = tail.next
        head, tail = reverse(head, tail)
        prev.next = head
        tail.next = next_start
        prev = tail
        head = next_start
    return dummy.next

def reverse(head, tail):
    prev = None
    cur = head
    while prev != tail:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return tail, head

def build_list(nums):
    dummy = ListNode(-1)
    cur = dummy
    for num in nums:
        node = ListNode(num)
        cur.next = node
        cur = cur.next
    return dummy.next

def print_list(head):
    result = []
    cur = head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result

nums = list(map(int, sys.stdin.readline().strip().split()))
k = int(sys.stdin.readline().strip())
head = build_list(nums)
head = reverseKGroup(head, k)
print(print_list(head))



