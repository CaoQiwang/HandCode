# 重排链表
# 注意断开和合并终止条件
import sys

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    # 找中点并断开
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    second = slow.next
    slow.next = None

    # 反转中点后的链表
    prev = None
    while second:
        next_node = second.next
        second.next = prev
        prev = second
        second = next_node
    # 反转后头是prev
    first, second = head, prev

    # 合并
    while second:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2


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
reorderList(head)
print(to_list(head))