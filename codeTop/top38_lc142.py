# 环形链表2
# 数学题

class Solution:
    def detectCycle(head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                entry = head
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        return None