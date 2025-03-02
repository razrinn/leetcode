from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        def dfs(i: int, j: int) -> None:
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            total =  1 + dfs(i - 1, j) + dfs(i, j - 1) + dfs(i + 1, j) + dfs(i, j + 1)
            return total

        res = 0
        for row in range(m):
            for col in range(n):
                tmp = 0
                if grid[row][col] == 1:
                    tmp = dfs(row, col)

                res = max(res, tmp)

        return res