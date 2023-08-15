# https://leetcode.com/problems/coin-change-ii/description/
# MEDIUM
# Tags: dplc, 2ddplc, #518

# GIVEN:
    # an integer array, coins, representing coins of different denominations
    # an integer, amount, representing a total amount of money

# TASK:
    # Return the number of combinations that make up that amount
    # If that amount of money cannot be made up by any combination of the coins, return 0

# EXAMPLES:
    # Input: amount = 5, coins = [1,2,5]
    # Output: 4
    # Explanation: there are four ways to make up the amount:
    # 5=5
    # 5=2+2+1
    # 5=2+1+1+1
    # 5=1+1+1+1+1

    # Input: amount = 3, coins = [2]
    # Output: 0
    # Explanation: the amount of 3 cannot be made up just with coins of 2.

    # Input: amount = 10, coins = [10]
    # Output: 1

###########################################################################################################

# ✅ ALGORITHM 1: 2D DYNAMIC PROGRAMMING
# Create m * n dp matrix, where m = no. of coins and n = amount from amount to 0
    # Each cell should be the no. of ways to form amount $n with coins [5] (for cells in the last row), coins [2,5] (for the cells in the 2nd last row) and coins [1,2,5] (for the cells in the 1st row)
    # We initiate the cells in the last column where amount = 0 as 1 each, since there will always be 1 way to get $0 with any combination/coins: by not picking any coins
    # We fill up the dp matrix from right to left, bottom to top
# if amount = 5 and coins = [1,2,5], dp matrix should look something like this:

            # 5   4   3   2   1   0
        # 1  [ ] [ ] [ ] [ ] [ ] [1]
        # 2  [ ] [ ] [ ] [ ] [ ] [1]
        # 5  [ ] [ ] [ ] [ ] [ ] [1]

# we start filling up the last row from right to left, followed by 2nd row from right to left, then 1st row from right to left
# for the last row, we are trying to form the $n using only coin [5],
    # if amount = $1, we take 1-5 = -4 which is out of bounds of the matrix -> set cell value = 0
    # if amount = $2, we take 2-5 = -3 which is out of bounds of the matrix -> set cell value = 0
    # if amount = $3, we take 3-5 = -2 which is out of bounds of the matrix -> set cell value = 0
    # if amount = $4, we take 4-5 = -1 which is out of bounds of the matrix -> set cell value = 0
    # if amount = $5, we take 5-5 = 0 which is in bounds -> we check the cell value at the same row at col = $0 which is 1 -> set cell value = 1

# for the 2nd row, we are trying to form the $n using coins [2,5],
    # if amount = $1, we take 1-2 = -1 which is out of bounds of the matrix -> set cell value = 0
        # the value at the cell below this cell = 0, so set final value of this cell as 0 + 0 = 0
    # if amount = $2, we take 2-2 = 0 which is in bounds -> we check the cell value at the same row at col = $0 which is 1 -> set cell value = 1
        # the value at the cell below this cell = 0, so set final value of this cell as 1 + 0 = 1
    # if amount = $3, we take 3-2 = 1 which is in bounds -> we check the cell value at the same row at col = $1 which is 0 -> set cell value = 0
        # the value at the cell below this cell = 0, so set final value of this cell as 0 + 0 = 0
    # ...and so on until each row and col cells are filled
# NOTE: while filling up each cell, we need to remember to add the value below this cell, since we can choose not to use the coin of the current row to make up to $n, but instead, use the other coins to make up $n

# finally, return the value at the topleft-most cell, i.e. dp[0][0]

# TIME COMPLEXITY: O(m*n)
    # m = no. of coins
    # n = amount
# SPACE COMPLEXITY: O(m*n)

def change(amount, coins):
    dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))] # amount+1 is for the additional col where amount = $0
    
    for r in range(len(dp)):
        dp[r][-1] = 1 # initialize all cells in the last col as 1, since the last col is for amount = $0 and there will always be 1 way to get $0

    for r in range(len(dp)-1, -1, -1): # iterate from right to left, bottom to top, starting from the last row at 2nd last col
        for c in range(amount-1, -1, -1):
            diff = amount-c - coins[r] # diff is the current amount $n - current coin at row
            if diff >= 0: # if diff is within bounds of dp,
                dp[r][c] = dp[r][amount - diff] # set current cell value as the value at same row, col = col for amount $diff
            if r < len(dp)-1: # if current row is not the last row of dp,
                dp[r][c] += dp[r+1][c] # we add the value below this cell to this cell
    
    return dp[0][0]

#==========================================================================================================

# ✅ ALGORITHM 2: 2D DYNAMIC PROGRAMMING (space optimized)
