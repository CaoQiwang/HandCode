# 环形链表

def has_cycle(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False

