# 139. Word Break
# https://leetcode.com/problems/word-break/
# MEDIUM
# Tags: dplc, #139

# GIVEN:
    # a string, s, and a dictionary of strings, wordDict

# TASK:
    # return true if s can be segmented into a space-separated sequence of one or more dictionary words
    # the same word in the dictionary may be reused multiple times in the segmentation

# EXAMPLES:
    # Input: s = "leetcode", wordDict = ["leet","code"]
    # Output: true
    # Explanation: Return true because "leetcode" can be segmented as "leet code".

    # Input: s = "applepenapple", wordDict = ["apple","pen"]
    # Output: true
    # Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
    # Note that you are allowed to reuse a dictionary word.

    # Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    # Output: false

###########################################################################################################

# ✅ ALGORITHM 1: DYNAMIC PROGRAMMING (RECURSIVE, TOP DOWN)
# dp(i) returns True if it's possible to build s up to and including index i with the words in wordDict
    # e.g. if s = "leetcode" and wordDict = ["leet", "code"],
    # dp(3) = True, because s up to index i is "leet"
    # -> the answer to the problem should be returned by dp(len(s)-1)
# We work from the back of s to the front
# For dp(i) to return true,
    # the last x characters of s up until index i matches a word of length x, AND
    # dp(j), where j is the index before the current word matched up until index i, returns true

# TIME COMPLEXITY: O(n * w * k)
    # n = len(s)
    # w = len(wordDict)
    # k = average length of the words in wordDict
    # Explanation: i in dp(i) ranges from 0-n; for each execution of dp(i), we iterate over wordDict of length w, and for each word we perform substring operations which takes O(k)
# SPACE COMPLEXITY: O(n)
    # The data structure we use for memoization and the recursion call stack can use up to O(n) space

from functools import cache

def wordBreak(s, wordDict):
    @cache
    def dp(i):
        if i < 0: 
            return True # it's always possible to build s up to an empty string
            # also we want dp(-1) to return True so if e.g. s = "leet" which is in wordDict, dp(i - len(word)) in the lines below will return True

        for word in wordDict:
            if s[i - len(word) + 1 : i + 1] == word and dp(i - len(word)):
                return True
        
        return False
    
    return dp(len(s)-1)

#==========================================================================================================

# ✅ ALGORITHM 2: DYNAMIC PROGRAMMING (ITERATIVE, BOTTOM UP)
    # https://www.youtube.com/watch?v=Sx9NNgInc3A
# dp[i] is True if it's possible to build s up to and including index i with the words in wordDict
    # e.g. if s = "leetcode" and wordDict = ["leet", "code"],
    # dp[3] = True, because s up to index 3 is "leet"
    # dp[4] = False, because s up to index 4 is "leetc"
    # -> the answer to the problem should be dp[len(s)-1]
# Initialize dp of size len(s) with all False values
# i is the index in s we are currently at
    # for every word in wordDict,
        # if s up to index i is the same length as current word, or the index before i - len(word) is True,
        # and s up to index i matches the word,
        # set dp[i] = True
        # break out of the "for word in wordDict" loop
# return the last element in dp, i.e. dp[len(s)-1]

# TIME COMPLEXITY: O(n * w * k)
    # n = len(s)
    # w = len(wordDict)
    # k = average length of the words in wordDict
    # Explanation: i in dp[i] ranges from 0-n; for each dp[i], we iterate over wordDict of length w, and for each word we perform substring operations which takes O(k)
# SPACE COMPLEXITY: O(n)
    # we used an array, dp, of length n

def wordBreak(s, wordDict):
    dp = [False] * len(s)

    for i in range(len(s)):
        for word in wordDict:
            if i < len(word)-1: # if s up to and including i cannot even match the length of current word
                continue # go to the next word

            if (i+1 == len(word) or dp[i - len(word)]) and s[i+1-len(word) : i+1] == word:
            # if s up to index i is the same length as current word,
            # OR the index before i - len(word) is True,
            # AND s up to index i matches the word,
                dp[i] = True
                break # break out of wordDict loop since at least 1 word already matches current substring
    
    return dp[-1]