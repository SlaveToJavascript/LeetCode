# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
# MEDIUM
# Tags: dplc, #714

# GIVEN:
    # an array, prices, where prices[i] is the price of a given stock on the ith day
    # an integer, fee, representing a transaction fee

# TASK:
    # Find the maximum profit you can achieve
    # You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction
    # NOTE: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again)
    # The transaction fee is only charged once for each stock purchase and sale

# EXAMPLES:
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6

###########################################################################################################

# ✅ ALGORITHM 1: DP (WITH 2 STATES)
# Consider that in the end, the only 2 states are that you don't own a share of stock, or that you do
    # Calculate the most profit you could have under each of these two cases:
    # 1) if I don't own a stock on the current day, I could have either not owned a stock on the previous day, or I could have owned a stock on the previous day and sold it on the current day
    # 2) if I own a stock on the current day, I could have either owned a stock on the previous day, or I could have not owned a stock on the previous day and bought it on the current day

# TIME COMPLEXITY: O(n)
    # n = len(prices)
# SPACE COMPLEXITY: O(1)

def maxProfit(prices, fee):
    # if I buy a stock on the 1st day:
    hold = -prices[0] # hold is what I have after buying a stock
    profit = 0 # profit is what I have after selling a stock; since we just bought the 1st day's stock and haven't sold it yet, profit = 0

    for i in range(1, len(prices)): # for the prices on the rest of the days,
        hold = max(hold, profit - prices[i]) # my hold on the ith day can be either: my existing hold (if I don't buy a stock), or my new hold after buying today's stock
        profit = max(profit, hold + prices[i] - fee) # my profit on the ith day can be either: my existing profit (if I don't sell the stock today) or my new profit after selling the stock today
        return profit

    return profit