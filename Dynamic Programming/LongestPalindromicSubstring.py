# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/description/
# MEDIUM
# Tags: 2ddplc, dplc, twopointerslc, #5

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

# ✅✅✅ ALGORITHM 2: TWO POINTERS, EXPAND FROM CENTERS
    # https://www.youtube.com/watch?v=XYQecbcd6_c
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

def longestPalindrome(s):
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

#==========================================================================================================

# ✅ ALGORITHM 3: 2D DYNAMIC PROGRAMMING
# MAIN IDEA:
    # if we know s[i]...s[j] is a palindrome, then if s[i-1] == s[j+1] (i.e. the char in front of i and the char behind j are the same), then s[i-1]...s[j+1] is also a palindrome
        # ODD-LENGTH PALINDROMES: each char s[i] on its own is a palindrome -> for each s[i-1]...s[i+1], if s[i-1] = s[i+1], then s[i-1]...s[i+1] is palindrome
        # EVEN-LENGTH PALINDROMES: if s[i] == s[i+1], then s[i]...s[i+1] is a palindrome -> if s[i-1] = s[i+2] (i.e. the char in front of and after the 2 bounds are the same), then s[i-1]...s[i+2] is a palindrome
# create a 2D array, dp, of size len(s) x len(s)
    # dp[i][j] = True if substring s[i]...s[j] inclusive is a palindrome, else False
# initialize ans = [0,0], where [i,j] are the inclusive bounds of the answer
    # i.e. ans = [i,j] means the answer (longest palindromic substring) = s[i]...s[j]
# EVEN-LENGTH PALINDROMES: initiate each dp[i][i] = True
    # because each char on its own is a palindrome
# ODD-LENGTH PALINDROMES: for each i, if s[i] == s[i+1], set dp[i][i+1] = True
    # e.g. "aa" is a palindrome -> set to True
# iterate over every possible difference between i and j, starting from 2 to len(s)-1
    # iterate over every possible value of i, from 0 to len(s)-diff
        # j = i + diff
        # if the chars at i and j are the same, and dp[i+1][j-1] is True, then s[i]...s[j] is palindrome -> set dp[i][j] = True, set ans = [i,j]
            # [i+1][j-1] refers to the pair immediately between i and j
# after the above nested iteration, i and j in ans is the starting and ending index of the longest palindrome
# if there is no palindrome, return the last initialized value of ans

# TIME COMPLEXITY: O(n^2)
    # We declare an n * n table dp, which takes O(n^2) time
    # We then populate O(n^2) pairs of i, j - each state takes O(1) time to compute
# TIME COMPLEXITY: O(n^2)
    # for the n*n dp table

def longestPalindrome(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    ans = [0,0] # [i,j] are the inclusive bounds of longest palindromic substring
        # s[i]...s[j] is the longest palindrome

    for i in range(n): # each char on its own is a palindrome -> set to True
        dp[i][i] = True
    
    for i in range(n-1): # if s[i] = s[i+1], then s[i]...s[i+1] is a palindrome -> set to True
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            ans = [i, i+1] # initiate answer to i, i+1 if s[i] = s[i+1]

    # check all substrings with len > 2, all the way up until len = n-1, for palindromes
    # diff is basically the difference between the starting and ending indices of the substring (i.e. length of substring -1)
    for diff in range(2, n): # for each possible diff = j-i,
        for i in range(n-diff): # When checking for palindromes of a specific length (diff + 1), the last starting index (i) that can be considered without going out of bounds is determined by subtracting diff from the total length n
            # i and j start iterating inwards from the outside (i.e. from the 2 ends of the substring)
            j = i + diff
            if s[i] == s[j] and dp[i+1][j-1]: # (i+1, j-1) is the pair between (i,j)
                dp[i][j] = True
                ans = [i,j]
    
    i, j = ans
    return s[i:j+1]