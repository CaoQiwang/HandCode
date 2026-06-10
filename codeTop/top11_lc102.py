# 二叉树的层序遍历
import sys
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        cur_level = []
        for _ in range(level_size):
            node = queue.popleft()
            cur_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(cur_level)
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
        if i < n and nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)
        i += 1
        if i < n and nums[i] is not None:
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1
    return root

line = sys.stdin.readline().split()
nums = [int(x) if x != 'None' else None for x in line]
root = build_tree(nums)
result = level_order(root)
print(result)




