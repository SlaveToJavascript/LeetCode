# https://leetcode.com/problems/is-subsequence/
# EASY

# GIVEN:
    # 2 strings s and t

# TASK:
    # return True if s is a subsequence of T, or false otherwise

# EXAMPLES:
    # Input: s = "abc", t = "ahbgdc"
    # Output: true

    # Input: s = "axc", t = "ahbgdc"
    # Output: false

###########################################################################################################

# ✅ ALGORITHM 1: TWO POINTERS
# Use 2 index pointers, 1 for s, 1 for t
# while-loop through s and t
    # increase s and t pointers when s[i] == t[i], increase only t pointer otherwise
# if s pointer can loop through s completely, s is a subsequence of t (return True)

def isSubsequence(s, t):
    s_p, t_p = 0, 0 # setting s and t index pointers

    while s_p < len(s) and t_p < len(t): # pointers continue iterating until they reach the end of s or t
        if s[s_p] == t[t_p]: # if the characters match, move both pointers forward
            s_p += 1
            t_p += 1
        else:
            t_p += 1
    
    return s_p == len(s) # if s is subsequence of t, the pointer would reach the end of s after looping