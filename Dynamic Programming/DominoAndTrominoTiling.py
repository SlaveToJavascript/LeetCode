# https://leetcode.com/problems/domino-and-tromino-tiling/
# MEDIUM
# Tags: dplc, #790

# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes
# Given an integer n, return the number of ways to tile an 2 x n board
# In a tiling, every square must be covered by a tile
# Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile
# NOTE: Since the answer may be very large, return it modulo 10^9 + 7

# EXAMPLES:
    # Input: n = 3
    # Output: 5
    # Explanation: The five different ways are show above.

    # Input: n = 1
    # Output: 1

###########################################################################################################

# ✅ ALGORITHM: DYNAMIC PROGRAMMING
# See DominoAndTrominoTiling.png
# MAIN IDEA: Starting from n=3, every n+1 has 2 more new combinations that cannot be formed from any previously formed combination
    # the remaining combinations for n=3 can be formed from the combinations for n=1 and n=2
# Create dp array where dp[i] = no. of ways to tile a 2*i board
# FORMULA: dp[i] = 2 * dp[i-1] + dp[i-3]
    # dp[1] = 1
    # dp[2] = 2

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def numTilings(n):
    dp = [1, 2, 5] + [0] * (n-3) # initiate values for n=1, n=2, n=3

    for i in range(3, n):
        dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % (10**9 + 7) # apply the formula
    
    return dp[n - 1] # return no. of tilings for n=n