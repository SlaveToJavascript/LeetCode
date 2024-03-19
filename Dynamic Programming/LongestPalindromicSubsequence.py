# 516. Longest Palindromic Subsequence
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
# MEDIUM
# Tags: dplc, #516

# GIVEN:
    # a string, s

# TASK:
    # find the longest palindromic subsequence's length in s
    # A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements

# EXAMPLES:
    # Input: s = "bbbab"
    # Output: 4
    # Explanation: One possible longest palindromic subsequence is "bbbb".

    # Input: s = "cbbd"
    # Output: 2
    # Explanation: One possible longest palindromic subsequence is "bb".

# NOTE: this question is almost exactly the same as Dynamic Programming/LongestCommonSubsequence.py

###########################################################################################################

# ✅✅✅ ALGORITHM 1: LONGEST COMMON SUBSEQUENCE USING S AND REVERSED S
    # https://youtu.be/bUr8cNWI09Q?t=30&si=se9OU6NjUGrGpGAR
# Since palindromes are 2 strings that are the same forwards and reversed, we can use the LCS algorithm with s and reverse(s)
    # if a subsequence from s is a palindrome, then that same subsequence should also be in reverse(s)
# so just apply the LCS algorithm to s and reverse(s)

# TIME COMPLEXITY: O(n^2)
    # n = len(s)
# SPACE COMPLEXITY: O(n^2)
    # for the 2D dp matrix

def longestPalindromeSubseq(s):
    dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)] # creates a 2D dp matrix of rows = len(s) + 1 and cols = len(s) + 1
        # the +1 is for an extra layer of 0's on the right and bottom borders so we don't go out of bounds

    # iterate every cell in dp matrix starting from bottom-right cell
    for i in range(len(s)-1, -1, -1):
        for j in range(len(s)-1, -1, -1):
            if s[i] == s[::-1][j]: # if the characters at i and j are the same,
                dp[i][j] = 1 + dp[i+1][j+1] # we put (1 + value at diagonal cell) as the cell's value
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    
    return dp[0][0]
