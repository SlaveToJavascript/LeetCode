# https://leetcode.com/problems/spiral-matrix/description/
# MEDIUM
# Tags: matrixlc, #54

# GIVEN:
    # m x n matrix

# TASK:
    # return all elements of the matrix in spiral order

# EXAMPLES:
    # Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # Output: [1,2,3,6,9,8,7,4,5]

    # Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # Output: [1,2,3,4,8,12,11,10,9,5,6,7]

###########################################################################################################

# ✅ ALGORITHM: 4 BOUNDARIES (LEFT, RIGHT, TOP, BOTTOM)
# use 4 boundaries to mark out the indexes we can traverse in each row and col

# TIME COMPLEXITY: O(m*n)
    # we visit each element once
# SPACE COMPLEXITY: O(1)

def spiralOrder(matrix):
    # set our 4 boundaries
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    result = [] # return value
    
    while left < right and top < bottom:
        # get every element in the top row
        for i in range(left, right):
            result.append(matrix[top][i])
        
        top += 1 # move down

        # get every element in the right col
        for i in range(top, bottom):
            result.append(matrix[i][right-1])
        
        right -= 1 # move to the left

        if not (left < right and top < bottom):
            break # we need this for the edge case where matrix is a single row or single column

        # get every element in the bottom row
        for i in range(right-1, left-1, -1): # go from r to l in reverse
            result.append(matrix[bottom-1][i])
        
        bottom -= 1 # move upwards

        # get every element in left column
        for i in range(bottom-1, top-1, -1):
            result.append(matrix[i][left])
        
        left += 1 # move to the right
    
    return result