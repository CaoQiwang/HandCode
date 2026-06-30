# 移除链表元素
# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 
# 虚拟头节点

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val):
    dummy_head = ListNode(0, next=head)
    pre = dummy_head
    cur = head
    while cur:
        if cur.val == val:
            next_node = cur.next
            pre.next = next_node
        else:
            pre = cur
        cur = cur.next
    return dummy_head.next