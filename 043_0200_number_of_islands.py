from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        def dfs(i: int, j: int) -> None:
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)

        return count