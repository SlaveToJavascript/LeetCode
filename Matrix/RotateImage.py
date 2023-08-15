# https://leetcode.com/problems/rotate-image/description/
# MEDIUM
# Tags: matrixlc, #48

# GIVEN:
    # an n x n 2D matrix representing an image

# TASK:
    # rotate the image by 90 degrees (clockwise)
    # NOTE: You have to rotate the image in-place, which means you have to modify the input 2D matrix directly

# EXAMPLES:
    # Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # Output: [[7,4,1],[8,5,2],[9,6,3]]

    # Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

###########################################################################################################

# ✅ ALGORITHM: REVERSE MATRIX + TRANSPOSE MATRIX
# We can achieve a 90 degree clockwise rotation simply by reversing the nested arrays in matrix, then transposing the reversed matrix
# Transposing = swapping rows to cols and cols to rows

# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(1)

def rotate(matrix):
    n = len(matrix)

    matrix[:] = matrix[::-1] # reverse order of rows in matrix

    # transpose matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]