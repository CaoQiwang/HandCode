# 设计链表
# 虚拟头节点，注意边界条件

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        cur = self.dummy_head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        next_node = self.dummy_head.next
        node = ListNode(val, next_node)
        self.dummy_head.next = node
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        cur = self.dummy_head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        next_node = cur.next
        cur.next = ListNode(val, next_node)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1
