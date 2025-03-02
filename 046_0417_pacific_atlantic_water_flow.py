from typing import List

# assisted by chatgpt, need revisit

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(x, y, visited, prev):
            if (x, y) in visited or x < 0 or y < 0 or x >= m or y >= n or heights[x][y] < prev:
                return

            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                dfs(nx, ny, visited, heights[x][y])


        pacific = set()
        atlantic = set()

        for row in range(m):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, n - 1, atlantic, heights[row][n-1])

        for col in range(n):
            dfs(0, col, pacific, heights[0][col])
            dfs(m - 1, col, atlantic, heights[m - 1][col])

        res = []
        for row in range(m):
            for col in range(n):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
        return res