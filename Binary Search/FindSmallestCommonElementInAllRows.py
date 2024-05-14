# 1198. Find Smallest Common Element in All Rows
# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/
# MEDIUM
# Tags: hashmaplc, binarysearchlc, premiumlc, #1198

# GIVEN:
    # an m x n matrix, mat, where every row is sorted in strictly increasing order

# TASK:
    # return the smallest common element in all rows
    # If there is no common element, return -1

# EXAMPLES:
    # Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
    # Output: 5

    # Input: mat = [[1,2,3],[2,3,4],[2,3,5]]
    # Output: 2

###########################################################################################################

# ✅ ALGORITHM 1: HASHMAP
# For each no. in matrix, use it as a key in hashmap
    # corresponding hashmap value would be a set of row #'s in which this key appears
# for each key in hashmap, if the length of the set of rows in which this key appears is equal to the length of matrix, update the min. key (smallest common element in every row) and return the min. key

# TIME COMPLEXITY: O(n * m)
    # n = no. of rows in matrix
    # m = no. of columns in matrix
# SPACE COMPLEXITY: O(n * m)
    # hashmap stores n keys, each of which has a set of m elements -> O(n * m)

from collections import defaultdict

def smallestCommonElement(mat):
    hm = defaultdict(set)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            hm[mat[i][j]].add(i)
    
    min_element = float('inf')
    for k in hm:
        if len(hm[k]) == len(mat):
            min_element = min(min_element, k)
    
    return min_element if min_element != float('inf') else -1

#==========================================================================================================

# ✅ ALGORITHM 2: BINARY SEARCH
# for each no. in the 1st row (mat[0]), use binary search to check if the no. is in all other rows
# if a no. is not found in 1 particular row, we can break out of the loop (since this no. doesn't exist in all rows)

# TIME COMPLEXITY: O(n * m * log(m))
    # n = no. of rows in matrix
    # m = no. of elements in each row
    # log(m) is due to binary search in each row
# SPACE COMPLEXITY: O(1)

import bisect

def smallestCommonElement(mat):
    for num in mat[0]: # for each num in the 1st row of matrix, search for it in the remaining rows
        is_common = True # to check if num is common across all rows 
        for row in mat[1:]: # check for num from 2nd row onwards
            idx = bisect.bisect_left(row, num)
            if idx == len(row) or row[idx] != num:
                # if idx = len(row), it means num is greater than all elements in row (i.e. it does NOT exist in row)
                # row[idx] != num : bisect_left only gives us the position where num would fit to maintain order of row, it doesn't guarantee that num is present in this position -> we need to check if num is actually in this position
                is_common = False
                break # if num is not in this row, break out of loop
    
        if is_common: # if we reached this line, it means num is common across all rows
            return num # return num (it's already the smallest num since we are iterating through the 1st row and it is sorted)

    return -1 # if we reached this line, it means no common element was found