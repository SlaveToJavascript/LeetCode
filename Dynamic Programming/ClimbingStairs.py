# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/
# EASY
# Tags: dplc, topinterview150lc, #70

# You are climbing a staircase. It takes n steps to reach the top
# Each time you can either climb 1 or 2 steps
# In how many distinct ways can you climb to the top?

# EXAMPLES:
    # Input: n = 2
    # Output: 2
    # Explanation: There are two ways to climb to the top.
    # 1. 1 step + 1 step
    # 2. 2 steps

    # Input: n = 3
    # Output: 3
    # Explanation: There are three ways to climb to the top.
    # 1. 1 step + 1 step + 1 step
    # 2. 1 step + 2 steps
    # 3. 2 steps + 1 step

###########################################################################################################

# ✅ ALGORITHM 1: DYNAMIC PROGRAMMING (RECURSIVE, TOP DOWN) WITH MEMOIZATION
# If n == 1, there is only 1 way to climb the stair
# If n == 2, there are two ways: climb two 1-step stairs or one 2-step stair
# For any other n, the no. of ways to climb to step n = no. of ways to climb to step n-1 + no. of ways to climb to step n-2
    # because at the (n-1)th step, you can take 1 more step to reach n, and at the (n-2)th step, you can take a 2-step jump to reach n

# TIME COMPLEXITY: O(n) 
    # there are n unique subproblems (1 for each step from 1 to n) ; with memoization, each subproblem is solved once
    # NOTE: without memoization, TC = O(2^n) 👎
        # each call generates 2 more calls, forming a binary tree of calls, where n is the depth of the tree
# SPACE COMPLEXITY: O(n)
    # memo takes O(n) space
    # max depth of recursion call stack = n (worst case)

def climbStairs(n):
    memo = {}

    def climb(n):
        if n in memo:
            return memo[n]
        if n <= 2:
            return n
            
        memo[n] = climb(n-1) + climb(n-2)
        return memo[n]
    
    return climb(n)

#==========================================================================================================

# ✅ ALGORITHM 2: DYNAMIC PROGRAMMING (ITERATIVE, BOTTOM UP)
# create array dp of size n+1
    # +1 because 0 to n (both inclusive)
# each dp[i] = no. of ways to reach the ith step
# FORMULA: no. of ways to reach ith step = no. of ways to reach (i-1)th step + no. of ways to reach (i-2)th step
# return the last element in dp (that is the no. of ways to reach the top of the stairs)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def climbStairs(n):
    if n < 2:
        return n
        
    dp = [0] * (n+1) # n+1 for the 0th index
    dp[1] = 1 # 1 way to reach 1st step
    dp[2] = 2 # 2 ways to reach 2nd step

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] # no. of ways to reach ith step = no. of ways to reach (i-1)th step + no. of ways to reach (i-2)th step

    return dp[-1]