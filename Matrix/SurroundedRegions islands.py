# https://leetcode.com/problems/surrounded-regions/description/
# MEDIUM
# Tags: graphlc, dfslc, matrixlc

# GIVEN:
    # an m x n matrix board containing 'X' and 'O'

# TASK:
    # capture all regions that are 4-directionally surrounded by 'X'
    # capture a region = flip all O's into X's in that region

# EXAMPLES:
    # Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    # Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    # Explanation:
        # [["X","X","X","X"],       [["X","X","X","X"],
        #  ["X","O","O","X"],   =>   ["X","X","X","X"],
        #  ["X","X","O","X"],        ["X","X","X","X"],
        #  ["X","O","X","X"]]        ["X","O","X","X"]]

        # Notice that an 'O' should not be flipped if:
        # - It is on the border, or
        # - It is adjacent to an 'O' that should not be flipped.
        # The bottom 'O' is on the border, so it is not flipped.
        # The other three 'O' form a surrounded region, so they are flipped.

    # Input: board = [["X"]]
    # Output: [["X"]]

###########################################################################################################

# ALGORITHM 1: DFS, CAPTURE EVERYTHING EXCEPT UNSURROUNDED REGIONS
# Instead of focusing on capturing surrounded regions, we can instead say: capture everything except unsurrounded regions
    # => our focus will not be on the unsurrounded regions instead

# Unsurrounded regions are regions that have cell(s) lying on the borders

# STEPS:
    # 1. Check all borders if there are any O's on the borders
        # these O's on borders are part of the unsurrounded regions
    # 2. For the O's on borders, change the 'O's to something else, e.g. 'U's (for unsurrounded)
    # 3. Do DFS on the O's on borders, accessing all cells that are part of that region, and change those cells' O's into U's as well
    # 4. Do a nested for loop to access each cell on the grid; change all O's into X's
        # => here, we are capturing everything except unsurrounded regions
    # 5. Go through each cell on the grid again and change all U's back into O's

# TIME COMPLEXITY: O(r*c) 
    # r = no. of rows, c = no. of cols
# SPACE COMPLEXITY: O(r*c) 

def solve(board):
    rows, cols = len(board), len(board[0])

    def dfs(board, r, c): # capture unsurrounded regions
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if board[r][c] != "O":
            return
        
        board[r][c] = "U" # mark the unsurrounded regions
        
        # do dfs to mark all connected cells as 'U'
        dfs(board, r-1, c)
        dfs(board, r+1, c)
        dfs(board, r, c-1)
        dfs(board, r, c+1)
    
    # 1. Capture unsurrounded regions on border (O -> U)
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O" and (r in [0, rows-1] or c in [0, cols-1]):
                dfs(board, r, c)
    
    # 2. Capture everything except unsurrounded regions (O -> X)
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"

    # 3. Convert all U's into O's (U -> O)
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "U":
                board[r][c] = "O"