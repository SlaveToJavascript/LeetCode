# 1100. Find K-Length Substrings With No Repeated Characters
# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/
# MEDIUM
# Tags: slidingwindowlc, hashmaplc, #1100

# GIVEN:
    # a string, s
    # an integer, k

# TASK:
    # return the number of substrings in s of length k with no repeated characters

# EXAMPLES:
    # Input: s = "havefunonleetcode", k = 5
    # Output: 6
    # Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.

    # Input: s = "home", k = 5
    # Output: 0
    # Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.

###########################################################################################################

# ✅ ALGORITHM: SLIDING WINDOW
# use a hashmap to store the count of each character in the current sliding window (each char must be <= 1)
# if the count of any char in the current window is greater than 1 OR if the size of window > k, shrink the window from the left until the count of each char in substring is = 1
# update the result (no. of k-lengthed substrings with no repeated chars) if length of window = k

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
    # OR space = O(1) since in the worst case, hashmap would have the max possible size of 26 (each letter in the alphabet)

from collections import defaultdict

def numKLenSubstrNoRepeats(s, k):
    chars_in_window = defaultdict(int) # chars in current window (between l and r) and their respective frequencies
    result = 0 # return value, i.e. no. of k-lengthed substrings with no repeated chars

    l = 0
    for r in range(len(s)):
        chars_in_window[s[r]] += 1

        while r-l+1 > k or chars_in_window[s[r]] > 1: # if length of current window > k OR there is a repeated char in current window,
            chars_in_window[s[l]] -= 1 # shrink window from the left by removing leftmost element from current window
            l += 1 # shift left pointer forward to shrink current window
        
        if r-l+1 == k: # if current window has a length of k,
            result += 1 # add its count to result
    
    return result