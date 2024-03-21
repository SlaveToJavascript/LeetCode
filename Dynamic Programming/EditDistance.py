# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/description/
# MEDIUM
# Tags: dplc, lcs, #72

# GIVEN:
    # 2 strings, word1 and word2

# TASK:
    # return the minimum number of operations required to convert word1 to word2
    # You have the following three operations permitted on a word:
        # Insert a character
        # Delete a character
        # Replace a character

# EXAMPLES:
    # Input: word1 = "horse", word2 = "ros"
    # Output: 3
    # Explanation: 
    # horse -> rorse (replace 'h' with 'r')
    # rorse -> rose (remove 'r')
    # rose -> ros (remove 'e')

    # Input: word1 = "horse", word2 = "ros"
    # Output: 3
    # Explanation: 
    # horse -> rorse (replace 'h' with 'r')
    # rorse -> rose (remove 'r')
    # rose -> ros (remove 'e')

# NOTE: this question is an extension / variation of the LCS problem: Dynamic Programming/LongestCommonSubsequence.py

###########################################################################################################

# ✅ ALGORITHM 1: 2D DYNAMIC PROGRAMMING (BOTTOM UP) TABULATION
    # https://www.youtube.com/watch?v=XYi2-LPrwm4
# Assuming i pointer iterates word1 and j pointer iterates word2, this is how the pointers will move after each operation:
    # (1) INSERT A CHARACTER: (i, j + 1)
        # e.g. word1 = "horse", word2 = "ros", and i = 0, j = 0:
        # since word1[i] = "h" != word2[j] = "r", we insert "r" in word1 -> word1 = "rhorse"
        # now, i continues to point to "h", but j shifts forward by 1 since the 1st char of word2 was inserted into word1
            # -> we continue looking for the LCS of "horse" and "os"
    # (2) DELETE A CHARACTER: (i+1, j)
        # e.g. word1 = "horse", word2 = "ros", and i = 0, j = 0:
        # since word1[i] = "h" != word2[j] = "r", we delete "h" from word1 -> word1 = "orse"
        # since word1[i] is deleted, shift i forward by 1
            # -> we continue looking for the LCS of "orse" and "ros"
    # (3) REPLACE A CHARACTER: (i+1, j+1)
        # e.g. word1 = "horse", word2 = "ros" ; i = 0, j = 0:
        # since word1[i] = "h" != word2[j] = "r", we replace "h" with "r" in word1 -> word1 = "rorse"
        # since word1[i] is replaced such that word1[i] = word2[j], shift i and j forward by 1 each
            # -> we continue looking for the LCS of "orse" and "os"
# if word1[i] = word2[j], we just move i and j forward by 1 each, but don't need to +1 to the no. of operations

# NOTE: the min. no. of operations to make any string A to become an empty string = len(string A)
    # by deleting all chars of string A

# STEPS:
# 1. Create a 2D dp grid m x n where m = len(word1), n = len(word2)
    # dp[i][j] = min. no. of operations needed to convert word1[i:] to word2[j:]
# 2. Initialize the values in the rightmost column and bottom row of dp
    # dp[-1][-1] = 0 since there are 0 operations to convert an empty string into an empty string
    # (bottom row: convert empty word1 into word2) dp[-1][j] = len(word2) - j, since we have to insert "len(word2) - j" no. of chars into empty word1 to get word2
    # (right column: convert word1 into empty word2) dp[i][-1] = len(word1) - i, since we have to delete all chars in word1[i:] to make word1[i:] an empty string
# 3. Fill up the rest of dp from bottom right to top left
    # if word1[i] = word2[j], it means both chars are equal -> move i and j forward by 1 each, but don't need to +1 to the no. of operations
        # -> dp[i][j] = dp[i+1][j+1]
    # else, we take the min. no. of operations among each of the 3 operations (insert, delete, replace) and +1 -> this will be dp[i][j]'s value
        # -> dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
            # i.e. bottom, right, diagonal
# 4. Return dp[0][0]

# TIME COMPLEXITY: O(mn)
    # m = len(word1), n = len(word2)
    # We iterate over the entire dp grid once
# SPACE COMPLEXITY: O(mn)
    # We create a 2D dp grid of size m x n

def minDistance(word1, word2):
    rows, cols = len(word1), len(word2)
    dp = [[float('inf') for _ in range(cols+1)] for _ in range(rows+1)]
    dp[-1][-1] = 0 # initialize bottom-right cell: there are 0 operations to convert an empty string into an empty string

    # initialize right column
        # right column: convert word1 into empty word2 (by deleting all chars in word1)
    for i in range(rows, -1, -1):
        dp[i][-1] = len(word1) - i # no. of chars to delete from word1 = len(word1[i:]) i.e. len(word1) - i
    
    # initialize bottom row
        # bottom row: convert empty word1 into word2 (by inserting all chars of word2 into word1)
    for j in range(cols, -1, -1):
        dp[-1][j] = len(word2) - j # no. of chars to insert into empty word1 = len(word2[j:]) i.e. len(word
    
    # fill up the rest of the dp table from bottom right to top left
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], # delete
                                   dp[i][j+1], # insert
                                   dp[i+1][j+1]) # replace
    
    return dp[0][0]