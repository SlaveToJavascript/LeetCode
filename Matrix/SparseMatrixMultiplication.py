# 311. Sparse Matrix Multiplication
# https://leetcode.com/problems/sparse-matrix-multiplication/
# MEDIUM
# Tags: matrixlc, #311

# GIVEN:
    # two sparse matrices mat1 and mat2, both of size m x k and k x n respectively

# TASK:
    # multiply mat1 and mat2 together, and return the result of the multiplication

# EXAMPLES:
    # Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
    # Output: [[7,0,0],[-7,0,3]]

    # Input: mat1 = [[0]], mat2 = [[0]]
    # Output: [[0]]

###########################################################################################################

# ✅ ALGORITHM 1: TRIPLE FOR-LOOPS (BRUTE FORCE)
# NOTE: there are the same no. of elements (k) in 1 row of mat1 as there are in 1 column of mat2
# to find each element result[i][j] of resulting matrix, multiply i'th row elements of mat1 with j'th column elements of mat2 and add them
# use 1 pointer to point to each row of mat1, 1 pointer to point to each column of mat2, and 1 pointer to point to each element in the current mat1 row

# TIME COMPLEXITY: O(m*n*k)
    # m = no. of rows in mat1
    # n = no. of columns in mat2
    # k = no. of columns in mat1 and no. of rows in mat2
    # we iterate over all m*k elements of mat1
    # for each element of mat1, we iterate over all n columns of mat2
# SPACE COMPLEXITY: O(1)
    # NOTE: result array, which is to be returned, is not included in calculation of space complexity

def multiply(mat1, mat2):
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))] # resulting matrix to be returned

    for row_index, row_elements in enumerate(mat1):
        for element_index, row_element in enumerate(row_elements):
            if row_element != 0:
                for col_index, col_element in enumerate(mat2[element_index]):
                    result[row_index][col_index] += row_element * col_element
    
    return result

#==========================================================================================================

# ✅ ALGORITHM 2: 