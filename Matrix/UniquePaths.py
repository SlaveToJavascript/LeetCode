# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/description
# MEDIUM
# Tags: dplc, 2ddplc, #62

# There is a robot on an m x n grid
# The robot is initially located at the top-left corner (i.e., grid[0][0])
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1])
# The robot can only move either down or right at any point in time

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner

# EXAMPLES:
# Input: m = 3, n = 7
# Output: 28

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

###########################################################################################################

# ✅ ALGORITHM 1: 2D DYNAMIC PROGRAMMING (BOTTOM UP)
# Create a 2D dp grid m x n
# The no. in each cell should be the no. of ways to get from that cell to destination (bottom right corner)
    # since we can only go right or down,
        # no. of ways to get from any cell i to destination = no. of ways to get from i's right cell to destination + no. of ways to get from i's bottom cell to destination
# create a mxn dp grid and initiate all cells in the last row and last col as 1
    # reason: since we can only move down and right, there is only 1 way to get from each cell in the last row and last col to destination
    # e.g. if m = 5 and n = 3, the dp matrix should look like this:

            # 1   2   3
        # 1  [ ] [ ] [1]
        # 2  [ ] [ ] [1]
        # 3  [ ] [ ] [1]
        # 4  [ ] [ ] [1]
        # 5  [1] [1] [1]

# Iterate the dp matrix from the cell at the 2nd last row, 2nd last col to the cell at 1st row 1st col
    # set the value of each cell = value in right cell + value in bottom cell
# Return the value in the source cell, i.e. the top left cell (i.e. dp[0][0])

# TIME COMPLEXITY: O(m*n)
    # for the nested for-loop
# SPACE COMPLEXITY: O(m*n)
    # for the dp matrix

def uniquePaths(m, n):
    dp = [[1 for _ in range(n)] for _ in range(m)] # creates a 2D dp mxn matrix
        # initate all values to 1 since all values in last row and last col should be set to 1
        # then we fill up the values for the rest of the matrix
    
    # iterate dp matrix from the cell at the 2nd last row 2nd last col to the cell at the 1st row 1st col
    for r in range(m-2, -1, -1):
        for c in range(n-2, -1, -1):
            dp[r][c] = dp[r+1][c] + dp[r][c+1] # value of each cell = value in right cell + value in bottom cell
    
    return dp[0][0] # source cell; this is the value of the no. of ways to get from this cell (source) to destination

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: 2D DYNAMIC PROGRAMMING (TOP DOWN)
# Create a 2D dp grid m x n
# Initiate all values in the 1st row and all values in the 1st col to 1
    # since from any cell in the 1st row to destination and from any cell in the 1st col to destination, there will only be 1 path
    # this is because we can only move down and right
# Iterate dp matrix, starting from the cell at 2nd row 2nd col; set the value in current cell = value in the cell above it + value in the cell on its left
# return the value in the cell at the last row last col

# TIME COMPLEXITY: O(m*n)
# SPACE COMPLEXITY: O(m*n)

def uniquePaths(m, n):
    dp = [[1 for _ in range(n)] for _ in range(m)] # all cells initialized to 1
    dp[0][0] = 1 # starting point of the robot

    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    
    return dp[m-1][n-1]