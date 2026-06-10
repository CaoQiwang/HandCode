# 合并两个有序链表

import sys

class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    dummy = ListNode(-1)
    cur = dummy
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            cur = list1
            list1 = list1.next
        else:
            cur.next = list2
            cur = list2
            list2 = list2.next
    if list1:
        cur.next = list1
    if list2:
        cur.next = list2
    return dummy.next
        

def build_linked_list(nums):
    if not nums:
        return None
    dummy = ListNode(-1)
    cur = dummy
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

def print_linked_list(head):
    cur = head
    result = []
    while cur:
        result.append(cur.val)
        cur = cur.next
    print(result)

arr1 = sys.stdin.readline().split()
arr2 = sys.stdin.readline().split()
list1 = build_linked_list(arr1)
list2 = build_linked_list(arr2)
head = merge_two_lists(list1, list2)
print_linked_list(head)
