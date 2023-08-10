# https://leetcode.com/problems/number-of-matching-subsequences/description/
# MEDIUM
# Tags: hashmaplc, #792

# GIVEN:
    # a string, s
    # an array of strings, words

# TASK:
    # return the number of words[i] that is a subsequence of s
    # A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters
        # e.g. "ace" is a subsequence of "abcde"

# EXAMPLES:
    # Input: s = "abcde", words = ["a","bb","acd","ace"]
    # Output: 3
    # Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

    # Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
    # Output: 2

###########################################################################################################

# ❌ ALGORITHM 1: TWO POINTERS + BRUTE FORCE (TLE)
# For each word in words,
    # maintain 2 pointers, 1 for the current word, 1 for s
    # shift both pointers forward if the current char in word matches current char in s, else shift only s pointer forward
# return the no. of words in words array that are subsequences of s

# TIME COMPLEXITY: O(n * m) 👎
    # n = no. of words in words array, m = length of s

def numMatchingSubseq(s, words):
    count = 0

    for word in words:
        word_pointer = 0 # pointer for current word
        s_pointer = 0 # pointer for s

        while word_pointer < len(word) and s_pointer < len(s):
            if word[word_pointer] == s[s_pointer]:
                word_pointer += 1
                s_pointer += 1
            else:
                s_pointer += 1
        
        if word_pointer == len(word):
            count += 1
    
    return count

###########################################################################################################