# https://leetcode.com/problems/merge-strings-alternately/description/
# EASY
# Tags: twopointerslc, stringlc, #1768

# GIVEN:
    # 2 strings, word1 and word2

# TASK:
    # Merge the strings by adding letters in alternating order, starting with word1
    # If a string is longer than the other, append the additional letters onto the end of the merged string
    # Return the merged string

# EXAMPLES:
    # Input: word1 = "abc", word2 = "pqr"
    # Output: "apbqcr"
    # Explanation: The merged string will be merged as so:
    # word1:  a   b   c
    # word2:    p   q   r
    # merged: a p b q c r

    # Input: word1 = "ab", word2 = "pqrs"
    # Output: "apbqrs"
    # Explanation: Notice that as word2 is longer, "rs" is appended to the end.
    # word1:  a   b 
    # word2:    p   q   r   s
    # merged: a p b q   r   s

    # Input: word1 = "abcd", word2 = "pq"
    # Output: "apbqcd"
    # Explanation: Notice that as word1 is longer, "cd" is appended to the end.
    # word1:  a   b   c   d
    # word2:    p   q 
    # merged: a p b q c   d

###########################################################################################################

# ✅ ALGORITHM 1: TWO POINTERS
# use 2 pointers: pointer p1 for word1, and pointer p2 for word2
# while both pointers are within bounds, add the respective chars to resulting string, and increment pointers
# add remaining chars not added to the resulting string from either word1 or word2, if any

# TIME COMPLEXITY = O(n+m)
    # n = len(word1), m = len(word2)
    # since each char in word1 and word2 is processed once
# SPACE COMPLEXITY = O(n+m)
    # space required to store result string

def mergeAlternately(word1, word2):
    result = ""
    p1 = p2 = 0
    while p1 < len(word1) and p2 < len(word2):
        result += word1[p1] + word2[p2]
        p1 += 1
        p2 += 1

    # fun fact: in Python, string/array slicing does not raise out of bounds index, but string/array indexing does (if out of bounds)
    # so the below 2 lines work even if p1/p2 is out of bounds
    result += word1[p1:]
    result += word2[p2:]
    
    return result