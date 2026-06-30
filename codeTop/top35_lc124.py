# 二叉树中的最大路径和
# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
# 路径和 是路径中各节点值的总和。
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

# DFS函数
def dfs(node):
    global ans
    if not node:
        return 0

    left = max(0, dfs(node.left))
    right = max(0, dfs(node.right))

    # 以当前节点为拐点的最大路径
    ans = max(ans, node.val + left + right)

    # 返回给父节点：只能选一边
    return node.val + max(left, right)


def build_example():
    # 例子：[-10,9,20,null,null,15,7]
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

root = build_example()
ans = float('-inf')
dfs(root)
print(ans)