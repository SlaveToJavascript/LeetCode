# 1180. Count Substrings with Only One Distinct Letter
# https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter
# EASY
# Tags: stringlc, #1180

# GIVEN:
    # a string, s

# TASK:
    # return the number of substrings that have only one distinct letter

# EXAMPLES:
    # Input: s = "aaaba"
    # Output: 8
    # Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
    # "aaa" occurs 1 time.
    # "aa" occurs 2 times.
    # "a" occurs 4 times.
    # "b" occurs 1 time.
    # So the answer is 1 + 2 + 4 + 1 = 8.

    # Input: s = "aaaaaaaaaa"
    # Output: 55

###########################################################################################################

# ✅ ALGORITHM: NO. OF SUBSTRINGS IN STRING OF LENGTH N = N*(N+1)/2
# ! FORMULA: for a string of length n, no. of substrings in the string = n*(n+1)/2
# iterate string s, with l and r pointers as the start and end of substrings with only 1 unique character; if we reach the end of string s or find a different char at pointer r from char at pointer l, add the no. of substrings within the current 1-character window to the result

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def countLetters(s):
    result = 0 # no. of substrings with 1 distinct char within string s
    l = 0
    for r in range(len(s)+1):
        if r == len(s) or s[l] != s[r]: # if r pointer reaches end of string or r points to a different char than l
            substr_len = r - l # substring = s[l] to s[r-1] inclusive
            result += substr_len * (substr_len+1) / 2 # apply the formula to get no. of substring within the current single-char string window
            l = r # reset current char as the new start of substring window
    
    return result