# 1380. Lucky Numbers in a Matrix
# https://leetcode.com/problems/lucky-numbers-in-a-matrix/
# EASY
# Tags: matrixlc, #1380

# GIVEN:
    # m x n matrix of distinct numbers

# TASK:
    # return all lucky numbers in the matrix in any order
        # A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column

# EXAMPLES:
    # Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
    # Output: [15]
    # Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

    # Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    # Output: [12]
    # Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

    # Input: matrix = [[7,8],[1,2]]
    # Output: [7]
    # Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

###########################################################################################################

# ✅ ALGORITHM 1: HASHSET INTERSECTION
# iterate each row, and add the minimum element to a set
# iterate each column, and add the maximum element to another set
# return the intersection of the two sets

# TIME COMPLEXITY: O(m*n)
    # the 2nd for-loop of columns is a double for-loop which takes O(m*n) time
# SPACE COMPLEXITY: O(m+n)
    # 2 sets of size m and n = O(m+n) space

def luckyNumbers (matrix):
    rows, cols = len(matrix), len(matrix[0])
    row_mins, col_maxes = set(), set()

    # add minimum element in each row to row_mins hash set
    for r in range(rows):
        row_min = min(matrix[r])
        row_mins.add(row_min)
    
    # add maximum element in each column to col_maxes hash set
    for c in range(cols):
        maxx = 0
        for r in range(rows):
            maxx = max(maxx, matrix[r][c])
        col_maxes.add(maxx)

    return list(row_mins.intersection(col_maxes))

#==========================================================================================================

# ✅ ALGORITHM 2: GREEDY (PROOF BY CONTRADICTION)
# there can only be 1 lucky number or NO lucky numbers
# because a lucky no. x is the min. in the row and max. in the column
    # this means all other no.s in the row are greater than x, and all other no.s in the column are smaller than x -> there cannot be another lucky no. in the same rol and column
    # for the remaining no.s in the matrix, in order to be a lucky no., they must be greater than the other no.s in the same row as x (since lucky no. must be max in their col), and they must be smaller than the other no.s in the same column as x (since lucky no. must be min in their row)
    # which means that any other lucky no.s need to be GREATER THAN x AND SMALLER THAN x at the same time, which is not possible! (contradiction)
    # therefore, there cannot be more than 1 lucky no. in the matrix
# ALGORITHM:
    # 1. find the minimum element in each row, and find the maximum element out of these row minimums
        # NOTE: only the maximum element out of the row minimums can be a lucky no., because for a lucky no. which is not a maximum element out of the row minimums, there must be another lucky no. which is greater than it in the same column
    # 2. at each column, find the maximum in that column and check if that column maximum = the max of row minimums
    # 3. if yes, return that column maximum as the lucky no. -> return that element in a list

# TIME COMPLEXITY: O(m*n)
    # the 2nd for-loop of columns is a double for-loop which takes O(m*n) time
# SPACE COMPLEXITY: O(1)

def luckyNumbers (matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_of_row_mins = 0 # maximum element out of the minimum values of each row

    for r in range(rows):
        row_min = min(matrix[r])
        max_of_row_mins = max(max_of_row_mins, row_min)

    for c in range(cols):
        col_max = matrix[0][c]
        for r in range(rows):
            col_max = max(col_max, matrix[r][c])
        
        if col_max == max_of_row_mins:
            return [col_max]
    
    return [] # no lucky no. found