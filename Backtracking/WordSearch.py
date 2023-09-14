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

# ✅ ALGORITHM 1: RECURSIVE BACKTRACKING DFS
# DFS: recursively explore each path (up, down, left, right) to check if we can form the target word
    # We dive deep into each path before moving onto the next potential path
# Backtracking: While DFS helps us to explore paths, backtracking ensures that if a path does not lead to a solution, we step back and explore other possible paths
    # In this problem, backtracking marks a cell as unvisited (removing it from path set) if the current path does not lead to the solution -> allows that cell to be part of other potential paths
    # ensures all potential paths can be explored without being obstructed by the previous unsuccessful paths

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
    
    def backtrack(r, c, i): # i = index in current char in word (we're searching for char word[i] in board)
        if i == len(word): # if index i == length of word we're searching for, it means all chars in word have been found in board and in path
                # NOTE: condition should not be len(path) == len(word) bc the 2 lengths might not be equal in cases where backtracking happens
            return True
        
        if r < 0 or r >= rows or c < 0 or c >= cols: # if r,c out of bounds
            return False
        if word[i] != board[r][c]: # if current char in board is not the current char in word that we're searching for
            return False
        if (r,c) in path: # if current char already exists in path where we store encountered chars in board that match the char in word
            return False # since we cannot use the same letter more than once
        
        path.add((r,c))
        if backtrack(r-1, c, i+1) or backtrack(r+1, c, i+1) or backtrack(r, c-1, i+1) or backtrack(r, c+1, i+1):
            return True # if either one of these are True, we've found the string
        path.remove((r,c)) # in backtracking, we clean up the last used possibility (the current position) since we don't have to revisit this position inside our path
            # in case all the recursive calls return False, we backtrack and try other paths
        
        return False

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0): # if true, we have found the entire word string in board
                return True

    return False

#==========================================================================================================

# ✅ ALGORITHM 2: DFS + MODIFY BOARD IN-PLACE AS VISITED
# For each char visited, mark it as visited
# while doing DFS over board, we keep checking if the current char in board = 1st char of the word to be searched
    # if current char = 1st char of word, we check for the remaining chars in string (i.e. take away 1st char from word)
    # when remaining word becomes an empty string, it means we have found the whole word in board -> return True
    # if all 4 neighbors are not = current char, it means this path is invalid -> unmark char as visited (i.e. revert cell's value back to original value of char)
        # then return False

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
        
        def dfs(r, c, remaining_word): # remaining_word = remaining string that has yet to be found
            if not remaining_word: # if remaining_word is an empty string -> all chars in word have been found
                return True

            if 0 <= r < rows and 0 <= c < cols and board[r][c] == remaining_word[0]: # if r,c within bounds and current char = 1st char of remaining_word
                temp = board[r][c] # we need to track its original value before marking as visited so that if current path does not contain the next char in word to be searched, we revert the value of this cell from "visited" back to its original value (so that other paths may use this cell in their path)
                board[r][c] = "#" # mark as visited
            
                for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # the 4 neighbors of current cell
                    nr, nc = r+x, c+y
                    if dfs(nr, nc, remaining_word[1:]): # if this neighbor = the next char to be found in word,
                        return True
                
                board[r][c] = temp # all 4 neighbors do not contain the char we are searching for -> this path is invalid -> revert current cell's value back into its original value (i.e. before we marked current cell as visited) so that other paths that contain this cell can use its original value
                return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, word): # if true is returned from dfs(), it means there is a valid path from r,c that contains all chars of word
                    return True
        
        return False