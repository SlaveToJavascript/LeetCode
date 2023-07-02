# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# MEDIUM

# GIVEN:
    # a string, s

# TASK:
    # find the length of the longest substring without repeating characters

# EXAMPLES:
    # Input: s = "abcabcbb"
    # Output: 3
    # Explanation: The answer is "abc", with the length of 3.

    # Input: s = "bbbbb"
    # Output: 1
    # Explanation: The answer is "b", with the length of 1.

    # Input: s = "pwwkew"
    # Output: 3
    # Explanation: The answer is "wke", with the length of 3.
    # Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# i iterates every character in s
# j (nested for loop) iterates every character in s after i
# isAllUnique(start, end) returns true if all chars between s[start] and s[end] are unique
# find max_len of unique substrings
# if isAllUnique(i, j), update max_len if current max_len greater than existing max_len

# TIME COMPLEXITY: O(n^3)
# SPACE COMPLEXITY: O(n)

def lengthOfLongestSubstring(s):
    def isAllUnique(start, end): # returns true if all chars in substring are unique
        chars = set()
        for i in range(start, end+1):
            if s[i] in chars:
                return False
            else:
                chars.add(s[i])
        return True
    
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if isAllUnique(i, j):
                max_len = max(max_len, j-i+1) # j-i+1 is the length of string starting from i and ending at j
    return max_len

#============================================================================================================

# ✅ ALGORITHM 2: SLIDING WINDOW
# define window as a set
# set left pointer = index 0
# iterate right pointer across string:
    # while s[right_pointer] is in window:
        # remove s[left_pointer] from window
        # shift left to the right by 1
    # add s[right_pointer] to window (now that there are no duplicates)
    # update new max length (= right-left+1) against existing max length
# return max length

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n) (because of the set)

def lengthOfLongestSubstring(s):
    max_len = 0
    window = set()
    left = 0
    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])
        max_len = max(max_len, right-left+1)
    return max_len