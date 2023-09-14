# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
# HARD
# Tags: dplc, #123

# GIVEN:
    # an array, prices, where prices[i] is the price of a given stock on the ith day

# TASK:
    # Find the maximum profit you can achieve
    # You may complete at most 2 transactions
    # NOTE: Do not engage in multiple transactions simultaneously
        # i.e. you must sell a stock before you buy again

# EXAMPLES:
    # Input: prices = [3,3,5,0,0,3,1,4]
    # Output: 6
    # Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
    # Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

    # Input: prices = [1,2,3,4,5]
    # Output: 4
    # Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    # Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

    # Input: prices = [7,6,4,3,1]
    # Output: 0
    # Explanation: In this case, no transaction is done, i.e. max profit = 0.

###########################################################################################################

# ✅ ALGORITHM: DYNAMIC PROGRAMMING
# BASIC IDEA: iterate over the array of stock prices and update 4 variables:
    # buy1 - min. price seen so far for the 1st txn
    # profit1 - max. profit seen so far for the 1st txn
    # buy2 - min. price seen so far for the 2nd txn, taking into account the profit from the 1st txn
    # profit2 - max. profit seen so far for 2nd txn
# After iteration, profit2 is returned as the max. profit achievable with 2 txns

# Here's how the algorithm works step by step for the input [3,3,5,0,0,3,1,4]:
    # Initialize buy1, buy2 = infinity, and profit1, profit2 = 0
    # price = 3 --> (buy1, profit1, buy2, profit2) = (3, 0, 3, 0)
    # price = 3 --> (buy1, profit1, buy2, profit2) = (3, 0, 3, 0) (no change)
    # price = 5 --> (buy1, profit1, buy2, profit2) = (3, 2, 3, 2)
    # price = 0 --> (buy1, profit1, buy2, profit2) = (0, 2, -2, 2)
    # price = 0 --> (buy1, profit1, buy2, profit2) = (0, 2, -2, 2) (no change)
    # price = 3 --> (buy1, profit1, buy2, profit2) = (0, 3, -2, 5)
    # price = 1 --> (buy1, profit1, buy2, profit2) = (0, 3, -2, 5) (no change)
    # price = 4 --> (buy1, profit1, buy2, profit2) = (0, 4, -2, 6)

# TIME COMPLEXITY: O(n)
    # iterate over the array of prices once
# SPACE COMPLEXITY: O(1)
    # only 4 variables are used

def maxProfit(prices):
    buy1, buy2 = float('inf'), float('inf') # since we want to minimize the price we buy stocks at, initialize buy prices to infinity
    profit1, profit2 = 0, 0 # since we want to maximize profit, initialize profits to 0

    # iterate over prices to update buy prices and profit values
    for price in prices:
        # 1st transaction (buy, profit) values
        buy1 = min(buy1, price) # 1st buy price = min. price encountered so far
        profit1 = max(profit1, price - buy1) # 1st profit = max profit from selling at current price

        # 2nd transaction (buy, profit) values
        buy2 = min(buy2, price - profit1) # profit1 is what we earned from the previous txn, so profit1 can offset the buying cost of our 2nd txn
        profit2 = max(profit2, price - buy2) # 2nd profit = max profit from selling at current price

    return profit2 # total profit after 2 txns