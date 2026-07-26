# 二叉树的右视图
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 层序遍历


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if i == level_size - 1:
                result.append(node.val)
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

nums = [1, 2, 3, None, 5, None, 4]
root = build_tree(nums)
print(rightSideView(root))
