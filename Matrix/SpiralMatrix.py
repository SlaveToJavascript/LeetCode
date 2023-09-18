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

# ✅✅ ALGORITHM 1: FOUR BOUNDARIES – TOP, DOWN, LEFT, RIGHT (MY VERSION)
# use 4 boundaries to mark out the indexes we can traverse in each row and col

def spiralOrder(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = []

    # indicate the inclusive bounds that we can traverse to for moving left, right, top, down
    left_bound = 0
    right_bound = cols - 1
    top_bound = 0
    bottom_bound = rows - 1

    while len(result) < rows * cols:
        # LEFT -> RIGHT (move right)
        r = top_bound # we're moving across top row (from left to right)
        for c in range(left_bound, right_bound + 1): # add each col cell within left and right bounds to result
            result.append(matrix[r][c])
        top_bound += 1 # after top row is visited, we don't need to visit top row anymore -> top boundary = next row

        # TOP -> BOTTOM (move down)
        c = right_bound # we're moving across right col (from top to bottom)
        for r in range(top_bound, bottom_bound + 1): # add each row cell within top and bottom bounds to result
            result.append(matrix[r][c])
        right_bound -= 1 # after right col is visited, we don't need to visit right col anymore -> right boundary = next col to its left

        # RIGHT -> LEFT (move left)
        r = bottom_bound # we're moving across bottom row (from right to left)
        if top_bound <= bottom_bound: # after moving down previously, current left movement is potentially across the same row as the initial right movement (if there's only 1 row left in current bounds) -> we need to do this check to ensure we're not retracing the same row we just moved right across
            for c in range(right_bound, left_bound - 1, -1): # add each col cell within left and right bounds to result
                result.append(matrix[r][c])
            bottom_bound -= 1 # after bottom row is visited, we don't need to visit bottom row anymore -> bottom boundary = next row to its top

        # BOTTOM -> TOP (move up)
        c = left_bound # we're moving across left col (from bottom to top)
        if left_bound <= right_bound: # after moving left previously, the upward movement is potentially across the same column as the initial downward movement (if there's only 1 col left in current bounds) -> we need to do this check to ensure we're not retracing the same col we just moved down across
            for r in range(bottom_bound, top_bound - 1, -1): # add each row cell within top and bottom bounds to result
                result.append(matrix[r][c])
            left_bound += 1 # after left col is visited, we don't need to visit left col anymore -> left boundary = next col to its right

    return result

#==========================================================================================================

# ✅ ALGORITHM 2: FOUR BOUNDARIES (NEETCODE'S VERSION)
# use 4 boundaries to mark out the indexes we can traverse in each row and col
# Similar to above solution

# TIME COMPLEXITY: O(m*n)
    # we visit each element once
# SPACE COMPLEXITY: O(1)

def spiralOrder(matrix):
    # set our 4 boundaries
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    result = [] # return value
    
    while left < right and top < bottom:
        # LEFT -> RIGHT
        # get every element in the top row
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1 # after top row is visited, we don't need to visit top row anymore -> top boundary = next row

        # TOP -> BOTTOM
        # get every element in the right col
        for i in range(top, bottom):
            result.append(matrix[i][right-1])
        right -= 1 # after right col is visited, we don't need to visit right col anymore -> right boundary = next col to its left

        if not (left < right and top < bottom):
            break # we need this for the edge case where matrix is a single row or single column

        # RIGHT -> LEFT
        # get every element in the bottom row
        for i in range(right-1, left-1, -1): # go from r to l in reverse
            result.append(matrix[bottom-1][i])
        bottom -= 1 # after bottom row is visited, we don't need to visit top row anymore -> bottom boundary = next row to its top

        # BOTTOM -> TOP
        # get every element in left column
        for i in range(bottom-1, top-1, -1):
            result.append(matrix[i][left])
        left += 1 # after left col is visited, we don't need to visit left col anymore -> left boundary = next col
    
    return result