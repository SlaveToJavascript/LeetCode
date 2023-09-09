# https://leetcode.com/problems/n-queens/
# HARD
# Tags: backtracklc, matrixlc, #51

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no 2 queens attack each other
# Given an integer n, return all distinct solutions to the n-queens puzzle
    # You may return the answer in any order
    # Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively

# EXAMPLES:
    # Input: n = 4
    # Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    # Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

    # Input: n = 1
    # Output: [["Q"]]

###########################################################################################################

# ✅ ALGORITHM: BACKTRACKING
# Since for each solution, we can only have at most 1 queen in each column, row and positive diagonal (i.e. bottom-left to top-right) and negative diagonal (i.e. top-left to bottom-right),
    # while iterating each row, we'll be putting exactly 1 queen in each row
    # to avoid putting a queen in a column that already has a queen, we maintain a cols_with_q set that contains the cols that have have queens
    # NOTE: we don't need to have a rows_with_q set since we'll be iterating each row and putting 1 queen in each row, so there can only possibly be 1 queen in each row
# To track positive and negative diagonals that have queens,
    # POSITIVE DIAGONAL cells go upwards from bottomleft to topright
        # for cells along a positive diagonal, their r+c values are the same
            # therefore, we can set the index of a positive diagonal = r+c
    # NEGATIVE DIAGONAL cells go downwards from topleft to bottomright
        # for cells along a negative diagonal, their r-c values are the same
            # therefore, we can set the index of a negative diagonal = r-c
    # therefore, to track the positive/negative diagonals that have queens, we can use a set similar to cols_with_q
# each backtrack(r) function call (where r = current row) iterates through each col c in row r and checks if that col / positive diagonal / negative diagonal already has a queen
    # if yes, skip this cell
    # if no, put queen in current cell and add current cell to the 3 sets (cols with queens, positive diagonals with queens, negative diagonals with queens)
# backtrack() to the next row (r+1)
# clean up the 3 sets and remove queen from current cell

# TIME COMPLEXITY: O(n!)
    # we have n choices (cells) for the 1st queen, n-2 choices for the 2nd queen, n-4 choices for the 3rd queen, etc.
    # therefore, total no. of solutions = n * (n-2) * (n-4) * ... * 1 = n!
# SPACE COMPLEXITY: O(n^2)
    # 3 sets (cols_with_q, pos_diag_with_q, neg_diag_with_q) each take O(n) space
    # board takes n*n space

def solveNQueens(n):
    board = [["."] * n for _ in range(n)] # nxn board of "."s
    result = [] # return value
    cols_with_q = set() # cols that already have queens
    pos_diag_with_q = set() # positive diagonals that already have queens
        # index = r+c
    neg_diag_with_q = set() # negative diagonals that already have queens
        # index = r-c

    def backtrack(r): # r = row no.
        if r == n: # this means all rows have been completed -> add this solution to result
            solution = [''.join(row) for row in board] # make each row array into string and add all strings into solution array
            result.append(solution) # add solution to return result
            return
        
        for c in range(n): # iterate each cell (col) in current row
            if c in cols_with_q or r+c in pos_diag_with_q or r-c in neg_diag_with_q: # if current col/positive diagonal/negative diagonal already has a queen,
                continue # skip this cell
            
            board[r][c] = "Q" # put queen in current cell
            cols_with_q.add(c) # mark current col as being occupied by queen
            pos_diag_with_q.add(r+c) # mark current +ve diagonal as being occupied by queen
            neg_diag_with_q.add(r-c) # mark current -ve diagonal as being occupied by queen

            backtrack(r+1) # go to next row

            board[r][c] = "." # remove queen from current cell
            cols_with_q.remove(c) # unmark current col
            pos_diag_with_q.remove(r+c) # unmark current +ve diagonal
            neg_diag_with_q.remove(r-c) # unmark current -ve diagonal
    
    backtrack(0)
    return result