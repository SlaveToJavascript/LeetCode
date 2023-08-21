# https://leetcode.com/problems/longest-repeating-character-replacement/
# MEDIUM
# Tags: slidingwindowlc, hashmaplc, #424

# GIVEN:
    # a string s
    # an integer k

# TASK:
    # You can choose any character of the string and change it to any other uppercase English character
    # You can perform this operation at most k times
    # TODO: Return the length of the longest substring containing the same letter you can get after performing the above operations

# EXAMPLES:
    # Input: s = "ABAB", k = 2
    # Output: 4
    # Explanation: Replace the two 'A's with two 'B's or vice versa.

    # Input: s = "AABABBA", k = 1
    # Output: 4
    # Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    # The substring "BBBB" has the longest repeating letters, which is 4.
    # There may exists other ways to achive this answer too.

###########################################################################################################

# ✅ ALGORITHM 1: SLIDING WINDOW + HASHMAP
# l and r pointer denotes the start and end of substring
# To check if a substring is valid, check if length of substring - no. of most frequent chars in substring <= k
    # e.g. substring = "BABB", k = 1 -> most frequent char in substring = "B", len(substring) - number of B's = 4-3 = 1 which is >= k
# if length of substring - no. of most frequent chars in substring > k, we shift l pointer forward until substring is valid again
# compare the length of each valid substring and return the maximum one

# TIME COMPLEXITY: O(n)
    # for the for-loop
# SPACE COMPLEXITY: O(1)
    # freq_hm will store at most 26 keys -> O(1)

from collections import defaultdict

def characterReplacement(s, k):
    freq_hm = defaultdict(int) # frequency hashmap: char -> no. of occurrences in current substring
    max_len = 0 # return value

    l = 0 # left pointer
    for r in range(len(s)): # right pointer
        freq_hm[s[r]] += 1 # increase the frequency of char s[r] by 1

        while (r-l+1) - max(freq_hm.values()) > k: # while substring is not valid, i.e. length of substring - no. of most frequent chars in substring > k
            freq_hm[s[l]] -= 1 # shifting l pointer forward means we remove an occurrence of char s[l] from freq_hm
            l += 1 # keep shifting l pointer forward until substring is valid

        # at this point, substring would be a valid substring
        max_len = max(max_len, r-l+1) # length of substring = r-l+1
    
    return max_len