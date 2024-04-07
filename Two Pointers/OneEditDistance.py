# 161. One Edit Distance
# https://leetcode.com/problems/one-edit-distance/description/
# MEDIUM
# Tags: twopointerslc, stringlc, #161

# GIVEN:
    # 2 strings, s and t

# TASK:
    # return true if they are both one edit distance apart, otherwise return false
    # A string s is said to be one distance apart from a string t if you can:
        # Insert exactly one character into s to get t.
        # Delete exactly one character from s to get t.
        # Replace exactly one character of s with a different character to get t

# EXAMPLES:
    # Input: s = "ab", t = "acb"
    # Output: true
    # Explanation: We can insert 'c' into s to get t.

    # Input: s = "", t = ""
    # Output: false
    # Explanation: We cannot get t from s by only one step.

###########################################################################################################

# ✅ ALGORITHM 1A: TWO POINTERS (my solution, attempted 08/04/2024)
# if s == t, return False as only 0 edits are needed
# length of s and t differs by more than 1, return False as they cannot possibly be 1 distance apart
# 2 pointers, 1 for each string that starts at the beginning of the string, comparing the respective chars at s and t
# if the chars are not equal and have not been edited, there are 3 possibilities to edit:
    # 1. INSERT 1 CHAR INTO s TO GET t
        # we know we need to insert a char into s if len(s) < len(t) by 1
        # since we're inserting a char into the current index of s, increment index of t by 1 to "skip" char at current index of t
    # 2. DELETE 1 CHAR FROM s TO GET t
        # we know we need to delete a char from s if len(s) > len(t) by 1
        # since we're deleting the char at current index of s, increment index of s by 1 to "skip" current char
    # 3. REPLACE 1 CHAR IN s WITH A DIFFERENT CHAR TO GET t
        # increment both pointers by 1 to "skip" current chars
# if we've already edited the strings, return False because it means we need at least 2 steps
# if we reach the end of the strings and have not edited the strings, return True

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def isOneEditDistance(s, t):
    if s == t:
        return False
    if abs(len(s)-len(t)) > 1: # lengths of s and t differ by more than 1 -> not 1 edit distance apart
        return False
    
    ps = pt = 0 # ps = pointer for s, pt = pointer for t
    edited = False # flag to check if we've already edited string s
    
    while ps < len(s) and pt < len(t):
        if s[ps] != t[pt] and not edited:
            if len(s) < len(t):
                # insert 1 char into s to get t
                # e.g. ab, acb
                pt += 1
                edited = True
            elif len(s) > len(t):
                # delete 1 char from s to get t
                # e.g. abcd, abd
                ps += 1
                edited = True
            else:
                # replace 1 char in s to get t
                # e.g. abcd, abdd
                ps += 1
                pt += 1
                edited = True
        elif s[ps] != t[pt] and edited: # current chars are different but we've already edited the string once
            return False
        elif s[ps] == t[pt]:
            ps += 1
            pt += 1
    
    return True

#============================================================================================================

# ✅✅✅ ALGORITHM 1B: TWO POINTERS (LeetCode editorial solution – less verbose)
# for simplicity, ensure that s is the shorter string
# RULES:
    # 1. if length of s and t differ by more than 1, they are not 1 edit distance apart
    # 2. if chars of s and t at an index i are different,
        # if s and t are the same length, it means we can replace current char in s with a different char to get t -> check if the rest of the strings s and t are the same
        # if s is shorter than t, it means we can insert a char into s to get t -> check if the rest of the string t is the same as string s from and including the current index
    # 3. if the 1st "len(s)" chars of s and t are the same, the strings can only be 1 edit distance apart if t has 1 extra char at the end

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def isOneEditDistance(s, t):
    if len(s) > len(t):
        isOneEditDistance(t, s) # ensure that s is the shorter string
    
    if len(t) - len(s) > 1:
        return False # lengths of s and t differ by more than 1 -> not 1 edit distance apart
    
    for i in range(len(s)):
        if s[i] != t[i]:
            if len(s) == len(t): # if s and t have the same length, check if the rest of the strings are the same
                return s[i+1:] == t[i+1:] # replace 1 char in s with a different char to get t
            else: # if s is shorter than t, check if the rest of string t is the same as as string s from the current index
                return s[i:] == t[i+1:] # insert 1 char into s to get t
    
    # if the 1st "len(s)" chars of s and t are the same, the strings can only be 1 edit distance apart if t has 1 extra char at the end
    return len(s) + 1 == len(t)