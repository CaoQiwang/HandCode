# 二叉树的锯齿状遍历
from collections import deque
import sys

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    do_reverse = False
    while queue:
        size = len(queue)
        level = []
        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if do_reverse:
            level.reverse()
        do_reverse = not do_reverse
        
        result.append(level)
    return result


def build_tree(nums):
    n = len(nums)
    if n == 0:
        return None
    root = TreeNode(nums[0])
    queue = deque([root])
    i = 1
    while queue and i < n:
        node = queue.popleft()
        if i < n and nums[i] != None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)
        i += 1
        if i < n and nums[i] != None:
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1
    return root


line = sys.stdin.readline().strip().split()
nums = [int(x) if x != 'None' else None for x in line]
root = build_tree(nums)
result = zigzagLevelOrder(root)
print(result)
