# 1605. Find Valid Matrix Given Row and Column Sums
# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/
# MEDIUM
# Tags: matrixlc, greedylc, #1605

# GIVEN:
    # 2 arrays, rowSum and colSum, of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix
        # In other words, you do not know the elements of the matrix, but you do know the sums of each row and column

# TASK:
    # Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements
    # Return a 2D array representing any matrix that fulfills the requirements
        # It's guaranteed that at least one matrix that fulfills the requirements exists

# EXAMPLES:
    # Input: rowSum = [3,8], colSum = [4,7]
    # Output: [[3,0],
    #          [1,7]]
    # Explanation: 
    # 0th row: 3 + 0 = 3 == rowSum[0]
    # 1st row: 1 + 7 = 8 == rowSum[1]
    # 0th column: 3 + 1 = 4 == colSum[0]
    # 1st column: 0 + 7 = 7 == colSum[1]
    # The row and column sums match, and all matrix elements are non-negative.
    # Another possible matrix is: [[1,2],
    #                              [3,5]]

    # Input: rowSum = [5,7,10], colSum = [8,6,8]
    # Output: [[0,5,0],
    #          [6,1,0],
    #          [2,0,8]]

###########################################################################################################

# ✅ ALGORITHM 1: GREEDY (RUBIK'S CUBE STYLE)
# initiate a matrix of 0's
# replace the first row of the matrix with colSum array
    # now, all columns satisfy the criteria
    # we check the sum of the first row and compare it with rowSum[0]
    # if the sum is greater than rowSum[0], reduce the sum by reducing each element of the first row by min(element, sum - rowSum[0]) (i.e. the element becomes 0 or becomes the difference of sum(first_row) - rowSum[0]), and add the reduced amount from each element in the 1st row to the element below it
        # e.g. if the first row is [5, 3, 2] (sum = 10) and rowSum[0] is 6 (diff = 10-6=4), then the first row becomes [1, 3, 2] and the second row becomes [4, 0, 0] (i.e. the 4 is "donated" from 5)
    # now check if the 2nd row = rowSum[1]
    # if not, repeat the process for the 2nd row
    # continue until all rows satisfy the criteria

# TIME COMPLEXITY: O(m*n)
# SPACE COMPLEXITY: O(m*n)

def restoreMatrix(rowSum, colSum):
    rows, cols = len(rowSum), len(colSum)
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        if r == 0: # if current row is the 1st row,
            result[r] = colSum # replace the 1st row with colSum -> result now satisfies the column sum criteria
        
        if sum(result[r]) > rowSum[r]: # if the sum of the current row is greater than the rowSum[r]
            diff = sum(result[r]) - rowSum[r] # calculate the difference
            for c in range(cols): # for each column in current row r,
                if diff > 0:
                    min_diff = min(diff, result[r][c]) # the difference that can be reduced from the current element, which is either the element itself, or the difference (whichever is smaller)
                    result[r][c] -= min_diff
                    diff -= min_diff
                    result[r+1][c] += min_diff # "donate" the reduced amount to the element in the same column next row
    
    return result