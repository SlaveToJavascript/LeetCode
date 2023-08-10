# https://leetcode.com/problems/palindromic-substrings/description/
# MEDIUM
# Tags: twopointerslc, dplc, #647

# GIVEN:
    # a string, s

# TASK:
    # return the number of palindromic substrings in it
    # A string is a palindrome when it reads the same backward as forward

# EXAMPLES:
    # Input: s = "abc"
    # Output: 3
    # Explanation: Three palindromic strings: "a", "b", "c".

    # Input: s = "aaa"
    # Output: 6
    # Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE (TLE)
# Get every possible substring from s and check if it's a palindrome

# TIME COMPLEXITY: O(n^3) ❌
    # There are about O(n^2) substrings from a string of length n
    # Each substring takes O(n) time to check if it's a palindrome => O(n^3) total TC
# SPACE COMPLEXITY: O(1)

#==========================================================================================================

# ✅ ALGORITHM 2: TWO POINTERS, EXPAND AROUND CENTER
# We iterate s, starting from 1st element
# Initiate 2 pointers, left and right
# while left and right pointers are not out of bounds of string s, check if character at left = character at right
    # if yes, this substring is a palindrome
        # shift left pointer to the left and right pointer to the right (until it's out of bounds)
    # this checks for odd-length substrings only (i.e. substrings of lengths 1, 3, 5, ...) since we start from substring of length 1 and shift both left and right pointers at the same time
# in the same iteration of s, check for even-lengthed substrings for palindromes:
    # let left pointer = current char of s, and right pointer = left + 1
    # while left and right pointers are not out of bounds of string s, keep checking if char at left = char at right -> if yes, this substring is a palindrome
        # shift left pointer to the left and right pointer to the right (until it's out of bounds)
    # this checks for even-length substrings only (i.e. substrings of lengths 2, 4, 6, ...) since we start from substring of length 2 and shift both left and right pointers at the same time
# return the count of palindromic substrings in s

# TIME COMPLEXITY: O(n^2)
    # O(n) for iteration of each char in s
    # O(n) for the expansions of left and right pointers in each iteration of s
    # O(n) * O(n) -> O(n^2)
# SPACE COMPLEXITY: O(1)

def countSubstrings(s):
    result = 0 # return value; the count of the no. of palindromic substrings in s

    # loop through all chars in s
    for i in range(len(s)):
        left = right = i # initiate left and right pointers at the current character in s
        
        while left >= 0 and right < len(s) and s[left] == s[right]: # while left and right pointers are within bounds of s, and char at left = char at right,
            result += 1 # current substring is a palindrome
            left -= 1 # shift left and right pointers
            right += 1 # if chars at left and right are not the same, no point shifting the pointers as current string is not palindrome
        
        # check for even-lengthed palindromic substrings
        left = i # reset left and right pointers
        right = i + 1 # right now points to char after left instead of left, so we can start with a substring of size 2

        # the below is the same as the above, but for even-lengthed substrings
        while left >= 0 and right < len(s) and s[left] == s[right]: # while left and right pointers are within bounds of s, and char at left = char at right,
            result += 1 # current substring is a palindrome
            left -= 1 # shift left and right pointers
            right += 1 # if chars at left and right are not the same, no point shifting the pointers as current string is not palindrome
        
    return result