from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val=val, left=None, right=None)

        if root.val > val:
            root.left = self.insertIntoBST(root=root.left, val=val)
        else:
            root.right = self.insertIntoBST(root=root.right, val=val)

        return root
