# https://leetcode.com/problems/minimum-penalty-for-a-shop/
# MEDIUM
# Tags: prefixlc, #2483

# GIVEN:
    # the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':
        # if the ith character is 'Y', it means that customers come at the ith hour
        # 'N' indicates that no customers come at the ith hour
    # If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:
        # For every hour when the shop is open and no customers come, the penalty increases by 1
        # For every hour when the shop is closed and customers come, the penalty increases by 1

# TASK:
    # Return the earliest hour at which the shop must be closed to incur a minimum penalty.
    # NOTE: if a shop closes at the jth hour, it means the shop is closed at the hour j

# EXAMPLES:
    # Input: customers = "YYNY"
    # Output: 2
    # Explanation: 
    # - Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
    # - Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
    # - Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
    # - Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
    # - Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
    # Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.

    # Input: customers = "NNNNN"
    # Output: 0
    # Explanation: It is best to close the shop at the 0th hour as no customers arrive.

    # Input: customers = "YYYY"
    # Output: 4
    # Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# For every hour from 0 to nth hour, find the penalty if we close at that hour
# Return the hour where the minimum penalty is incurred

# TIME COMPLEXITY: O(n^2) ❌
    # O(n) to iterate each hour
        # for each hour, we take O(n) to get the count of N's and Y's for the whole array
# SPACE COMPLEXITY: O(n)

def bestClosingTime(customers):
    # before closing, N -> +1 penalty
    # after closing, Y -> +1 penalty
    penalties = []
    for i in range(len(customers)):
        before = customers[:i].count('N')
        after = customers[i:].count('Y')
        penalties.append(before+after)
    
    penalties.append(customers.count('N'))
    
    return penalties.index(min(penalties))

#==========================================================================================================

# ✅ ALGORITHM 2: PREFIX and POSTFIX
# maintain 2 extra arrays:
    # prefix_n = number of N's before each index i in customers
    # postfix_y = number of Y's at and after each index i in customers
# 2 separate for loops to fill up prefix_n and postfix_y arrays
    # for prefix_n: fill it up from front to back
    # for postfix_y: fill it up from back to front
# sum up each element at index i in prefix_n and postfix_y and return the index i where the sum of prefix_n[i] + postfix_y[i] is the smallest

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def bestClosingTime(customers):
    # during and after closing, Y -> +1 penalty
    prefix_n = [0] * (len(customers)+1)
    postfix_y = [0] * (len(customers)+1)
    
    # fill up prefix_n
    for i in range(1, len(customers)+1):
        prefix_n[i] = prefix_n[i-1] + (customers[i-1] == "N") # before closing, +1 penalty for each N
    
    # fill up postfix_y (from back to front)
    for i in range(len(customers)-1, -1, -1):
        postfix_y[i] = postfix_y[i+1] + (customers[i] == "Y") # during & after closing, +1 penalty for each Y
    
    min_penalty = float('inf')
    idx = 0 # index of the smallest penalty where penalty = prefix_n[idx] + postfix_y[idx]

    for i in range(len(postfix_y)):
        penalty = prefix_n[i] + postfix_y[i]
        if penalty < min_penalty:
            min_penalty = penalty
            idx = i
    
    return idx