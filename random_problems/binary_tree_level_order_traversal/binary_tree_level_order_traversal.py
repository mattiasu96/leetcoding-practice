from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        queue = deque()
        order_list = []
        curr = root
        level = 0
        if root:
            queue.append(root)

        while len(queue) > 0:
            level_list = []
            for i in range(len(queue)):
                curr = queue.popleft()
                print(curr.val)
                level_list.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                    
                if curr.right:
                    queue.append(curr.right)
            order_list.append(level_list)
            level = level + 1


        return order_list
        
