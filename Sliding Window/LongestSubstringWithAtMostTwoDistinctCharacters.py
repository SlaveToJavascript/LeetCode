# 159. Longest Substring with At Most Two Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
# MEDIUM
# Tags: slidingwindowlc, hashmaplc, premiumlc, #159

# GIVEN:
    # string, s

# TASK:
    # return the length of the longest substring that contains at most two distinct characters

# EXAMPLES:
    # Input: s = "eceba"
    # Output: 3
    # Explanation: The substring is "ece" which its length is 3.

    # Input: s = "ccaabbb"
    # Output: 5
    # Explanation: The substring is "aabbb" which its length is 5.

###########################################################################################################

# ✅ ALGORITHM: SLIDING WINDOW
# use a sliding window to keep track of the longest substring with at most two distinct characters
# use a hashmap to store the count of each character in the current substring
# if the count of distinct characters in the current substring is greater than 2, shrink the window from the left until the count of distinct characters is 2
# update the max length of the substring

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
    # additional space is used only for a hashmap with at most 3 elements

from collections import defaultdict

def lengthOfLongestSubstringTwoDistinct(s):
    max_len = 0
    distinct_chars = defaultdict(int)

    l = 0
    for r in range(len(s)):
        distinct_chars[s[r]] += 1 # add current char at r pointer to hashmap

        while len(distinct_chars) > 2: # if there are more than 2 distinct chars in this substring from l to r,
            distinct_chars[s[l]] -= 1 # shrink the window from the left
            if distinct_chars[s[l]] == 0: # if the count of the char at l pointer is 0,
                del distinct_chars[s[l]] # remove it from the hashmap
            l += 1 # move the left pointer to the right to shrink current window

        max_len = max(max_len, r-l+1) # update max length
    
    return max_len