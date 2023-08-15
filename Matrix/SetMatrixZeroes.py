# https://leetcode.com/problems/set-matrix-zeroes/
# MEDIUM
# Tags: matrixlc, #73

# GIVEN:
    # an m x n integer matrix, matrix

# TASK:
    # if an element is 0, set its entire row and column to 0's, and do it in-place

# EXAMPLES:
    # Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    # Output: [[1,0,1],[0,0,0],[1,0,1]]

    # Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

###########################################################################################################

# ✅ ALGORITHM 1: BRUTE FORCE (space complexity not optimized)
# Save all coords of 0's in the matrix into a set
# Iterate through the set and for each coord of 0, set its entire row and col to 0

# TIME COMPLEXITY: O(m*n)
# SPACE COMPLEXITY: O(m*n)
    # worst case, if all values in matrix are 0's

def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    zeros = set()

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zeros.add((r, c)) # get all coords of existing 0's in the matrix and add to set
    
    for r, c in zeros: # for each coord of 0
        # set all values in its row to 0
        for col in range(cols):
            matrix[r][col] = 0
        
        # set all values in its col to 0
        for row in range(rows):
            matrix[row][c] = 0

#==========================================================================================================

# ✅ ALGORITHM 1: MARK ROWS AND COLS TO BE ZEROED (space complexity optimized)
# Iterate through entire matrix once, and identify which rows and cols need to be zeroed
# For the rows and cols that need to be zeroed, use the first cells in these rows and cols to mark them out
# Iterate through the matrix again, and for each cell, if its row or col is marked, set it to 0

# TIME COMPLEXITY: O(m*n)
# SPACE COMPLEXITY: O(1)

def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    firstRowToBeZeroed = False # this variable is to tell us if 1st row needs to be zeroed or not

    # determine which rows and cols need to be zeroed
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0 # we set the 1st element in this column to 0

                if r > 0:
                    matrix[r][0] = 0 # we set the 1st element in this row to 0
                else:
                    firstRowToBeZeroed = True # we cannot set 1st element in this row to 0 if we are at the 1st row, because if we do, it might be mistaken for an indication that the 1st row and col must be zeroed, which is not the case
    
    # iterate entire matrix; if the 1st element of current row/col is marked 0, set current cell to 0
    # we have to skip the 1st row and 1st col as we'll change those to 0 afterwards
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0: # if the 1st value in current col is 0 or 1st value in current row is 0
                matrix[r][c] = 0
    
    # zero out the 1st row and 1st col if we need to
    if matrix[0][0] == 0:
        # remember, the 1st row of the matrix tells us which cols we can zero out
        for r in range(rows):
            matrix[r][0] = 0 # we set all values in the 1st column to 0
    
    if firstRowToBeZeroed: # if we need to zero out the 1st row,
        for c in range(cols):
            matrix[0][c] = 0 # we zero out all values in the 1st row