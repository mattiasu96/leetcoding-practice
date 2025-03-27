class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree_search(self, root: TreeNode, value: int):
        if root is None or root.val == value:
            return root

        if value < root.val:
            return self.tree_search(root.left, value)
        else:
            return self.tree_search(root.right, value)


solution = Solution()

print(
    solution.tree_search(
        TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(25)), 25
    )
)
