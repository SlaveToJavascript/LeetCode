# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/description
# MEDIUM
# Tags: dplc, 2ddplc, matrixlc, #64

# GIVEN:
    # a m x n grid filled with non-negative numbers

# TASK:
    # find a path from top left to bottom right, which minimizes the sum of all numbers along its path
    # NOTE: You can only move either down or right at any point in time

# EXAMPLES:
    # Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
    # Output: 7
    # Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

    # Input: grid = [[1,2,3],[4,5,6]]
    # Output: 12

###########################################################################################################

# ✅ ALGORITHM 1: 2D DYNAMIC PROGRAMMING (TOP-DOWN) (my solution)
# create a 2D dp matrix where dp[i][j] = the min. path sum from source (grid[0][0]) to grid[i][j]
# to get the min. path sum from source to grid[i][j], get the minimum between the numbers on the top of dp[i][j] and to the left of dp[i][j], then add grid[i][j] to that number
    # since we can only move downward and rightward, those are the only 2 immediate neighbors from which we can get to grid[i][j]
# fill up dp's 1st row and 1st col first, since those are cells without either a left cell or a top cell to compare against each other
# start filling up from dp[1][1] until the rest of the matrix

# TIME COMPLEXITY: O(m*n)
# SPACE COMPLEXITY: O(m*n)

def minPathSum(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    dp[0][0] = grid[0][0]
    
    # fill up 1st row of dp
    for c in range(1, cols):
        dp[0][c] = grid[0][c] + dp[0][c-1]
    
    # fill up 1st col of dp
    for r in range(1, rows):
        dp[r][0] = grid[r][0] + dp[r-1][0]
    
    # fill up rest of dp
    for r in range(1, rows):
        for c in range(1, cols):
            dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]
    print(dp)
    
    return dp[rows-1][cols-1]

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: 2D DYNAMIC PROGRAMMING (TOP-DOWN) (without pre-filling top row and left col)
# same as above, except instead of pre-filling values in the top row and left col, we add an additional top row and left col (borders) of inf values so that to fill up cells in the 1st row and 1st col, we can compare the values from these borders to get a minimum
    # NOTE: because of the extra row and col added to dp, dp[i][j] would correspond to grid[i-1][j-1] instead of grid[i][j]
# return the number at the last row last col of dp

# TIME COMPLEXITY: O(m*n)
# SPACE COMPLEXITY: O(m*n)

def minPathSum(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[float('inf') for _ in range(cols+1)] for _ in range(rows+1)] # create a (m+1) * (n+1) matrix, because we need an extra top row and left column so that cells in the 1st row and 1st col can compare the values on their top and left cells, and get the min value of the comparison
        # because of this extra top row and left column, grid[i][j] corresponds to dp[i+1][j+1]
    dp[0][1] = 0 # for the 1st row 1st col, we're comparing min(inf, inf) -> so change one of the 'inf's to 0

    for r in range(1, rows+1): # we start iterating from dp[1][1] which corresponds to grid[0][0]
        for c in range(1, cols+1):
            dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r-1][c-1] # dp[r][c] = the minimum of top vs left cells + grid[r-1][c-1] (since there's an extra top+left border, dp[i][j] corresponds to grid[i-1][j-1])

    return dp[rows][cols] # return the cell at the last row last col of dp