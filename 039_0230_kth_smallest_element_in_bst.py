from typing import Optional
# very close to answer only missing return statemenet, need revisit

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if node == None:
                return None

            left = dfs(node.left)
            if left:
                return left

            self.move_count -= 1
            if self.move_count == 0:
                return node.val

            right = dfs(node.right)
            return right

        self.move_count = k
        return dfs(root)