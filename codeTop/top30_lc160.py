# 相交链表

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def getIntersectionNode(headA, headB):
    indexA = headA
    indexB = headB
    while indexA != indexB:
        if indexA:
            indexA = indexA.next
        else:
            indexA = headB
        if indexB:
            indexB = indexB.next
        else:
            indexB = headA
    return indexA