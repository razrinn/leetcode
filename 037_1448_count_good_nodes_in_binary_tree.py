from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0

        self.count = 0

        def dfs(root: TreeNode, cur_max: int) -> int:
            if root == None:
                return

            self.count += 1 if root.val >= cur_max else 0
            dfs(root.left, max(cur_max, root.val))
            dfs(root.right, max(cur_max, root.val))


        dfs(root, root.val)
        return self.count
