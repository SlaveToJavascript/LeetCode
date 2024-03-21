# https://leetcode.com/problems/longest-common-subsequence/
# MEDIUM
# Tags: dplc, 2ddplc, #1143

# GIVEN:
    # 2 strings, text1 and text2

# TASK:
    # return the length of their longest common subsequence
    # If there is no common subsequence, return 0
    # NOTE: A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
        # e.g. "ace" is a subsequence of "abcde"
    # A common subsequence of 2 strings is a subsequence that is common to both strings

# EXAMPLES:
    # Input: text1 = "abcde", text2 = "ace" 
    # Output: 3  
    # Explanation: The longest common subsequence is "ace" and its length is 3.

    # Input: text1 = "abc", text2 = "abc"
    # Output: 3
    # Explanation: The longest common subsequence is "abc" and its length is 3.

    # Input: text1 = "abc", text2 = "def"
    # Output: 0
    # Explanation: There is no such common subsequence, so the result is 0.

###########################################################################################################

# ✅ ALGORITHM: 2D DYNAMIC PROGRAMMING (BOTTOM UP)
    # https://www.youtube.com/watch?v=Ua0GhsJSlWM
# MAIN IDEA: if text1 = "abcde" and text2 = "ace", since the 1st character of each string is "a", then we can reduce this problem into its subproblem: we are now finding the LCS of "bcde" and "ce" (i.e. removed "a" from both strings)
    # if text1 = "abcde" and text2 = "bce", since the 1st character of both strings are different, we can reduce this problem into its subproblem: the LCS of the 2 strings are either in "abcde" and "ce", OR in "bcde" and "bce"
# Create a 2D dp grid m x n where m = len(text1), n = len(text2)
    # dp[i][j] = length of LCS of text1[i:] and text2[j:]
# to this dp grid, add a layer of 0's to its right and bottom borders
    # this is so we don't have to check for out of bounds errors ; also, the LCS of an empty string and any other string will always have a length of 0
    # e.g. if text1 = "abcde" and text2 = "ace", the grid should look like this:
        
        # a   c   e
    # a  [ ] [ ] [ ] [0]
    # b  [ ] [ ] [ ] [0]
    # c  [ ] [ ] [ ] [0]
    # d  [ ] [ ] [ ] [0]
    # e  [ ] [ ] [ ] [0]
    #    [0] [0] [0] [0]

# We start from comparing the last character of each string (i.e. "e")
# Since the last character of both substrings = "e", at the dp cell for "e" vs "e", we put 1 + the value at the bottom-right-diagonal cell
    # bottom-right-diagonal is because we are building the dp from bottom-right to top-left -> the answer we're looking for is in the topleft-most cell
    # +1 is because since the substrings "e" and "e" are the same -> we +1 as this is a common subsequence
# If the characters don't match, we put the value of the cell as max(value in the right cell, value in the bottom cell)
    # e.g. for text1 = "abcde" and text2 = "bce", since their 1st chars are different, the max length of LCS = max length of LCS("abcde" and "ce") (WHICH IS REPRESENTED BY THE CELL ON ITS RIGHT) vs LCS("bcde" and "bce") (WHICH IS REPRESENTED BY THE CELL AT ITS BOTTOM)
        # -> the value we put at the "a" vs "b" cell = max(value in the right cell, value in the bottom cell)
# After iterating through each cell of the dp matrix from bottom-right to top-left, we return the value at dp[0][0] (topleft)

# TIME COMPLEXITY: O(m * n)
    # m = len(str1), n = len(str2)
    # for the nested for-loop
# SPACE COMPLEXITY: O(m * n)
    # for the dp matrix

def longestCommonSubsequence(text1, text2):
    dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)] # creates a 2D dp matrix of rows = len(text1) + 1 and cols = len(text2) + 1
        # the +1 is for an extra layer of 0's on the right and bottom borders so we don't go out of bounds

    # iterate every cell in dp matrix starting from bottom-right cell
    for i in range(len(text1)-1, -1, -1):
        for j in range(len(text2)-1, -1, -1):
            if text1[i] == text2[j]: # if the characters in the strings are the same,
                dp[i][j] = 1 + dp[i+1][j+1] # we put (1 + value at diagonal cell) as the cell's value
            else: # if the characters in the strings are not the same,
                dp[i][j] = max(dp[i][j+1], dp[i+1][j]) # length of LCS = max(value in the right cell, value in the bottom cell)
    
    return dp[0][0]