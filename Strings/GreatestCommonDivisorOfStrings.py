# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
# EASY
# Tags: #1071

# GIVEN:
    # two strings str1 and str2

# TASK:
    # return the largest string x such that x divides both str1 and str2
    # NOTE: For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times)

# EXAMPLES:
    # Input: str1 = "ABCABC", str2 = "ABC"
    # Output: "ABC"

    # Input: str1 = "ABABAB", str2 = "ABAB"
    # Output: "AB"

    # Input: str1 = "LEET", str2 = "CODE"
    # Output: ""

###########################################################################################################

# ✅ ALGORITHM: BRUTE FORCE
# Start checking from the max possible length of the common divisor string, which is length of the shorter string
    # because question asks for longest possible common divisor string
# For each length, check if this length might be the length of a common divisor string
    # to check: first check if lengths of both strings are divisible by this length
        # then check if substring extracted from str1 of this length multiplied by (length of str2 divided by this length) == str2, and vice versa
        # if true, a substring of this length is a common divisor string

# TIME COMPLEXITY: O(min(m,n) * (m+n))
    # there are up to min(m, n) substring lengths to check (if it's a common divisor string length)
    # each check involves iterating over str1 and str2 to check if the substring of this length is a common divisor string, which takes O(m+n) time
# SPACE COMPLEXITY: O(min(m,n))
    # We need to keep a copy of base in each iteration, which takes O(min(m,n)) space

def gcdOfStrings(str1, str2):
    # helper function to check if str_len could be the length of a common divisor string
    # returns True if the common divisor string has a length of str_len
    def isCommonDivisor(str_len):
        if len(str1) % str_len or len(str2) % str_len:
            return False
        return str1[:str_len] * (len(str2)/str_len) == str2 and str2[:str_len] * (len(str1)/str_len) == str1

    for str_len in range(min(len(str1), len(str2)), 0, -1): # start checking from the longest possible length of a common divisor string, i.e. min(len(str1), len(str2))
        if isCommonDivisor(str_len):
            return str1[:str_len]
    
    return "" # no common divisor string found