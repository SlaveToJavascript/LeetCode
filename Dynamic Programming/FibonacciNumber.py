# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/description/
# EASY
# Tags: dplc, #509

# Fibonacci sequence: each number is the sum of the two preceding ones, starting from 0 and 1
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1
# TODO: Given n, calculate F(n)

# EXAMPLES:
    # Input: n = 2
    # Output: 1
    # Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

    # Input: n = 3
    # Output: 2
    # Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

    # Input: n = 4
    # Output: 3
    # Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

###########################################################################################################

# ✅ ALGORITHM 1: DYNAMIC PROGRAMMING (RECURSIVE, TOP DOWN) WITH MEMOIZATION

# TIME COMPLEXITY: O(n)
    # there are n unique subproblems
    # with memoization, each subproblem is solved exactly once
    # without memoization, TC = O(2^n)
# SPACE COMPLEXITY: O(n)

def fib(n):
    memo = {}

    def fib(n):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    
    return fib(n)

#==========================================================================================================

# ✅ ALGORITHM 2: DYNAMIC PROGRAMMING (ITERATIVE, BOTTOM UP)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)