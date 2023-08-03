# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# MEDIUM
# Tags: twopointerslc, #122

# GIVEN:
    # an integer array, prices, where prices[i] is the price of a given stock on the ith day

# TASK:
    # find the maximum profit you can achieve, if you can buy the stock and sell it in the future
    # you can buy and sell as many times as you want, but can only hold 1 stock at any given time

# EXAMPLES:
    # Input: prices = [7,1,5,3,6,4]
    # Output: 7
    # Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    # Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    # Total profit is 4 + 3 = 7.

    # Input: prices = [1,2,3,4,5]
    # Output: 4
    # Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    # Total profit is 4.

    # Input: prices = [7,6,4,3,1]
    # Output: 0
    # Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

###########################################################################################################

# ✅ ALGORITHM 1: TWO POINTERS
# MAIN IDEA: as long as there is an increase in the stock, even if it's the next day, you should buy now then sell it when there's any increase
# Don't have to wait for a higher increase before selling since you can always buy now, sell tomorrow (for profit), then buy again tomorrow after selling, then sell again when there's a future price increase again

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def maxProfit(prices):
    profit = 0

    for i in range(1, len(prices)): # start from 2nd element in array since there is no previous price to compare to if we start from the 1st element
        if prices[i] > prices[i-1]: # as long as current element is greater than previous element, we make the profit (by buying and selling)
            profit += prices[i] - prices[i-1]
    
    return profit