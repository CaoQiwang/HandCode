# 排序链表
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
# 归并排序

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyList:
    def __init__(self, head=None, length=0):
        self.length = length
        self.head = head

    def create_list(self, arr):
        dummy = ListNode(0)
        cur = dummy
        for i in range(len(arr)):
            node = ListNode(arr[i])
            cur.next = node
            cur = node
        self.length = len(arr)
        self.head = dummy.next
        return self.head

    def print_list(self):
        cur = self.head
        result = []
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergeList(left, right)
    
    def mergeList(self, head1, head2):
        dummy = ListNode(0)
        cur = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                cur = cur.next
                head1 = head1.next
            else:
                cur.next = head2
                cur = cur.next
                head2 = head2.next
        if head1:
            cur.next = head1
        elif head2:
            cur.next = head2
        return dummy.next


arr = [-1,5,3,4,0]
mylist = MyList()
head = mylist.create_list(arr)
print(mylist.print_list())
sol = Solution()
head = sol.sortList(head)
print(mylist.print_list())
