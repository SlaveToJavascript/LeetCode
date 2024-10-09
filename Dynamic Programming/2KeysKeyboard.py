# 650. 2 Keys Keyboard
# https://leetcode.com/problems/2-keys-keyboard/
# MEDIUM
# Tags: dplc, #650

# There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:
    # Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
    # Paste: You can paste the characters which are copied last time.
# Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

# EXAMPLES:
    # Input: n = 3
    # Output: 3
    # Explanation: Initially, we have one character 'A'.
    # In step 1, we use Copy All operation.
    # In step 2, we use Paste operation to get 'AA'.
    # In step 3, we use Paste operation to get 'AAA'.

    # Input: n = 1
    # Output: 0

###########################################################################################################

# ✅ ALGORITHM 1: DYNAMIC PROGRAMMING (BOTTOM-UP i.e. MEMOIZATION) my solution
# ! MAIN IDEA: if n is even, dp[n] = dp[n//2] + 2 (+2 for 1 copy and 1 paste); if n is odd, we find the largest divisor of n and take dp[n] = dp[largest_divisor_of_n] + n//largest_divisor_of_n (+1 for 1 copy and n//largest_divisor_of_n - 1 pastes)

# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(n)

def minSteps(n):
    dp = [0] * (n+1)
    
    for i in range(2, len(dp)):
        if i % 2 == 0: # i is even
            dp[i] = dp[i//2] + 2 # +1 for copy, +1 for paste
        else:
            for j in range(i-1, 0, -1):
                if i % j == 0: # i is a divisor of j
                    dp[i] = dp[j] + i//j
                    break
    
    return dp[-1]