# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
# MEDIUM
# Tags: matrixlc, #36

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    # Each row must contain the digits 1-9 without repetition.
    # Each column must contain the digits 1-9 without repetition.
    # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
    # A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    # Only the filled cells need to be validated according to the mentioned rules.

# EXAMPLES:
    # Input: board = 
    # [["5","3",".",".","7",".",".",".","."]
    # ,["6",".",".","1","9","5",".",".","."]
    # ,[".","9","8",".",".",".",".","6","."]
    # ,["8",".",".",".","6",".",".",".","3"]
    # ,["4",".",".","8",".","3",".",".","1"]
    # ,["7",".",".",".","2",".",".",".","6"]
    # ,[".","6",".",".",".",".","2","8","."]
    # ,[".",".",".","4","1","9",".",".","5"]
    # ,[".",".",".",".","8",".",".","7","9"]]
    # Output: true

    # Input: board = 
    # [["8","3",".",".","7",".",".",".","."]
    # ,["6",".",".","1","9","5",".",".","."]
    # ,[".","9","8",".",".",".",".","6","."]
    # ,["8",".",".",".","6",".",".",".","3"]
    # ,["4",".",".","8",".","3",".",".","1"]
    # ,["7",".",".",".","2",".",".",".","6"]
    # ,[".","6",".",".",".",".","2","8","."]
    # ,[".",".",".","4","1","9",".",".","5"]
    # ,[".",".",".",".","8",".",".","7","9"]]
    # Output: false
    # Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

###########################################################################################################

# ✅ ALGORITHM: BRUTE FORCE
# 1. Check each row for duplicates
# 2. Check each column for duplicates
# 3. Check each 3x3 subgrid for duplicates
    # get the (r,c) coords of the top-left cell of each 3x3 subgrid and iterate within each 3x3 subgrid to check for duplicates
# 4. If any duplicates are found, return False
# 5. Return True

# TIME COMPLEXITY: O(1)
    # since the board is always a 9x9 matrix
    # if board is NxN, then time complexity is O(N^2)
# SPACE COMPLEXITY: O(1) 
    # since we are not using any extra space

def isValidSudoku(board):
    for i in range(9):
        # check each row i
        row = [x for x in board[i] if x != "."] # filter out empty cells in row i
        if len(row) != len(set(row)): # if there are duplicates in row i
            return False
        
        # check each col i
        col = [arr[i] for arr in board if arr[i] != "."] # filter out empty cells in col i
        if len(col) != len(set(col)): # if there are duplicates in col i
            return False
        
    # check each 3x3 subgrid
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    if board[r+i][c+j] != ".":
                        subgrid.append(board[r+i][c+j])
            # OR subgrid = [board[i][j] for i in range(r, r+3) for j in range(c, c+3) if board[i][j] != "."]

            if len(subgrid) != len(set(subgrid)): # if there are duplicates in the 3x3 subgrid
                return False

    return True