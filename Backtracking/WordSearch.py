# https://leetcode.com/problems/word-search/
# MEDIUM
# Tags: backtracklc, dfslc, matrixlc, #79

# GIVEN:
    # m x n grid of characters, board
    # a string, word

# TASK:
    # return true if word exists in the grid
    # The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring
    # The same letter cell may not be used more than once

# EXAMPLES:
    # Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    # Output: true

    # Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    # Output: true

    # Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    # Output: false

###########################################################################################################

# ✅ ALGORITHM: BACKTRACKING / DFS

# TIME COMPLEXITY: O(m * n * 4^w)
    # m = number of rows
    # n = number of columns
    # w = length of word
    # O(m*n) for nested for loop
    # backtrack() takes 4^(len(word))
        # O(len(word)) for recursion call stack itself (without the 4 calls)
        # since we're calling backtrack() 4 times within each call, TC = O(4^len(word))
# SPACE COMPLEXITY: O(4^w)
    # w = length of word
    # for recursion call stack
        # O(len(word)) for recursion call stack itself (without the 4 calls)
        # since we're calling backtrack() 4 times within each call, TC = O(4^len(word))

def exist(board, word):
    rows, cols = len(board), len(board[0])
    path = set() # stores the encountered chars in board that match the chars in word
    
    def backtrack(r, c, i): # i = index in word of current char we're searching for
        if i == len(word): # if index i == length of word we're searching for, it means all chars in word have been found in board and in path
            return True
        
        if r < 0 or r >= rows or c < 0 or c >= cols: # if r,c out of bounds
            return False
        if word[i] != board[r][c]: # if current char in board is not the current char in word that we're searching for
            return False
        if (r,c) in path: # if current char already exists in path where we store encountered chars in board that match the char in word
            return False # since we cannot use the same letter more than once
        
        path.add((r,c))
        result = backtrack(r-1, c, i+1) or backtrack(r+1, c, i+1) or backtrack(r, c-1, i+1) or backtrack(r, c+1, i+1) # if either one of these are True, we've found the string
        path.remove((r,c)) # in backtracking, we clean up the last used possibility (the current position) since we don't have to revisit this position inside our path
        return result

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0): # if true, we have found the entire word string in board
                return True

    return False