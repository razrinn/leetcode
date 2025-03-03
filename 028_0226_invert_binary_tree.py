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

    # second run, use fn inside
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root

        def swap(node):
            if node == None:
                return

            node.left, node.right = node.right, node.left

            swap(node.left)
            swap(node.right)

        swap(cur)
        return root