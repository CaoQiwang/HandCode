
# 二叉树中序遍历

class Solution:
    def inorderTraversal(self, root):
        result = []
        if root == None:
            return []
        def inorder(node):
            if node.left is not None:
                inorder(node.left)
            result.append(node.val)
            if node.right is not None:
                inorder(node.right)
        inorder(root)
        return result