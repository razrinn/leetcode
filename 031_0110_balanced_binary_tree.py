from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkHeight(root)[1]

    def checkHeight(self, root: Optional[TreeNode]) -> Tuple[int, bool]:
        if root == None:
            return (0, True)

        left = self.checkHeight(root.left)
        right = self.checkHeight(root.right)

        boolcheck = left[1] and right[1] and abs(right[0] - left[0]) <= 1

        return (1 + max(left[0], right[0]), boolcheck)