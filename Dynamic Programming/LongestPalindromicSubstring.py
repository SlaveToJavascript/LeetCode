# https://leetcode.com/problems/longest-palindromic-substring/description/
# MEDIUM
# Tags: dplc, twopointerslc, #5

# GIVEN:
    # a string, s

# TASK:
    # return the longest palindromic substring in s

# EXAMPLES:
    # Input: s = "babad"
    # Output: "bab"
    # Explanation: "aba" is also a valid answer.

    # Input: s = "cbbd"
    # Output: "bb"

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE (TLE)
# Get every possible substring from s and check if it's a palindrome, then return the palindromic substring that has the max length

# TIME COMPLEXITY: O(n^3) ❌
    # There are about O(n^2) substrings from a string of length n
    # Each substring takes O(n) time to check if it's a palindrome => O(n^3) total TC
# SPACE COMPLEXITY: O(1)

#==========================================================================================================

# ✅ ALGORITHM 2: TWO POINTERS, EXPAND AROUND CENTER
# We iterate s, starting from 1st element
# We initiate the max_palindrome_len = 1 (since the shortest possible palindrome would be a single char in s)
    # max_palindrome_len is the length of the longest palindrome in s
# Initiate 2 pointers, left and right
# while left and right pointers are not out of bounds of string s, check if character at left = character at right
    # if yes, this substring is a palindrome
        # if length of this palindromic substring > existing max_palindrome_len, update max_palindrome_len and update answer to current substring
        # shift left pointer to the left and right pointer to the right (until it's out of bounds)
    # this checks for odd-length substrings only (i.e. substrings of lengths 1, 3, 5, ...) since we start from substring of length 1 and shift both left and right pointers at the same time
# in the same iteration of s, check for even-lengthed substrings for palindromes:
    # let left pointer = current char of s, and right pointer = left + 1
    # while left and right pointers are not out of bounds of string s, keep checking if char at left = char at right -> if yes, this substring is a palindrome
        # if length of this palindromic substring > existing max_palindrome_len, update max_palindrome_len and update answer to current substring
        # shift left pointer to the left and right pointer to the right (until it's out of bounds)
    # this checks for even-length substrings only (i.e. substrings of lengths 2, 4, 6, ...) since we start from substring of length 2 and shift both left and right pointers at the same time
# return the count of palindromic substrings in s

# TIME COMPLEXITY: O(n^2)
    # O(n) for iteration of each char in s
    # O(n) for the expansions of left and right pointers in each iteration of s
    # O(n) * O(n) -> O(n^2)
# SPACE COMPLEXITY: O(1)

def longestPalindrome(self, s):
    max_palindrome_len = 1 # initiate the length of the longest palindrome to 1, since the minimum length of a palindrome is just 1 character in s
    ans = s[0] # return value; initiate the answer (i.e. longest palindromic substring) to any char in s

    # loop through all chars in s
    for i in range(len(s)):
        left = right = i # initiate left and right pointers at the current character in s
        while left >= 0 and right < len(s) and s[left] == s[right]: # while left and right pointers are within bounds of s, and char at left = char at right,
            if right-left+1 > max_palindrome_len: # if length of current palindromic substring > existing max length of palindromic substrings,
                max_palindrome_len = max(max_palindrome_len, right-left+1) # update the max length
                ans = s[left : right+1] # update the return value with the current palindromic substring
            left -= 1 # shift left and right pointers
            right += 1 # if chars at left and right are not the same, no point shifting the pointers as current string is not palindrome
        
        # check for even-lengthed palindromic substrings
        left = i # reset left and right pointers
        right = left + 1 # right now points to char after left instead of left, so we can start with a substring of size 2

        # the below is the same as the above, but for even-lengthed substrings
        while left >= 0 and right < len(s) and s[left] == s[right]: # while left and right pointers are within bounds of s, and char at left = char at right,
            if right-left+1 > max_palindrome_len: # if length of current palindromic substring > existing max length of palindromic substrings,
                max_palindrome_len = max(max_palindrome_len, right-left+1) # update the max length
                ans = s[left : right+1] # update the return value with the current palindromic substring
            left -= 1 # shift left and right pointers
            right += 1 # if chars at left and right are not the same, no point shifting the pointers as current string is not palindrome

    return ans