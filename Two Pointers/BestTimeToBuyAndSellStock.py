# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# EASY
# Tags: twopointerslc, #121

# GIVEN:
    # integer array, prices, where prices[i] is the price of a given stock on ith day

# TASK:
    # Find and return max profit from buying a stock on one day and selling it another day in the future
    # If you cannot get any profit, return 0

# EXAMPLES:
    # Input: prices = [7,1,5,3,6,4]
    # Output: 5
    # Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    # Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

    # Input: prices = [7,6,4,3,1]
    # Output: 0
    # Explanation: In this case, no transactions are done and the max profit = 0.

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# Double for-loop where outer loop iterates each element before last element
# and inner loop iterates each element after the element from the outer loop and compares for max profit

# TIME COMPLEXITY = O(n^2) ❌

def maxProfit(prices):
    max_profit = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
    return max_profit

#==========================================================================================================

# ❌ ALGORITHM 2: Single for-loop, get max of all elements behind 
# Iterate each element before last element, while getting max of all elements behind that (pointer) element

# TIME COMPLEXITY = O(n^2) ❌

def maxProfit(prices):
    min = float('inf') # the biggest number
    max_profit = 0
    for price in prices:
        if price < min:
            min = price
        elif price - min > max_profit:
            max_profit = price - min
    return max_profit

#==========================================================================================================

# ✅ ALGORITHM 3: TWO POINTERS, SINGLE FOR-LOOP
# 2 pointers, left (aiming for min buy price) and right (aiming for max sell price)
# Iterate once through
    # if left < right (✅), find profit and check if profit is maximum
        # update max_profit (if necessary) and right pointer +1 to find even higher sell price (i.e. even higher profit)
    # if left > right (❌), make left pointer = right pointer so left becomes the smaller value. right pointer +1 to be 1 after left pointer
        # since right is smaller than left, it means we can buy the stock at an even lower price (right), so we move the left pointer to right
        # because why would we hold on to left pointer (which is greater than right) when we can wait one day and get a lower buying price, which would therefore lead to a higher profit in the future?
# Return max_profit

# TIME COMPLEXITY = O(n) ✅
# SPACE COMPLEXITY = O(1)

def maxProfit(prices):
    l = 0 # left pointer aims to get the min buy price that will give max profit
    r = 1 # right pointer aims to get the max sell price that will give max profit
    max_profit = 0
    
    while r < len(prices): # while right index is within length of prices array
        if prices[l] > prices[r]: # if left (min) is greater than right (max)
            l = r # left (min) index becomes right (max) index -> now left is smaller
            r += 1 # right (max) index moves forward (1 after left (min) index)
        else: # if left (min) is smaller than right (max)
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            r += 1
    
    return max_profit