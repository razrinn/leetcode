from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)
        rows = {}
        cols = {}
        boxes = {}

        for i in range(size):
            for j in range(size):
                row_cell = board[i][j]
                if row_cell != ".":
                    if i not in rows:
                        rows[i] = {row_cell: True}
                    else:
                        if row_cell in rows[i]:
                            return False
                        else:
                            rows[i][row_cell] = True

                col_cell = board[j][i]
                if col_cell != ".":
                    if i not in cols:
                        cols[i] = {col_cell: True}
                    else:
                        if col_cell in cols[i]:
                            return False
                        else:
                            cols[i][col_cell] = True

                x = j // 3 + ((i % 3) * 3)
                y = j % 3 + ((i // 3) * 3)
                box_cell = board[x][y]
                if box_cell != ".":
                    if i not in boxes:
                        boxes[i] = {box_cell: True}
                    else:
                        if box_cell in boxes[i]:
                            return False
                        else:
                            boxes[i][box_cell] = True
        return True


# TOPICS: array, hashtable, matrix
# DIFFICULTY: medium
# NOTES: faster to determine index x,y of a matrix
