# 删除链表的倒数第N个节点

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy_head = ListNode(0, head)
    slow = dummy_head
    fast = dummy_head
    for _ in range(n+1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
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

head = build([1, 2, 3, 4, 5])
head = removeNthFromEnd(head, 2)
print(to_list(head))