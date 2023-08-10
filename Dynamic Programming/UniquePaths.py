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

# ✅ ALGORITHM: 2D DYNAMIC PROGRAMMING (BOTTOM UP)
# Create a 2D dp grid m x n
# The no. in each cell should be the no. of ways to get from that cell to destination (bottom right corner)
    # since we can only go right or down,
        # no. of ways to get from any cell i to destination = no. of ways to get from i's right cell to destination + no. of ways to get from i's bottom cell to destination
# to this dp grid, add a layer of 0's to its right and bottom borders
    # e.g. if grid is 5 x 3, the grid should look like this:

            # 1   2   3
        # 1  [ ] [ ] [ ] [0]
        # 2  [ ] [ ] [ ] [0]
        # 3  [ ] [ ] [ ] [0]
        # 4  [ ] [ ] [ ] [0]
        # 5  [ ] [ ] [ ] [0]
        #    [0] [0] [0] [0]

# Initiate the cell in the last row, last col (i.e. dp[m-1][n-1]) as 1
    # bc there is only 1 way to get from the same cell to the same cell
# Iterate through the dp grid from bottom right to top left
    # set the value of each cell = value in right cell + value in bottom cell
# Return the value in the source cell, i.e. the top left cell (i.e. dp[0][0])

# TIME COMPLEXITY: O(m*n)
    # for the nested for-loop
# SPACE COMPLEXITY: O(m*n)
    # for the dp matrix

def uniquePaths(m, n):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)] # creates a 2D dp matrix of (m+1) x (n+1)
        # the +1 is for an extra layer of 0's on the right and bottom borders so we don't go out of bounds

    dp[m-1][n-1] = 1 # set the value of the bottom-right cell to 1 as there's 1 way to get from destination to destination
    
    # iterate every cell in dp matrix starting from bottom-right cell
    for r in range(m-1, -1, -1):
        for c in range(n-1, -1, -1):
            if r == m-1 and c == n-1:
                continue # skip the destination cell since its value, 1, has already been set before the nested for-loops
            dp[r][c] = dp[r+1][c] + dp[r][c+1] # value of each cell = value in right cell + value in bottom cell
    
    return dp[0][0] # source cell; this is the value of the no. of ways to get from this cell (source) to destination