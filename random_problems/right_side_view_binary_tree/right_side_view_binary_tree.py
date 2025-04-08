from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        queue = []
        curr = root
        result_list = []
        if not root:
            return []

        queue.append(curr)

        while len(queue) > 0:
            level_sublist = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                level_sublist.append(curr.val)

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            result_list.append(level_sublist[-1])

        return result_list
