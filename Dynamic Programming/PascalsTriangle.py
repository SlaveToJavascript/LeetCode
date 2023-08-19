# https://leetcode.com/problems/pascals-triangle/
# EASY
# Tags: dplc, #118

# GIVEN:
    # integer numRows

# TASK:
    # return the first numRows rows of Pascal's triangle
    # In Pascal's triangle, each number is the sum of the two numbers directly above it

# EXAMPLES:
    # Input: numRows = 5
    # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

    # Input: numRows = 1
    # Output: [[1]]

###########################################################################################################

# ✅ ALGORITHM: DYNAMIC PROGRAMMING

# TIME COMPLEXITY: O(n^2)

def pascals_triangle(numRows):
    result = []
    for i in range(numRows):
        row = [None] * (i + 1)
        row[0] = 1
        row[-1] = 1
        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
    return result