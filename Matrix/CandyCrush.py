# 723. Candy Crush
# https://leetcode.com/problems/candy-crush/description
# MEDIUM
# Tags: matrixlc, twopointerslc, premiumlc, #723

# Given an m x n integer array board representing the grid of candy where board[i][j] represents the type of candy. A value of board[i][j] == 0 represents that the cell is empty.
# The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:
    # If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time - these positions become empty.
    # After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.
    # After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
    # If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.
# You need to perform the above rules until the board becomes stable, then return the stable board.

# EXAMPLES:
    # Input: board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
    # Output: [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]

    # Input: board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
    # Output: [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]

###########################################################################################################

# ✅ ALGORITHM 1: BRUTE FORCE
# THREE STEPS, repeat them until no more candies are crushed:
    # 1. Find (horizontal and vertical groups of 3)
    # 2. Crush (replace these groups of 3 with 0's)
    # 3. Drop (other candies fall down to replace the crushed candies in the board)
# (1) FIND:
    # create a set of candies that are to be crushed
    # iterate the matrix using a double for-loop, checking for horizontal groups of 3's; add the (r,c) coords of thes cells to the set
    # iterate the matrix again, checking for vertical groups of 3's; add the (r,c) coords of thes cells to the set
        # NOTE: for cells that are 0, skip these cells as 0's are already crushed
# (2) CRUSH:
    # for each cell (r,c) in the set, replace the cell value on the board with 0's
# (3) DROP:
    # in each column, locate the bottom-most cell with a 0 value and keep track of the lowest 0-cell's row index
    # iterate each column, and within each column, iterate each row starting from the bottom cell and going up
        # during the iteration, whenever we find a cell that is not 0, we swap it with the lowest_zero cell
            # whenever there was a swap done, move lowest_zero up (i.e. lowest_zero -= 1, since lowest_zero is a row index)

# TIME COMPLEXITY: O(m^2 * n^2)
    # m x n = size of board
    # each find_and_crush() takes O(m*n) time
    # there could be at most O(m*n) independent drop steps to eliminate all candy groups
    # -> overall TC = O(m^2 * n^2)
# SPACE COMPLEXITY: O(m * n)
    # to_crush set takes at most O(m*n) space, in the worst case where all candies are the same value

def candyCrush(board):
    rows, cols = len(board), len(board[0])
    
    def find_and_crush():
        to_crush = set()

        # find horizontal groups of 3 candies
        for r in range(rows):
            for c in range(2, cols):
                if board[r][c] == 0:
                    continue
                if board[r][c] == board[r][c-1] == board[r][c-2]:
                    to_crush.add((r,c))
                    to_crush.add((r,c-1))
                    to_crush.add((r,c-2))
        
        # find vertical groups of 3 candies
        for r in range(2, rows):
            for c in range(cols):
                if board[r][c] == 0:
                    continue
                if board[r][c] == board[r-1][c] == board[r-2][c]:
                    to_crush.add((r,c))
                    to_crush.add((r-1,c))
                    to_crush.add((r-2,c))
        
        for (r,c) in to_crush:
            board[r][c] = 0
        
        return bool(to_crush) # return True if to_crush is not empty (i.e. there were candies to crush), return False if no candies were crushed
    
    def drop():
        for c in range(cols):
            lowest_zero_r = -1
            for r in range(rows-1, -1, -1):
                # get the lowest 0-cell's row index
                if board[r][c] == 0:
                    lowest_zero_r = max(lowest_zero_r, r) # the lowest 0-cell has the largest row index
                # swap
                elif lowest_zero_r != -1: # if lowest 0-cell has already been found, and current cell's value is not 0,
                    board[r][c], board[lowest_zero_r][c] = 0, board[r][c] # swap the cells at r and lowest_zero_r
                    lowest_zero_r -= 1 # lowest_zero row index moves up
    
    while find_and_crush():
        drop()
    
    return board

#==========================================================================================================

# ✅✅ ALGORITHM 2: OPTIMIZED BRUTE FORCE (optimized DROP algorithm + space-optimized in-place crushing of candies)
# OPTIMIZED DROP ALGORITHM:
    # instead of swapping elements from bottom to top, we can use a more efficient method by compacting non-zero values and then filling up the remaining cells (at the top) with 0's
# SPACE-OPTIMIZED IN-PLACE CRUSHING OF CANDIES
    # Algorithm 1 takes at most O(m*n) space to store candies, but we can improve the way we mark candies to be crushed, by updating board in-place
    # !!! we can change the values of the crushed candies to their negative values, e.g. if board[r][c] = 25 and this candy needs to be crushed, we change it to board[r][c] = -25

# TIME COMPLEXITY: O(m^2 * n^2)
    # m x n = size of board
    # each find_and_crush() takes O(m*n) time
    # there could be at most O(m*n) independent drop steps to eliminate all candy groups
    # -> overall TC = O(m^2 * n^2)
# SPACE COMPLEXITY: O(1)
    # Both the function drop and find_and_crush involve in-place modification and do not require additional space

def candyCrush(board):
    rows, cols = len(board), len(board[0])
    
    def find_and_crush():
        crushed = False

        # find horizontal groups of 3 candies
        for r in range(rows):
            for c in range(2, cols):
                if board[r][c] == 0:
                    continue
                if abs(board[r][c]) == abs(board[r][c-1]) == abs(board[r][c-2]):
                    crushed = True
                    board[r][c] = -abs(board[r][c])
                    board[r][c-1] = -abs(board[r][c-1])
                    board[r][c-2] = -abs(board[r][c-2])
        
        # find vertical groups of 3 candies
        for r in range(2, rows):
            for c in range(cols):
                if board[r][c] == 0:
                    continue
                if abs(board[r][c]) == abs(board[r-1][c]) == abs(board[r-2][c]):
                    crushed = True
                    board[r][c] = -abs(board[r][c])
                    board[r-1][c] = -abs(board[r-1][c])
                    board[r-2][c] = -abs(board[r-2][c])

        # after compacting non-zero values, fill up the remaining cells (at the top) with 0's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] < 0:
                    board[r][c] = 0
        
        return crushed
    
    def drop():
        for c in range(cols):
            drop_to_index = rows-1 # drop_to_index is the row index in column c where the current cell in the iteration should fall to; it starts from the bottom-most cell in the column
            for r in range(rows-1, -1, -1): # iterate each cell in the column from bottom up
                if board[r][c] != 0:
                    board[drop_to_index][c] = board[r][c] # current cell at board[r][c] drops to the cell at row "drop_to_index"
                    drop_to_index -= 1 # drop_to_index moves up by 1 row
            
            for r in range(drop_to_index + 1):
                board[r][c] = 0 # after compacting non-zero values to the bottom, we fill up the remaining cells (at the top) with 0's
    
    while find_and_crush():
        drop()
    
    return board