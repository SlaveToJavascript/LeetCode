# https://leetcode.com/problems/snakes-and-ladders/description
# MEDIUM
# Tags: graphlc, matrixlc, bfslc, #909

# You are given an n x n integer matrix board where the cells are labeled from 1 to n^2 starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row
# You start on square 1 of the board
# In each move, starting from square curr, do the following:
    # Choose a destination square, next, with a label in the range [curr + 1, min(curr + 6, n2)]
        # This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board
    # If next has a snake or ladder, you must move to the destination of that snake or ladder
        # Otherwise, you move to next
    # The game ends when you reach the square n^2
# A board square on row r and column c has a snake or ladder if board[r][c] != -1
    # The destination of that snake or ladder is board[r][c]
    # Squares 1 and n^2 do not have a snake or ladder
# Note that you only take a snake or ladder at most once per move
    # If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder
    # e.g. board = [[-1,4],[-1,3]], and on the first move, your destination square is 2
    # You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
# Return the least number of moves required to reach the square n2
    # If it is not possible to reach the square, return -1

# EXAMPLES:
    # Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    # Output: 4
    # Explanation: 
    # In the beginning, you start at square 1 (at row 5, column 0).
    # You decide to move to square 2 and must take the ladder to square 15.
    # You then decide to move to square 17 and must take the snake to square 13.
    # You then decide to move to square 14 and must take the ladder to square 35.
    # You then decide to move to square 36, ending the game.
    # This is the lowest possible number of moves to reach the last square, so return 4.

    # Input: board = [[-1,-1],[-1,3]]
    # Output: 1

###########################################################################################################

# ✅ ALGORITHM: BFS
# This is basically BFS except instead of checking the 4 neighbors of a node, we check all squares that can be reached when we roll a dice (i.e. check its next 6 neighbors)
    # we check each neighbor if the neighbor is the destination, i.e. n^2
# if not, add neighbor to queue together with no. of moves to get to neighbor from start

# TIME COMPLEXITY: O(n^2)
    # worst case: visit every square in the board
# SPACE COMPLEXITY: O(n^2)
    # we might store every square in queue and/or visited

def snakesAndLadders(board):
    n = len(board)
    board.reverse() # reverse the board so we start from row 0 and destination is in last row

    def coords(x): # get (r,c) coords of a square labelled x
        r = (x-1) // n
        # even rows: left to right
        c = (x-1) % n
        # odd rows: right to left -> flip the col number
        if r % 2 != 0: # if odd row,
            c = n - 1 - c # e.g. 1st col becomes last col, 2nd last col becomes 2nd col, etc.
        
        return (r,c)
    
    q = [(1, 0)] # q[i] = (square no., no. of moves to get to current square)
        # start from square 1, 0 moves to get to square 1
    visited = set()

    while q:
        square, moves = q.pop(0)
        
        for dice_num in range(1, 7): # iterate through each possible dice number from 1-6
            neighbor = square + dice_num # neighbor is the next square we land on after rolling dice
            nr, nc = coords(neighbor) # coords of neighbor
            if board[nr][nc] != -1: # if neighbor has a snake or ladder that brings us to another square,
                neighbor = board[nr][nc] # go to the square where it takes us

            if neighbor == n * n: # if neighbor is the destination (i.e. square n^2),
                return moves + 1 # moves = no. of moves to get to square, moves+1 = no. of moves to get to neighbor of square
            
            if neighbor not in visited: # if neighbor hasn't been visited as a neighbor of another square in the past,
                q.append((neighbor, moves+1)) # add neighbor to q
                visited.add(neighbor) # mark neighbor as visited
    
    return -1