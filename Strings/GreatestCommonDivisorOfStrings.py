# 1071. Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
# EASY
# Tags: stringlc, leetcode75lc, lc75lc, #1071

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
# Start checking from the max possible length of the common divisor string
    # the max possible length of the common divisor string is the length of the shorter string
    # qn asks for largest gcd string, so this is a greedy approach
# For each gcd string length, check if this length can possibly be the length of a common divisor string
    # to check: first check if lengths of both str1 and str2 are divisible by this gcd string length
        # if False, this gcd string is impossible to be the answer
    # if True, check if gcd substring of length substr_len extracted from str2 multiplied by (length of str1 divided by substr_len) == str1, and vice versa
    # if true, a substring of this length is a common divisor string
# return empty string if no common divisor string is found

# TIME COMPLEXITY: O(min(m,n) * (m+n))
    # there are up to min(m, n) substring lengths to check (if it's a common divisor string length)
    # each check involves iterating over str1 and str2 to check if the substring of this length is a common divisor string, which takes O(m+n) time
# SPACE COMPLEXITY: O(min(m,n))
    # We need to keep a copy of base in each iteration, which takes O(min(m,n)) space

def gcdOfStrings(str1, str2):
    for substr_len in range(min(len(str1), len(str2)), 0, -1): # this is the potential gcd substring length; it starts from length of shorter string and decreases at each iteration to find max length of potential gcd string
        
        if len(str1) % substr_len != 0 or len(str2) % substr_len != 0: # if either str1 or str2 cannot fully be divided by substr_len, this substr_len cannot possibly be length of gcd string
            continue # continue to the next iteration
        
        elif len(str1)//substr_len * str2[:substr_len] == str1 and len(str2)//substr_len * str1[:substr_len] == str2: # check if gcd substring of length substr_len extracted from str2 multiplied by (length of str1 divided by substr_len) == str1, and vice versa
            return str1[:substr_len]
    
    return "" # if no gcd substring was returned at this point, it means there is no gcd substring for str1 and str2