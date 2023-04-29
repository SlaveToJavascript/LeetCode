# https://leetcode.com/problems/longest-palindrome/

# Given: string s, return length of the longest palindrome that can be built with its letters (case sensitive)

# Input: s = "abccccdd"
# Output: 7
# Explanation: longest palindrome that can be built is "dccaccd", whose length is 7

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1

###########################################################################################################

# ✅ ALGORITHM 1: HASHMAP
# Create dictionary of each character in s and their respective frequencies in s
# Iterate dictionary and sum up the maximum EVEN-numbered values of each character frequency
    # i.e. s[character] // 2 * 2
    # e.g. if s[character] = 7, add 6; if s[character] = 6, add 6
# Check for any odd-numbered values in the dictionary; if there are, length +1 (it becomes middle character)

# TIME COMPLEXITY: O(n), where n is length of s
# SPACE COMPLEXITY: O(n), because of the creation of hashmap

def longestPalindrome(s):
    freqs = {}
    # Add each character in s and their respective frequencies into freqs dictionary
    for char in s:
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1
    
    # Iterate freqs dictionary to add largest EVEN-numbered value to length
    length = 0
    for char in freqs:
        length += freqs[char] // 2 * 2
    
    # If there are any odd-numbered values in dictionary, length +1 (middle character)
    if any(x % 2 != 0 for x in freqs.values()):
        length += 1
    
    return length

#============================================================================================================

# ALTERNATIVE SOLUTION:
import collections

def longestPalindrome(s):
    ans = 0
    for v in collections.Counter(s).itervalues():
        ans += v / 2 * 2
        if ans % 2 == 0 and v % 2 == 1:
            ans += 1
    return ans