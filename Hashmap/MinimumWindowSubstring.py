# https://leetcode.com/problems/minimum-window-substring/description/
# HARD
# Tags: slidingwindowlc, hashmaplc, #76

# GIVEN:
    # 2 strings, s and t, of lengths m and n respectively

# TASK:
    # return the minimum window substring of s such that every character in t (including duplicates) is included in the window
    # If there is no such substring, return the empty string ""

# EXAMPLES:
    # Input: s = "ADOBECODEBANC", t = "ABC"
    # Output: "BANC"
    # Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

    # Input: s = "a", t = "a"
    # Output: "a"
    # Explanation: The entire string s is the minimum window.

    # Input: s = "a", t = "aa"
    # Output: ""
    # Explanation: Both 'a's from t must be included in the window.
    # Since the largest window of s only has one 'a', return empty string.

###########################################################################################################

# ✅ ALGORITHM: SLIDING WINDOW

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

from collections import Counter, defaultdict

def minWindow(s, t):
    if t == "":
        return ""
    
    countT = Counter(t) # each char in t -> no. of occurrence of char in t
    countSWindow = defaultdict(int) # each char in current s window -> no. of occurrence of char in current s window
    have, need = 0, len(countT) # need = there are x chars in t, which is what we need
        # have = there are y chars in current s window, which is what we have
        # when have = need, we have all t chars in current s window
    min_len = float('inf') # min. length of shortest window substring
    min_window = [-1, -1] # left and right indexes of min substring
    l = 0 # left boundary of s window

    for r in range(len(s)): # right boundary of s window
        countSWindow[s[r]] += 1 # update count of current char at right pointer in countSWindow hashmap
        if s[r] in countT and countSWindow[s[r]] == countT[s[r]]:
            have += 1

        # keep shrinking s window while we have all t chars in current window
        while have == need:
            if r-l+1 < min_len: # check if current s window length is less than existing window length
                min_window = [l, r] # if it is, update boundaries of min. window
                min_len = r-l+1 # update min. window length
            
            # keep shrinking s window by removing left char from current window
            countSWindow[s[l]] -= 1 # decrement hashmap frequency of left char in window by 1
            if s[l] in countT and countSWindow[s[l]] < countT[s[l]]: # if left char removed is part of t and count of this char in current s window (after removal) is now less than no. of this char in t,
                have -= 1
            l += 1 # move left bounary forward
    
    l, r = min_window # left and right boundaries of the minimum window substring
    return s[l:r+1] if min_len != float('inf') else "" # if min_len = infinity, we didn't update anything -> return "", else return the min. substring