# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = deque([root])
        res = []
        while queue:
            tmp = []
            for i in range(len(queue)):
                pop = queue.popleft()
                tmp.append(pop.val)

                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)

            res.append(tmp)

        return res