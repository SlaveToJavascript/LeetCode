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

# ✅ ALGORITHM 1: DYNAMIC PROGRAMMING
# Iterate through each i in numRows
    # Create a row of length i+1
    # set 1st and last element of each row = 1
    # Iterate through each element j in row except for 1st and last elements
        # set each element = sum of previous row's (j-1)th and jth elements
    # append row to result array
# return result array

# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(1)
    # return value does not contribute to space complexity

def generate(numRows):
    result = []
    for i in range(numRows):
        row = [None] * (i + 1)
        row[0] = 1
        row[-1] = 1
        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
    return result

#==========================================================================================================

# ✅ ALGORITHM 1A: DYNAMIC PROGRAMMING (shorter and cleaner)
# same as above except, instead of skipping 1st and last elements of each row, we replace the value of jth or (j-1)th element with 0 if they do not exist in the row above (in the result array)

# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(1)
    # return value does not contribute to space complexity

def generate(numRows):
    result = [[1]]
    for i in range(1, numRows):
        ans = [1] * (i+1)
        for j in range(len(ans)):
            ans[j] = (result[i-1][j-1] if j > 0 else 0) + (result[i-1][j]if j < len(ans)-1 else 0)
        result.append(ans)
    
    return result