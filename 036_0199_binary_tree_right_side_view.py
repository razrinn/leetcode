from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        queue = deque([root])
        res = []
        while queue:
            lgth = len(queue)
            for i in range(lgth):
                pop = queue.popleft()

                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)

                if i == lgth - 1:
                    res.append(pop.val)



        return res