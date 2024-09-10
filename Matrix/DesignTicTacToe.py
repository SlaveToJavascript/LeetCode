# 348. Design Tic-Tac-Toe
# https://leetcode.com/problems/design-tic-tac-toe/
# MEDIUM
# Tags: matrixlc, premiumlc, #348

# Assume the following rules are for the tic-tac-toe game on an n x n board between two players:
    # A move is guaranteed to be valid and is placed on an empty block.
    # Once a winning condition is reached, no more moves are allowed.
    # A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

# Implement the TicTacToe class:
    # TicTacToe(int n) Initializes the object the size of the board n.
    # int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move, and the two players alternate in making moves. Return
        # 0 if there is no winner after the move,
        # 1 if player 1 is the winner after the move, or
        # 2 if player 2 is the winner after the move.

# EXAMPLES:
    # Input
    # ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
    # [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
    # Output
    # [null, 0, 0, 0, 0, 0, 0, 1]

    # Explanation
    # TicTacToe ticTacToe = new TicTacToe(3);
    # Assume that player 1 is "X" and player 2 is "O" in the board.
    # ticTacToe.move(0, 0, 1); // return 0 (no one wins)
    # |X| | |
    # | | | |    // Player 1 makes a move at (0, 0).
    # | | | |

    # ticTacToe.move(0, 2, 2); // return 0 (no one wins)
    # |X| |O|
    # | | | |    // Player 2 makes a move at (0, 2).
    # | | | |

    # ticTacToe.move(2, 2, 1); // return 0 (no one wins)
    # |X| |O|
    # | | | |    // Player 1 makes a move at (2, 2).
    # | | |X|

    # ticTacToe.move(1, 1, 2); // return 0 (no one wins)
    # |X| |O|
    # | |O| |    // Player 2 makes a move at (1, 1).
    # | | |X|

    # ticTacToe.move(2, 0, 1); // return 0 (no one wins)
    # |X| |O|
    # | |O| |    // Player 1 makes a move at (2, 0).
    # |X| |X|

    # ticTacToe.move(1, 0, 2); // return 0 (no one wins)
    # |X| |O|
    # |O|O| |    // Player 2 makes a move at (1, 0).
    # |X| |X|

    # ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
    # |X| |O|
    # |O|O| |    // Player 1 makes a move at (2, 1).
    # |X|X|X|

###########################################################################################################

# ✅ ALGORITHM：CHECK VERTICALLY, HORIZONTALLY AND DIAGONALLY with O(1) time
# create n*n matrix (2D array)
# every time a move() is made, check the horizontal vertical and 2 diagonal paths where the move is made in, whether all 3 elements in the path are == player's no.
# NOTE: we only need to check for a completed main diagonal path (top-left to bottom-right) if the move that was made falls in the main diagonal path, AND we only need to check for a completed anti-diagonal path (top-right to bottom-left) if the move that was made falls in the anti-diagonal path
    # condition for a cell (r,c) to be in the MAIN DIAGONAL path: r == c
    # ! condition for a cell (r,c) to be in the ANTI-DIAGONAL path: r + c == n-1

# TIME COMPLEXITY: O(1) for move()
# SPACE COMPLEXITY: O(n^2)
    # for the board

class TicTacToe(object):
    def __init__(self, n):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)] # create n*n matrix

    def move(self, row, col, player):
        self.board[row][col] = player # make the move by marking cell with player no.

        # check for valid horizontal row
        if all(ele == player for ele in self.board[row]):
            return player
        
        # check for valid vertical col
        if all(row[col] == player for row in self.board):
            return player
        
        # check for valid main diagonal (cells in top-left to bottom-right path) (only if row == col)
        if row == col and all(self.board[i][i] == player for i in range(self.n)):
            return player
        
        # check for valid anti-diagonal (cells in top-right to bottom-left path) (only if row+col == n-1)
            # cells in anti-diagonal: (0,n-1), (1,n-2), (2,n-3), ...
        if row + col == self.n-1 and all(self.board[i][self.n-i-1] == player for i in range(self.n)):
            return player
        
        return 0