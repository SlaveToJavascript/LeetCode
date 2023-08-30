# https://leetcode.com/problems/maximal-square/
# MEDIUM
# Tags: dplc, 2ddplc, matrixlc, #221

# GIVEN:
    # m x n binary matrix filled with 0's and 1's

# TASK:
    # find the largest square containing only 1's and return its area

# EXAMPLES:
    # Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    # Output: 4

    # Input: matrix = [["0","1"],["1","0"]]
    # Output: 1

    # Input: matrix = [["0"]]
    # Output: 0

###########################################################################################################

# ✅ ALGORITHM 1: 2D DYNAMIC PROGRAMMING (ITERATIVE, BOTTOM UP)
# MAIN IDEA: use 2D dp matrix where dp[i][j] = length of largest valid square that can be formed that has matrix[i][j] as the topleft cell of the square
    # fill up dp from bottomright to topleft, where the value of each cell dp[i][j] = matrix[i][j] + the minimum of dp[i][j]'s right, bottom and diagonally bottomright cell
# Create 2D dp matrix of (m+1) * (n+1)
    # we create an extra last row and last column of 0's (borders) so that the last row and col can use this extra border to be filled up
# iterate and fill up dp from bottomright to topleft, where the value of each cell dp[i][j] = matrix[i][j] + the minimum of dp[i][j]'s right, bottom and diagonally bottomright cell
# after each dp[i][j] is updated, update the maximum length of valid square
# return the maximum length of valid square

# TIME COMPLEXITY: O(m*n)
    # iterate through all cells of matrix
# SPACE COMPLEXITY: O(m*n)
    # 2D dp array

def maximalSquare(matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_len = 0 # return value
    dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)] # dp[i][j] = length of largest valid square that can be formed with matrix[i][j] as the topleft cell
        # remember to initiate dp with 1 extra row and col
    
    for r in range(rows-1, -1, -1): # iterate dp array from bottomright to topleft
        for c in range(cols-1, -1, -1):
            dp[r][c] = int(matrix[r][c]) # dp[r][c] copies over the value at matrix[r][c] (0 or 1)
            if dp[r][c]: # if dp[r][c] is not 0,
                dp[r][c] += min(dp[r][c+1], dp[r+1][c+1], dp[r+1][c]) # the minimum of dp[r][c]'s right, bottom and diagonally bottomright cell
            
            max_len = max(max_len, dp[r][c]) # everytime after a dp cell is updated, update max length
    
    return max_len ** 2 # return max area of valid square

#==========================================================================================================

# ✅ ALGORITHM 2: 2D DYNAMIC PROGRAMMING (RECURSIVE, TOP DOWN)
# Use a hashmap cache to store the indexes (i,j) and length of largest valid square that can be formed that has matrix[r][c] as the topleft cell of the square
    # e.g. cache = {
    #               (i,j): 3,
    #               (i2,j2): 4,
    # }
# Create a recursive helper function that takes in the row and col index of the current cell (r,c), and returns the length of largest valid square that can be formed that has matrix[r][c] as the topleft cell of the square

# TIME COMPLEXITY: O(m*n)
    # visiting each cell of matrix once
# SPACE COMPLEXITY: O(m*n)
    # 2D dp array

def maximalSquare(matrix):
    rows, cols = len(matrix), len(matrix[0])
    cache = {} # map each (r,c) -> max length of valid square with (r,c) as topleft cell

    def maxSquareLen(r,c):
        if r >= rows or c >= cols:
            return 0
        
        if (r,c) not in cache:
            # get the max square lengths of bottom cell, right cell and diagonal bottomright cell
            down = maxSquareLen(r+1, c)
            right = maxSquareLen(r, c+1)
            diagonal = maxSquareLen(r+1, c+1) # diagonal bottomright

            cache[(r,c)] = int(matrix[r][c]) # add to cache and initialize key to matrix[r][c]
            if matrix[r][c] == "1":
                cache[(r,c)] += min(down, right, diagonal)
        
        return cache[(r,c)]
    
    maxSquareLen(0, 0) # start from cell at the 1st row 1st col, fill up cache
    return max(cache.values()) ** 2 # return max area of valid square