# 36. Valid Sudoku

# Determine if a 9 x 9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # # brute force
        # # rows
        # for row in board:
        #     this_row = []
        #     for item in row:
        #         if item in this_row:
        #             return False
        #         elif item != ".":
        #             this_row.append(item)

        # # cols
        # for col in range(9):
        #     this_col = []
        #     for row in range(9):
        #         if board[row][col] in this_col:
        #             return False
        #         elif board[row][col] != ".":
        #             this_col.append(board[row][col])

        # # 3x3s
        # # This is SO BAD. NEVER DO THIS.
        # this_11 = []
        # this_12 = []
        # this_13 = []
        # this_21 = []
        # this_22 = []
        # this_23 = []
        # this_31 = []
        # this_32 = []
        # this_33 = []

        # for row1 in range(3):
        #     row2 = row1 + 3
        #     row3 = row1 + 6
        #     for col1 in range(3):
        #         col2 = col1 + 3
        #         col3 = col1 + 6

        #         if board[row1][col1] in this_11:
        #             return False
        #         elif board[row1][col1] != ".":
        #             this_11.append(board[row1][col1])

        #         if board[row1][col2] in this_12:
        #             return False
        #         elif board[row1][col2] != ".":
        #             this_12.append(board[row1][col2])

        #         if board[row1][col3] in this_13:
        #             return False
        #         elif board[row1][col3] != ".":
        #             this_13.append(board[row1][col3])

        #         if board[row2][col1] in this_21:
        #             return False
        #         elif board[row2][col1] != ".":
        #             this_21.append(board[row2][col1])

        #         if board[row2][col2] in this_22:
        #             return False
        #         elif board[row2][col2] != ".":
        #             this_22.append(board[row2][col2])

        #         if board[row2][col3] in this_23:
        #             return False
        #         elif board[row2][col3] != ".":
        #             this_23.append(board[row2][col3])

        #         if board[row3][col1] in this_31:
        #             return False
        #         elif board[row3][col1] != ".":
        #             this_31.append(board[row3][col1])

        #         if board[row3][col2] in this_32:
        #             return False
        #         elif board[row3][col2] != ".":
        #             this_32.append(board[row3][col2])

        #         if board[row3][col3] in this_33:
        #             return False
        #         elif board[row3][col3] != ".":
        #             this_33.append(board[row3][col3])

        # return True

        # # ChatGPT cleaning up my crap:
        # # Check rows and columns
        # for i in range(9):
        #     row = set()
        #     column = set()
        #     for j in range(9):
        #         if board[i][j] != '.' and board[i][j] in row:
        #             return False
        #         row.add(board[i][j])

        #         if board[j][i] != '.' and board[j][i] in column:
        #             return False
        #         column.add(board[j][i])

        # # Check 3x3 boxes
        # for i in range(0, 9, 3):
        #     for j in range(0, 9, 3):
        #         box = set()
        #         for k in range(3):
        #             for l in range(3):
        #                 current_val = board[i+k][j+l]
        #                 if current_val != '.' and current_val in box:
        #                     return False
        #                 box.add(current_val)

        # return True

        # using sets and only 1 iteration over the entire matrix
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != ".":
                    res += [(i, element), (element, j),
                            (i // 3, j // 3, element)]
        return len(res) == len(set(res))
