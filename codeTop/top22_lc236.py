# 二叉树最近公共祖先
import sys
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestAncestor(root, p, q):
    if not root:
        return None
    
    if root == p or root == q:
        return root
    
    left = lowestAncestor(root.left, p, q)
    right = lowestAncestor(root.right, p, q)
    if left and right:
        return root
    if left:
        return left
    if right:
        return right
    return None


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

def find_node(root, target):
    if root is None:
        return None
    if root.val == target:
        return root
    left = find_node(root.left, target)
    right = find_node(root.right, target)
    if left:
        return left
    if right:
        return right
    return None

def main():
    line1 = sys.stdin.readline().strip().split()
    nums = [int(x) if x != 'None' else None for x in line1]
    line2 = list(map(int, sys.stdin.readline().strip().split()))
    p_val, q_val = line2[0], line2[1]
    root = build_tree(nums)
    p = find_node(root, p_val)
    q = find_node(root, q_val)
    node = lowestAncestor(root, p, q)
    print(node.val)

if __name__ == "__main__":
    main()
