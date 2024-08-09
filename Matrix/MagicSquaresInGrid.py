# 840. Magic Squares In Grid
# https://leetcode.com/problems/magic-squares-in-grid/
# MEDIUM
# Tags: matrixlc, #840

# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
# Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?
# Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

# EXAMPLES:
    # Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
    # Output: 1
    # Explanation: 
    # The following subgrid is a 3 x 3 magic square:
        # [[4,3,8],
        #  [9,5,1],
        #  [2,7,6]]
    # while this one is not:
        # [[3,8,4],
        #  [5,1,9],
        #  [7,6,2]]
    # In total, there is only one magic square inside the given grid.

    # Input: grid = [[8]]
    # Output: 0

###########################################################################################################

# ✅ ALGORITHM 1: BRUTE FORCE
# sum(1..9) = 45 -> each row, col, diag should have sum = 15 each
# For each 3x3 subgrid, check if it is a magic square.
    # check if grid only has 1-9, no duplicates, none out of range
    # check if sum of each row = 15
    # check if sum of each col = 15
    # check if sum of each diagonal = 15

# TIME COMPLEXITY: O(n*m)
    # n = rows
    # m = cols
# SPACE COMPLEXITY: O(1)

def numMagicSquaresInside(grid):
    rows, cols = len(grid), len(grid[0])
    
    def is_magic_square(r,c): # (r,c) stands for the coords of the topleft most cell
        # ensure 1-9 in grid (no duplicates, none out of range)
        values = set()
        for i in range(r, r+3):
            for j in range(c, c+3):
                if grid[i][j] in values or not (1 <= grid[i][j] <= 9):
                    return False
                values.add(grid[i][j])
        
        # check if sum(rows) = 15
        for i in range(r, r+3):
            if sum(grid[i][c:c+3]) != 15:
                return False
            
        # check if sum(cols) = 15
        for j in range(c, c+3):
            if grid[r][j] + grid[r+1][j] + grid[r+2][j] != 15:
                return False
        
        # check if each diagonal sum = 15
        if (
            grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or 
            grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15
        ):
            return False
        
        return True

    result = 0
    for r in range(rows-2):
        for c in range(cols-2):
            result += int(is_magic_square(r,c))
    
    return result

#==========================================================================================================

# NOTE: do not use the below algorithm unless interviewer asks for a 2nd way of solving it! It's too complicated to derive during an interview

# ✅ ALGORITHM 2: MATH
# ! MAIN IDEA: we know that the number in the middle cell can only be 5, and we deduce the positions of the rest of the numbers by their frequencies in the equations
    # WHY IS THE MIDDLE CELL 5?
        # if we choose to start with 1 + x + y = 15, then x + y = 14
        # if x is 9, then y is 5
        # if x is 8, then y is 6
        # if x is 7, then y is 7 (invalid since there shouldn't be duplicates)
        # -> we have:
            # 1 + 5 + 9 = 15
            # 1 + 6 + 8 = 15
        # following the same logic, we also have:
            # 2 + 4 + 9 = 15
            # 2 + 5 + 8 = 15
            # 2 + 6 + 7 = 15
            # 3 + 4 + 8 = 15
            # 3 + 5 + 7 = 15
            # 4 + 5 + 6 = 15
    # we can see that only 5 has appeared in the above equations 4 times, so 5 should be the middle cell
        # we need the sums of middle column, middle row and diagonals to be = 15 each -> we need to identify a number that appeared in the above equations 4 times -> this will be the middle cell
    # after filling in the 5 in the middle cell, there are 4 corner cells and 4 non-corner cells
        # for each corner cell, the number in the corner cell appears 3 times in the above equations
        # for each non-corner cell, the number in the non-corner cell appears 2 times in the above equations
        # so, the number in the corner cell should be 2/4/6/8, and the number in the non-corner cell should be 1/9
    # if we choose 2 to be in the topleft cell, then 8 must be in the bottomright cell -> 1 choice
    # if we choose 4 to be in the topleft cell, then 6 must be in the bottomright cell -> total 2 choices
    # total no. of choices = 4C1 * 2C1 = 8
        # 4C1 = 4 ways to choose for the left corner cell (2,4,6,8)
        # 2C1 = 2 ways left to choose for the other corner cell (e.g. if I choose 2 for the topleft corner cell, then 8 is the only choice left for the bottomright corner cell -> we have 2 choices left for the topright corner cell)
        # we cannot choose the rest of the cells, they are determined by the choices we made for these 2 corner cells

def numMagicSquaresInside(grid):
    rows, cols = len(grid), len(grid[0])
    result = 0
    pattern1 = "438167294381672"
    pattern2 = "927618349276183"
    
    def is_magic(r, c):
        if grid[r][c] != 5:
            return 0
        neighbors = [
            [r-1, c], [r-1, c+1],
            [r, c+1], [r+1, c+1],
            [r+1, c], [r+1, c-1],
            [r, c-1], [r-1, c-1]
        ]
        sequence = ""

        for nr, nc in neighbors:
            sequence += str(grid[nr][nc])
        if sequence in pattern1 or sequence in pattern2:
            return True
        
        return False
    
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            result += int(is_magic(r, c))
    
    return result