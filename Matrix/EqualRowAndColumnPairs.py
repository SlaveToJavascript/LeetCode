# https://leetcode.com/problems/equal-row-and-column-pairs/description/
# MEDIUM

# GIVEN:
    # n x n integer matrix grid

# TASK:
    # return the number of pairs (ri, cj) such that row ri and column cj are equal
    # A row-column pair is equal if they contain the same elements in the same order

# EXAMPLES:
    # Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
    # Output: 1
    # Explanation: There is 1 equal row and column pair:
    # - (Row 2, Column 1): [2,7,7]

    # Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    # Output: 3
    # Explanation: There are 3 equal row and column pairs:
    # - (Row 0, Column 0): [3,1,2,2]
    # - (Row 2, Column 2): [2,4,2,2]
    # - (Row 3, Column 2): [2,4,2,2]

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# we traverse through every possible combination of rows and columns (row R, col C) 
# and check if all elements at the same position in R and C are equal to each other

# TIME COMPLEXITY: O(n^3) ❌
    # There are a total of O(n^2) pairs when iterating over each row R and column C
    # Traversing each element in R and C takes O(n) time

def equalPairs(grid):
    count = 0
    n = len(grid)
    
    # Check each row r against each column c.
    for r in range(n):
        for c in range(n):
            match = True
            
            # Iterate over row r and column c.
            for i in range(n):
                if grid[r][i] != grid[i][c]:
                    match = False
                    break
                    
            # If row r equals column c, increment count by 1.
            count += int(match)
                
    return count

#==========================================================================================================

# ✅ ALGORITHM 2: HASHMAP
# Store each row of grid as a hashable object (tuple) in a dictionary; value is frequency of row in grid
# Iterate each column of grid, checking if column exists in dictionary
# If it exists, increment counter by value of the key-value pair
# Return counter

# TIME COMPLEXITY: O(n^2)
    # we iterate over each row and column only once
    # converting each array into a hashable object (tuple) takes O(n) time
# SPACE COMPLEXITY: O(n^2)
    # we store each row in hashmap; worst case scenario: hashmap contains n distinct rows of length n

def equalPairs(grid):
    row_hm = {}

    # add every row in grid into dictionary
    for row in grid:
        if tuple(row) in row_hm:
            row_hm[tuple(row)] += 1
        else:
            row_hm[tuple(row)] = 1
    
    counter = 0
    
    # check every column if it is in dictionary
    for i in range(len(grid)):
        col = [row[i] for row in grid]
        if tuple(col) in row_hm:
            counter += row_hm[tuple(col)] # no. of frequencies = no. of pairs for that column
    return counter