# 322. Coin Change
# https://leetcode.com/problems/coin-change/description/
# MEDIUM
# Tags: dplc, graphlc, bfslc, #322

# GIVEN:
    # an integer array, coins, representing coins of different denominations
    # an integer, amount, representing a total amount of money

# TASK:
    # Return the smallest no. of coins that you need to make up that amount
    # If that amount of money cannot be made up by any combination of the coins, return -1

# EXAMPLES:
    # Input: coins = [1,2,5], amount = 11
    # Output: 3
    # Explanation: 11 = 5 + 5 + 1

    # Input: coins = [2], amount = 3
    # Output: -1

    # Input: coins = [1], amount = 0
    # Output: 0

###########################################################################################################

# ✅✅✅ ALGORITHM 1: DYNAMIC PROGRAMMING (BOTTOM UP)
# Create dp array, where dp[x] = min. no. of coins summing up to exactly $x
    # initiate each dp value with infinity (since we're comparing for minimum dp[x] for each x)
# dp[0] = 0 (since min. no. of coins to get $0 is 0, i.e. no coins)
# for amount from 1 to $amount, do an inner for-loop on the "coins" array:
    # if amount $x <= current coin amount, dp[x] = min(existing dp[x], 1 + dp[x - current_coin_amt])
        # the "1" comes from the current coin
        # e.g. at coin = 5, dp[7] = dp[7-5] = dp[2], i.e. min. no. of coins needed to get $7 = min. no. of coins needed to get $2 + 1 coin (i.e. the current coin whose value = $5)
# return value = dp[amount] if dp[amount] is not = the initialized value (i.e. infinity), else return -1
    # if dp[amount] = the initialized value (infinity), it means no coin combination was found for it -> return -1

# TIME COMPLEXITY: O(amount * len(coins))
# SPACE COMPLEXITY: O(amount)

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1) # initiate dp array of length = amount+1; each dp[i] is initiated to = infinity so that we can compare for the minimum
        # length of dp array = amount+1 so that we can have an additional dp[0] = 0
    dp[0] = 0 # a min. of 0 coins are needed to get $0
    
    for amt in range(1, len(dp)): # iterate from amt = $1 to amt = $amount
        for coin in coins: # iterate coins array
            if amt >= coin: # if current amount is greater than current coin amount,
                dp[amt] = min(dp[amt], 1 + dp[amt - coin])
    
    return dp[amount] if dp[amount] != amount+1 else -1 # if dp[amount] = initialized max value (amount+1), there are no coin combinations found with any of the coins

#==========================================================================================================

# ✅ ALGORITHM 2: BFS
# If we imagine the search as a tree, "the fewest number of coins that you need to make up that amount", in other words, is the shortest path
    # shortest = smallest amount of coins
# shortest path is a BFS algorithm
# when you use BFS you don't have to think about the minimum: the first returned number of coins will be the minimum
# IDEA: we try to build the amount using given coins
# each time we try one coin:
    # if we used n coins for current amount, then with current coin used, remaining amount and no. of coins is updated to: remaining amount = current_amount - coin; no. of coins used += 1
    # once the remaining amount = 0, we are done -> return corresponding no. of coins used
# if there was no return -> return -1 at the end

# TIME COMPLEXITY: O(amount * len(coins))
# SPACE COMPLEXITY: O(amount * len(coins))

def coinChange(coins, amount):
    q = [ (amount, 0) ] # q format: q[i] = (remaining_amount, no._of_coins)
    visited = set() # set with visited amount to avoid duplicate work

    while q:
        remaining_amt, num_coins = q.pop(0)
        if remaining_amt == 0: 
            return num_coins # if remaining amount is 0, we have found our answer
        
        for coin in coins:
            new_amt = remaining_amt - coin
            
            if new_amt >= 0 and new_amt not in visited: # if new_amt is at least 0 and we haven't checked this new_amt before,
                q.append((new_amt, num_coins+1)) # +1 for the current coin
                visited.add(new_amt) # mark this amount as checked
    
    return -1