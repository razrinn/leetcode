from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            hmap_row = {}
            hmap_col = {}
            hmap_subboxes = {}
            for j in range(len(board)):
                row_cell = board[i][j]
                col_cell = board[j][i]
                box_cell = board[j//3 + 3 * (( j + (i *9)) // (3 * 9))][j % 3 + ((3 * i) % 9)]
                if row_cell != "." and row_cell in hmap_row:
                    return False
                hmap_row[row_cell] = True
                if col_cell != "." and col_cell in hmap_col:
                    return False
                hmap_col[col_cell] = True
                if box_cell != "." and box_cell in hmap_subboxes:
                    return False
                hmap_subboxes[box_cell] = True
        return True