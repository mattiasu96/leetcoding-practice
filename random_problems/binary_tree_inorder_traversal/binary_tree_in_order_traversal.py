from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        elements = []

        if not root:
            return []

        if root:
            elements = self.inorderTraversal(root.left)
            elements.append(root.val)
            elements_2 = self.inorderTraversal(root.right)
            elements = elements + elements_2

        return elements
