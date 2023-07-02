# https://leetcode.com/problems/determine-if-two-strings-are-close/description/
# MEDIUM

# 2 strings are close to each other if you can get one from the other using the following operations:
# Operation 1: Swap any two existing characters
    # e.g. abcde -> aecdb
# Operation 2: Transform every occurrence of 1 existing char into another existing char, and do the same with the other char.
    # e.g. aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary

# TASK:
    # Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise

# EXAMPLES:
    # Input: word1 = "abc", word2 = "bca"
    # Output: true
    # Explanation: You can attain word2 from word1 in 2 operations.
    # Apply Operation 1: "abc" -> "acb"
    # Apply Operation 1: "acb" -> "bca"

    # Input: word1 = "a", word2 = "aa"
    # Output: false
    # Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

    # Input: word1 = "cabbba", word2 = "abbccc"
    # Output: true
    # Explanation: You can attain word2 from word1 in 3 operations.
    # Apply Operation 1: "cabbba" -> "caabbb"
    # Apply Operation 2: "caabbb" -> "baaccc"
    # Apply Operation 2: "baaccc" -> "abbccc"

###########################################################################################################

# ✅ ALGORITHM 1: HASHMAP
# Operation 1 (swap any 2 existing characters) basically means you can freely reorder any characters in the strings
# Operation 2 (transform every occurrence of any 1 existing char into another, and do the same w the other char) basically means you can freely assign the frequencies of the characters
    # i.e. the frequencies of chars in both strings are the same numbers
# so check for:
    # 1) if the sets of characters in both strings are the same
    # 2) if the integer frequencies of characters in both strings are the same

from collections import Counter

def closeStrings(word1, word2):
    if len(word1) != len(word2): return False # if their lengths are diff they're definitely not close
    word1hm = Counter(word1) # Counter() creates a dict of each unique letter in word1 (key) and its frequency (value)
    word2hm = Counter(word2)
    return set(word1hm.keys()) == set(word2hm.keys()) and sorted(word2hm.values()) == sorted(word1hm.values())