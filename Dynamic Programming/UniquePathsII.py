# 63. Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/description/
# MEDIUM
# Tags: dplc, 2ddplc, matrixlc, #63

# GIVEN:
    # an m x n integer array, obstacleGrid
    # There is a robot initially located at the top-left corner (i.e., obstacleGrid[0][0])
    # The robot tries to move to the bottom-right corner (i.e., obstacleGrid[m - 1][n - 1])
    # The robot can only move either down or right at any point in time
    # An obstacle and space are marked as 1 or 0 respectively in obstacleGrid
    # A path that the robot takes cannot include any square that is an obstacle

# TASK:
    # Return the number of possible unique paths that the robot can take to reach the bottom-right corner

# EXAMPLES:
    # Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    # Output: 2
    # Explanation: There is one obstacle in the middle of the 3x3 grid above.
    # There are two ways to reach the bottom-right corner:
    # 1. Right -> Right -> Down -> Down
    # 2. Down -> Down -> Right -> Right

    # Input: obstacleGrid = [[0,1],[0,0]]
    # Output: 1

###########################################################################################################

# ✅ ALGORITHM 1: 2D DYNAMIC PROGRAMMING (BOTTOM UP) (not space optimized)
# Create dp matrix of (m+1) x (n+1) (the +1 for each row and col is for an additional right and bottom border of 0's)
# set dp[m-1][n-1] = 1 if it's not an obstacle, else 0 if it's an obstacle
    # dp[m-1][n-1] is the destination
# Iterate dp and fill up its cell values from bottom right to top left
    # if the cell is an obstacle, the cell value = 0
    # else, if cell is not obstacle, cell value = value of cell on the right + value of cell below
# return the value of topleft-most cell

# TIME COMPLEXITY: O(m*n)
    # for the nested for-loop
# SPACE COMPLEXITY: O(m*n)
    # for the dp matrix

def uniquePathsWithObstacles(obstacleGrid):
    rows, cols = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)] # the +1 for each row and col is for an additional column on the right and row at the bottom for 0's
    dp[rows-1][cols-1] = 1 if obstacleGrid[rows-1][cols-1] == 0 else 0 # this is the destination cell; if it's an obstacle, set its value to 0; otherwise, set its value to 1

    for r in range(rows-1, -1, -1):
        for c in range(cols-1, -1, -1):
            if r == rows-1 and c == cols-1: 
                continue # this is the destination cell; we already set the value for this cell
            if obstacleGrid[r][c] != 1: # if current cell is not an obstacle,
                dp[r][c] = dp[r][c+1] + dp[r+1][c] # set its value = cell on the right + cell below
    
    return dp[0][0]

#==========================================================================================================

# ✅✅ ALGORITHM 2: 2D DYNAMIC PROGRAMMING (BOTTOM UP) (space optimized)
# When filling up the values for each cell, since we only need the values of the cells below and to its right, we only need a 1D dp array to track the values below, and keep updating this dp array for every row/col
# Every time we find the value of a cell, we update the dp value at that column with this updated value

# TIME COMPLEXITY: O(m*n)
    # for the nested for-loop
# SPACE COMPLEXITY: O(n)
    # for the 1D dp array

def uniquePathsWithObstacles(obstacleGrid):
    rows, cols = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * cols
    dp[cols-1] = 1 # this is the destination cell

    for r in range(rows-1, -1, -1):
        for c in range(cols-1, -1, -1):
            if obstacleGrid[r][c] == 1: # if this cell is an obstacle,
                dp[c] = 0 # update this cell's value to 0
            elif c < cols-1: # if this cell is not obstacle and is not the last column,
                dp[c] = dp[c] + dp[c+1] # value of cell = itself + right cell
            # else: # if c is last col,
            #     dp[c] = dp[c] + 0 # we don't need this line as it does nothing
    return dp[0]

#==========================================================================================================

# ✅ ALGORITHM 3: RECURSIVE + CACHING
# Create dp hashmap where key = (row, col) of obstacleGrid and value = no. of paths from source (at 0,0) to current cell
    # this dp caches results so we don't repeat some of the work
# For each cell, the no. of paths from source to current cell = value in cell above + value in cell on the left
# If current cell is an obstacle, set its value to 0
# Return the value of the cell at the last row, last col

# TIME COMPLEXITY: O(m*n)
    # for the nested for-loop
# SPACE COMPLEXITY: O(m*n)
    # for the dp hashmap

def uniquePathsWithObstacles(obstacleGrid):
    rows, cols = len(obstacleGrid), len(obstacleGrid[0])
    dp = {} # key = coords of cell (r,c); value = no. of paths from source at (0,0) to cell (r,c)
    dp[(0,0)] = 1 # there is 1 path from source to source itself

    # dfs(r,c) function returns the no. of paths from source to (r,c)
    def dfs(r,c):
        # base cases:
        if r < 0 or c < 0: 
            return 0 # if (r,c) is out of bounds
        if (r,c) in dp: 
            return dp[(r,c)] # if value of dfs(r,c) is already cached
        if obstacleGrid[r][c] == 1: 
            return 0 # if (r,c) is an obstacle, there are no paths from source to (r,c)

        dp[(r,c)] = dfs(r-1,c) + dfs(r,c-1) # no. of paths from source to (r,c) = no. of paths from source to cell above + no. of paths from source to cell on the left
            # cache this value in dp hashmap
        return dp[(r,c)]
    
    return dfs(rows-1, cols-1) # return no. of paths from source to destination (rows-1,cols-1)