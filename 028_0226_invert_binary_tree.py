# watch solution, need revisit
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invert(root)

    def invert(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node == None:
            return node
        left_inverted = self.invert(node.left)
        right_inverted = self.invert(node.right)

        node.left, node.right = right_inverted, left_inverted

        return node