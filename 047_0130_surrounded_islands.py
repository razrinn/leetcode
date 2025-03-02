# i ask for chatgpt assistance, need revisit

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m, n = len(board), len(board[0])

        def dfs(x: int, y: int, not_islands):
            if x < 0 or y < 0 or x >= m or y >= n or board[x][y] == "X":
                return

            if (x, y) in not_islands:
                return

            if board[x][y] == "O" and (x == 0 or y == 0 or x == m - 1 or y == n - 1):
                not_islands.add((x, y))

            if board[x][y] == "O" :
                not_islands.add((x, y))

            dfs(x + 1, y, not_islands)
            dfs(x - 1, y, not_islands)
            dfs(x, y + 1, not_islands)
            dfs(x, y - 1, not_islands)

        non_islands = set()

        for row in range(m):
                dfs(row, 0, non_islands)
                dfs(row, n - 1, non_islands)

        for col in range(n):
            dfs(0, col, non_islands)
            dfs(m - 1, col, non_islands)

        for row in range(m):
            for col in range(n):
                if (row, col) not in non_islands:
                    board[row][col] = "X"