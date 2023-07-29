# https://leetcode.com/problems/n-th-tribonacci-number/
# EASY
# Tags: dplc, hashmaplc, #1137

# GIVEN:
    # integer, n

# TASK:
    # return the value of Tn where T_0 = 0, T_1 = 1, T_2 = 1, and T_(n+3) = T_n + T_(n+1) + T_(n+2) for n >= 0

# EXAMPLES:
    # Input: n = 4
    # Output: 4
    # Explanation:
    # T_3 = 0 + 1 + 1 = 2
    # T_4 = 1 + 1 + 2 = 4

    # Input: n = 25
    # Output: 1389537

###########################################################################################################

# ✅ ALGORITHM 1: ITERATIVE DP (BOTTOM UP)
# Create integer array dp where each dp[i] = T_i
# set 0th, 1st and 2nd indexes for dp as 0, 1, 1
# iterate from index 3 to len(dp), where each dp[i] = dp[i-3] + dp[i-2] + d[i-1] = sum(dp[i-3:i])
# return last element in dp which is = T_n

# TIME COMPLEXITY: O(n)
    # Iterating over indices from 3 to n takes O(n) time
# SPACE COMPLEXITY: O(n)
    # We build an array of size n + 1, which takes O(n) space

def tribonacci(n):
    if n < 2: return n
    dp = [0] * (n+1)
    dp[0], dp[1], dp[2] = 0, 1, 1
    for i in range(3, n+1):
        dp[i] = sum(dp[i-3:i])
    return dp[-1]

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: BETTER ITERATIVE DP (BOTTOM UP)
# previous solution requires O(n) space complexity since we store all visited tribonacci no.s in dp
# each tribonacci no. only depends on its 3 previous no.s, and no.s before that do not affect its value
    # Therefore, it's unnecessary to store all the terms
# Instead, we only need to store 3 most recent tribonacci no.s (a, b, c)
    # Then, the next tribonacci no. is simply a + b + c
# Afterward, we update a, b, and c as the most recent 3 tribonacci no.s:
    # a = b
    # b = c
    # c = a + b + c
# We can continue obtaining the value of the next term using the same method of a + b + c
# This approach only requires constant space complexity

# TIME COMPLEXITY: O(n)
    # We have to update the value of a, b and c by n-2 times, each update takes constant time
    # Thus it takes O(n) time
# SPACE COMPLEXITY: O(1)
    # We only need to update several parameters: a, b and c, which takes O(1) space

def tribonacci(n):
    if n < 3:
        return 1 if n else 0
    a, b, c = 0, 1, 1
    for _ in range(n-2): # n-2 is bc n-2 no. of updates needed before c gets to n's position
        a, b, c = b, c, a + b + c
    return c

#==========================================================================================================

# ✅ ALGORITHM 3: RECURSIVE DP (TOP DOWN)
# let dfs(i) = T_i
# we are also given the following; store them in a dictionary:
    # dfs(0) = 0
    # dfs(1) = 1
    # dfs(2) = 1
# create recursive function where dfs(i) = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
    # if i = 0 or 1 or 2, return its corresponding value from the dictionary

# TIME COMPLEXITY: O(n)
    # We recursively call dfs on subproblems and each subproblem dfs(i) is computed once
# SPACE COMPLEXITY: O(n)
    # The hash map dp contains at most n + 1 key-value pairs

def tribonacci(n):
    dp = {0: 0, 1: 1, 2: 1}
        
    def dfs(i):
        if i in dp:
            return dp[i]
        dp[i] = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
        return dp[i]
    
    return dfs(n)