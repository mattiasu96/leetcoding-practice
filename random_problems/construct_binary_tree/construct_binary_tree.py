# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}

        def construct_tree(preorder, inorder):
            if not preorder or not inorder:
                return None

            root = TreeNode(preorder[0])
            mid = indices[preorder[0]]  # inorder.index(preorder[0])

            root.left = construct_tree(
                preorder=preorder[1 : mid + 1], inorder=inorder[:mid]
            )
            root.right = construct_tree(
                preorder=preorder[mid + 1 :], inorder=inorder[mid + 1 :]
            )

            return root

        return construct_tree(preorder, inorder)
