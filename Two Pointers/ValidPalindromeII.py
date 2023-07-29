# https://leetcode.com/problems/valid-palindrome-ii/description/
# EASY
# Tags: twopointerslc, #680

# GIVEN:
    # a string, s

# TASK:
    # return true if the s can be palindrome after deleting at most one character from it

# EXAMPLES:
    # Input: s = "aba"
    # Output: true

    # Input: s = "abca"
    # Output: true
    # Explanation: You could delete the character 'c'.

    # Input: s = "abc"
    # Output: false

###########################################################################################################

# ✅ ALGORITHM 1: TWO POINTERS
# l and r pointers point at 1st and last character in s respectively
# while l <= r, keep shifting both pointers until char at l != char at r
# check if string without char at l = the reverse of itself and check if string without char at r = the reverse of itself
# return True / False according to above condition

def validPalindrome(s):
    if s == s[::-1]: return True # if string is already palindrome: return true

    l, r = 0, len(s)-1
    while l <= r:
        if s[l] != s[r]:
            # either remove char at l or r
            remove_l = s[:l] + s[l+1:]
            remove_r = s[:r] + s[r+1:]
            return remove_l == remove_l[::-1] or remove_r == remove_r[::-1]
        else:
            l += 1
            r -= 1