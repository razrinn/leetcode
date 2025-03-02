"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.clone = {}

        def dfs(node: Optional['Node']) -> Optional['Node']:
            if node == None:
                return None

            if node.val in self.clone:
                return self.clone[node.val]

            self.clone[node.val] = Node(node.val)

            tmp = []
            for n in node.neighbors:
                nr = dfs(n)
                if nr != None:
                    tmp.append(nr)

            self.clone[node.val].neighbors = tmp

            return self.clone[node.val]

        copy = dfs(node)

        return copy
