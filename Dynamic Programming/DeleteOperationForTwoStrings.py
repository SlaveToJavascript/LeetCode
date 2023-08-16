# https://leetcode.com/problems/delete-operation-for-two-strings/description/
# MEDIUM
# Tags: dplc, 2ddplc, #583

# GIVEN:
    # 2 strings, word1 and word2

# TASK:
    # return the minimum number of character deletions from word1 and/or word2 required to make word1 = word2

# EXAMPLES:
    # Input: word1 = "sea", word2 = "eat"
    # Output: 2
    # Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

    # Input: word1 = "leetcode", word2 = "etco"
    # Output: 4

###########################################################################################################

# ✅ ALGORITHM 1: 2D DYNAMIC PROGRAMMING (BOTTOM UP + MEMOIZATION)
# MAIN IDEA: we look for the longest common subsequence (LCS) of both strings -> remaining characters will be deleted
# Finding LCS: if word1 = "sea" and word2 = "sat", since the 1st character of each string is "s", then we can reduce this problem into its subproblem: we are now finding the LCS of "ea" and "at" (i.e. removed "s" from both strings)
    # if word1 = "sea" and word2 = "eat", since the 1st character of both strings are different, we can reduce this problem into its subproblem: the LCS of the 2 strings are either in "ea" and "eat", OR in "sea" and "at"
# Create a 2D dp grid m x n where m = len(word1), n = len(word2)
# to this dp grid, add a layer of 0's to its right and bottom borders
    # e.g. if word1 = "sea" and word2 = "eat", the grid should look like this:
        
        # e   a   t
    # s  [ ] [ ] [ ] [0]
    # e  [ ] [ ] [ ] [0]
    # a  [ ] [ ] [ ] [0]
    #    [0] [0] [0] [0]

# We start from comparing the last character of each string (i.e. "a" vs "t")
# Since the characters don't match, we put the value of the bottomright cell as max(value in the right cell, value in the bottom cell)
    # e.g. for word = "sea" and word2 = "eat", since their 1st chars are different, the no. of LCS = max of LCS("ea" and "eat") vs LCS("sea" and "at")
        # -> the value we put at the "s" vs "e" cell = max(value in the right cell, value in the left cell)
# Since the 2nd char of word1 and 1st char of word2 = "e", at the dp cell for "e" vs "e", we put 1 + the value at the bottom-right-diagonal cell
    # bottom-right-diagonal is because we are building the dp from bottom-right to top-left -> the answer we're looking for is in the topleft-most cell
    # e.g. if word1 = "sea", word2 = "sat", since the 1st char for both are "s", we continue looking for next char in the LCS in the remaining characters, i.e. "ea" (word1) and "at" (word2)
    # +1 is because since the chars "s" and "s" are the same -> we +1 as this is a common subsequence
# After iterating through each cell of the dp matrix from bottom-right to top-left, the value at dp[0][0] (topleft) is the length of the LCS of word1 and word2
# Return len(word1) + len(word2) - 2 * len(LCS)
    # we need the total no. of chars to be deleted from both strings to both form LCS

# TIME COMPLEXITY: O(m * n)
    # m = len(word1), n = len(word2)
    # for the nested for-loop
# SPACE COMPLEXITY: O(m * n)
    # for the dp matrix

def minDistance(word1, word2):
    dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)] # the +1 are for the additional layer of 0's at the bottom row and last column

    for i in range(len(word1)-1, -1, -1):
        for j in range(len(word2)-1, -1, -1):
            if word1[i] == word2[j]: # if the chars at current index of word1 and word2 are the same,
                dp[i][j] = 1 + dp[i+1][j+1] # +1 as we increment LCS length, then take from bottomright cell as the remaining of the LCS comes from word1[i+1:] and word2[j+1:]
            else: # if the chars at current index of word1 and word2 are different,
                dp[i][j] = max(dp[i+1][j], dp[i][j+1]) # the LCS can be found in word1[i+1:] vs word2[j:] OR word1[i:] vs word2[j+1:]
    
    return len(word1) + len(word2) - 2 * dp[0][0]

#==========================================================================================================

# ✅ ALGORITHM 2: RECURSION + CACHING
# Use helper function minDeletions(i, j) which returns the min character deletions needed so that word1[i:] = word2[j:]
# We use a cache to keep track of previously encountered values of (i,j) and read from cache whenever we reach a previously encountered value of (i,j)

# TIME COMPLEXITY: O(n^2)
    # n = max(len(word1), len(word2))

def minDistance(word1, word2):
    cache = {} # hashmap, where key = (i,j) and value = min no. of character deletions so that word1[i:] = word2[j:]

    def minDeletions(i, j): # returns the min character deletions needed so that word1[i:] = word2[j:]
        if (i, j) in cache:
            return cache[(i,j)]
        
        if i == len(word1) and j == len(word2): # i and j are out of bounds
            return 0

        if i == len(word1) or j == len(word2): # if either word1 or word2 is an empty string, 
            # just return remaining chars of the non-empty string
                # e.g. word1 = "abc", word2 = "", no. of deletions to make word1 become empty string = no. of characters in word1
            cache[(i,j)] = max(len(word1)-i, len(word2)-j) # this will get us the no. of chars in the non-empty string
            return cache[(i,j)]

        if word1[i] == word2[j]: # if the current chars at word1 and word2 are the same, we don't need to delete anything
            cache[(i,j)] = minDeletions(i+1, j+1) # we move to the next character in word1 and word2
            return cache[(i,j)]
        else: # if the current chars at word1 and word2 are different, we need to delete either the current char in word1 or the current char in word2
            option1 = 1 + minDeletions(i+1, j) # option1: delete current char of word1
            option2 = 1 + minDeletions(i, j+1) # option2: delete current char of word2
                # in both cases, we have to +1 as 1 character is deleted
            cache[(i,j)] = min(option1, option2) # now we find out which option results in min no. of deletions and cache that result
            return cache[(i,j)]
    
    return minDeletions(0,0) # return min character deletions needed so that word1 = word2