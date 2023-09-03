# https://leetcode.com/problems/triangle/
# MEDIUM
# Tags: dplc, 2ddplc, #120

# GIVEN:
    # an integer array, triangle

# TASK:
    # return the minimum path sum from top to bottom
    # NOTE: For each step, you may move to an adjacent number of the row below
        # i.e. if you are on index i on the current row, you may move to either index i or index i + 1 on the next row

# EXAMPLES:
    # Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    # Output: 11
    # Explanation: The triangle looks like:
    #    2
    #   3 4
    #  6 5 7
    # 4 1 8 3
    # The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

    # Example 2:

    # Input: triangle = [[-10]]
    # Output: -10

###########################################################################################################

# ✅ ALGORITHM 1: 2D DYNAMIC PROGRAMMING TOP-DOWN (my solution) (not space optimized)
# for each cell in triangle, we can fill up 2 cells in the row below it
    # e.g. for each triangle[r][c], we can fill up the max path sum at triangle[r+1][c] and at triangle[r+1][c+1]
# Create a 2D dp array of the same length and width as triangle array, where each dp[i][j] = min path sum up until triangle[i][j]
    # initialize dp with all infinity values
# fill up dp[0][0] = triangle[0][0]
# iterate through all rows and cols of dp, each time filling up the values for dp[row+1][col] and dp[row+1][col+1]
    # each filled up value of dp[row+1][col] and dp[row+1][col+1] should be the minimum of its existing value vs the new value below:
        # for dp[row+1][col]: new path sum value = dp[row][col] + triangle[row+1][col]
        # for dp[row+1][col+1]: new path sum value = dp[row][col] + triangle[row+1][col+1]
# return the minimum value in the last row of dp

# TIME: O(n^2)
    # n is the number of rows in triangle
    # we iterate through all rows and cols of dp, which is n^2
# SPACE: O(n^2)
    # for dp array

def minimumTotal(triangle):
    dp = [[float('inf')] * len(arr) for arr in triangle] # initiate dp array to be same size as triangle array, filled with inifity values
    dp[0][0] = triangle[0][0] # the max path sum for the 1st row in the triangle

    for r in range(len(triangle)-1): # iterate each row in triangle excluding the last row (since for each row in triangle, we're filling up the next row in dp)
        for c in range(len(triangle[r])):
            dp[r+1][c] = min(dp[r+1][c], dp[r][c] + triangle[r+1][c])
            dp[r+1][c+1] = min(dp[r+1][c+1], dp[r][c] + triangle[r+1][c+1])
    
    return min(dp[-1]) # return the min path sum that ends in the last row

#==========================================================================================================

# ✅ ALGORITHM 2: 2D DYNAMIC PROGRAMMING BOTTOM-UP (space optimized)
# Create 1D dp array of length = len(triangle) +1
    # because each row has 1 more element than the previous row -> dp array has 1 more element than last row of triangle
# Flip the triangle upside down and iterate each row of this upside down triangle
    # for each row, iterate each col
        # for each col, dp[col] = min(dp[col], dp[col+1]) + triangle[row][col]
# return the 1st element in dp (which corresponds to the tip of the triangle)

# TIME: O(n^2)
    # n is the number of rows in triangle
    # we iterate through all rows and cols of dp, which is n^2
# SPACE: O(n)
    # for dp array

def minimumTotal(triangle):
    dp = [0] * (len(triangle)+1)

    for row in triangle[::-1]: # flip triangle upside down
        for col, n in enumerate(row):
            dp[col] = n + min(dp[col], dp[col+1])
    
    return dp[0]