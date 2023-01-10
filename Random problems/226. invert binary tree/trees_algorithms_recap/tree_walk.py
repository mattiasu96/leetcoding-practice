class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree_walk(self, root: TreeNode):
        if root is not None:
            self.tree_walk(root.left)
            print(root.val)
            self.tree_walk(root.right)


solution = Solution()

solution.tree_walk(TreeNode(10, TreeNode(5, TreeNode(20), TreeNode(20)), TreeNode(6)))
