# https://leetcode.com/problems/decode-ways/description/
# MEDIUM
# Tags: hashmaplc, stringlc, dplc, #91

# GIVEN:
    # integer string s (e.g. "12345")

# TASK:
    # assuming alphabets can be decoded to numbers with the following mapping:
        # A -> 1
        # B -> 2
        # ...
        # Z -> 26

    # return the number of ways s can be decoded

# EXAMPLES:
    # Input: s = "11106"
    # Output: 2
    # Explanation: "11106" could be decoded as "AAJF" (1,1,10,6) or "KJF" (11,10,6).
    #     Note that the grouping (1,11,06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

    # Input: s = "12"
    # Output: 2
    # Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

    # Input: s = "226"
    # Output: 3
    # Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

    # Input: s = "06"
    # Output: 0
    # Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

###########################################################################################################

# ❌ ALGORITHM 1: RECURSION (TLE)
# e.g. if s = "12345",
# MAIN IDEA:
# To decode "12345": either decode "1" (-> "A") then decode("2345"), OR, decode "12" (-> "L") then decode("345")
# Therefore, num_ways("12345") = num_ways("2345") + num_ways("345")

# However, to decode "27345", you can ONLY do: decode "2" (-> "B") then decode("7345")
    # because there is no decode("27") as there is no mapping for 27
# Therefore, num_ways("27345") = num_ways("7345")

# ***** IN SUMMARY *****:
    # base cases: (1) when string is empty, and (2) when string starts with "0"
    # recursive cases:
        # (1) num_ways("12345") = num_ways("2345") + num_ways("345")
        # (2) num_ways("27345") = num_ways("7345")

# TIME COMPLEXITY: O(2^n) ❌

def numDecodings(s):
    # use a helper function that returns the number of ways to decode the last k letters of string
    # e.g. helper("12345", 3) means we only look at the last 3 digits, i.e. "345"
        # so we don't have to create a new string every time we recurse
    def helper(s, k):
        # base cases: when string is empty AND when string starts with "0"
        if k == 0: return 1 # there is 1 way to decode an empty string
        if s[0] == "0": return 0

        # recursive cases:
        starting_decode_idx = len(s)-k # this is the starting index of the string we want to decode
        if int(s[starting_decode_idx : starting_decode_idx+2]) <= 26: # if the first 2 digits of the string we want to decode is <= 26
            result = helper(s, k-1) + helper(s, k-2)
        else: # if the first 2 digits of the string we want to decode is > 26
            result = helper(s, k-1)
        return result
    
    return helper(s, len(s))

#==========================================================================================================

# ✅ ALGORITHM 2: DYNAMIC PROGRAMMING WITH HASHMAP
# Let dp[i] be the no. of ways to decode a string from the start up till dp[i]
    # e.g. for s = "12345", if i=2, dp[i] = no. of ways to decode the string "123"
# MAIN IDEA: dp[i] = dp[i+1] + dp[i+2] (if first 2 chars of s are <=26) 
        # OR dp[i] = dp[i+1] (if first 2 chars of s are > 26)

# TIME COMPLEXITY: O(n)
    # since we are using hashmap to store no. of ways a substring can be decoded, to avoid recalculating them (which is the concept of memoization)
# SPACE COMPLEXITY: O(n)
    # we are using hashmap of variable length n

def numDecodings(s):
    ways_to_decode = { len(s) : 1 } # this is our cache where key is the index of a char in s, and value is the no. of ways to decode a string from the begining until i
        # e.g. for s = "12345", if i=2, ways_to_decode[i] = no. of ways to decode the string "123"
    # we initialize len(s) in the hashmap so if we get an empty string, we can return 1 (there is 1 way to decode an empty string)

    def helper(i): # i is the index we are currently at in our string s
        if i in ways_to_decode: # either i has already been cached, or i is at the last digit in s
            return ways_to_decode[i]
        if s[i] == "0": # if s starts with 0, there are no possible ways to decode
            return 0
        
        num_ways = helper(i+1)
        
        # RECALL THE FORMULA:
            # if s starts with "27" and above for its 1st 2 chars, no. of ways to decode s = no. of ways to decode the integer starting from the 2nd char
                # e.g. if s = "27345", no. of ways to decode "27345" = no. of ways to decode "7345"
            # else if s starts with "26" and below for its 1st 2 chars, no. of ways to decode s = no. of ways to decode the integer starting from the 2nd char + no. of ways to decode the integer starting from the 3rd char
                # e.g. if s = "12345", no. of ways to decode "12345" = no. of ways to decode "2345" + no. of ways to decode "345"
        
        num_ways = helper(i + 1) # if 1st 2 chars of s > 26, this is the no. of ways to decode s
        if i + 1 < len(s): # if we have a 2nd digit that comes after our current digit at i
            if int(s[i : i+2]) <= 26: # if the int of the 2 digits from i and i+1 are <= 26,
                num_ways += helper(i + 2) # we also need to add the number of ways to decode s[i+2:] to find its total no. of ways of decoding
        ways_to_decode[i] = num_ways # cache the no. of ways to decode s up till and including the digit at i
        return num_ways

    return helper(0) # bc we want to find out no. of ways to decode string starting at 0