# https://leetcode.com/problems/online-stock-span/description/
# MEDIUM
# Tags: monotonicstacklc, stacklc, monotoniclc, designlc, #901

# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day
# The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day
    # e.g. if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days
    # Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days

# Implement the StockSpanner class:
    # StockSpanner() Initializes the object of the class
    # next(int price) Returns the span of the stock's price given that today's price is price

# EXAMPLES:
    # Input
    # ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
    # [[], [100], [80], [60], [70], [60], [75], [85]]
    # Output
    # [null, 1, 1, 1, 2, 1, 4, 6]

    # Explanation
    # StockSpanner stockSpanner = new StockSpanner();
    # stockSpanner.next(100); // return 1
    # stockSpanner.next(80);  // return 1
    # stockSpanner.next(60);  // return 1
    # stockSpanner.next(70);  // return 2
    # stockSpanner.next(60);  // return 1
    # stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
    # stockSpanner.next(85);  // return 6

###########################################################################################################

# ✅ ALGORITHM: DECREASING MONOTONIC STACK
# Create a stack where stack[i] = (price, span)
# For the next(price) function, when we want to add a price to stack, we will only add price to stack if current price is smaller than the price at the top of the stack
    # if current price < price @ top of stack, its span = 1
    # add (current price, span) to stack
# Else, if current price >= price @ top of stack (i.e. we found a higher price), we keep popping from stack until we found a current price that is < price @ top of stack, then we add that current price to stack
    # for each popped price's span, we increment current price's span by it
# return span

# TIME COMPLEXITY: O(n)
    # n = number of prices
    # while loop can run at most n times
# SPACE COMPLEXITY: O(n)
    # worst case scenario: all the stock prices are decreasing -> while loop will never run, which means the stack grows to a size of n

class StockSpanner(object):
    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1 # initiate span to 1 (if price < price @ top of stack, its span is 1)
        
        while self.stack and price >= self.stack[-1][0]: # while price >= price @ top of stack
            popped_stock, popped_span = self.stack.pop() # keep popping from stack
            span += popped_span # increment the span of current price by popped spans
        
        self.stack.append((price, span)) # add current price and its span to stack
        
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)