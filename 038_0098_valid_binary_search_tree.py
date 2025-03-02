from typing import Optional
# really close to answer but see solution, need revisit
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], minimum: float, maximum: float) -> bool:
            if node == None:
                return True

            if not (minimum < node.val < maximum):
                return False

            left = dfs(node.left, minimum, node.val)
            right = dfs(node.right, node.val, maximum)

            return True and left and right

        return dfs(root, float("-inf"), float("inf"))