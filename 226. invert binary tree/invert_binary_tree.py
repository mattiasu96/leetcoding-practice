# NB: a binary search tree has a specific structure in the node values, dont forget it
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: TreeNode):
        temp = 0

        if root is None:
            return root

        temp = root.left
        root.left = root.right
        root.right = temp
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root







solution = Solution()

print(solution.invert_tree(TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(25))))
