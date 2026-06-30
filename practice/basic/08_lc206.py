# 反转链表
# 双指针

def reverseList(head):
    cur = head
    pre = None
    while cur:
        next_node = cur.next
        cur.next = pre
        pre = cur
        cur = next_node
    return pre