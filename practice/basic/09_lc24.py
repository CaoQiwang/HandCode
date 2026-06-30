# 两两交换链表节点
# 画图


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    dummy_head = ListNode(next=head)
    cur = dummy_head

    while cur.next and cur.next.next:
        cur_node = cur.next
        next_node = cur.next.next.next
        cur.next = cur_node.next
        cur.next.next = cur_node
        cur_node.next = next_node
        cur = cur_node
    return dummy_head.next