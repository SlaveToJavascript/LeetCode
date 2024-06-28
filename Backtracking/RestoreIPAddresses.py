# 93. Restore IP Addresses
# https://leetcode.com/problems/restore-ip-addresses/
# MEDIUM
# Tags: backtracklc, #93

# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

# EXAMPLES:
    # Input: s = "25525511135"
    # Output: ["255.255.11.135","255.255.111.35"]

    # Input: s = "0000"
    # Output: ["0.0.0.0"]

    # Input: s = "101023"
    # Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

###########################################################################################################

# ✅ ALGORITHM: BACKTRACKING
    # https://youtu.be/61tN4YEdiTM?si=rvx7XauUdy8IGwz1&t=324
# iterate s, checking each 1-char, 2-char and 3-char string group in s
    # let start of each string group be "start", let end of each string group be "end"
# if the group is valid, concatenate it to the current IP address + "." at the back
# once there are 4 dots and we reach the end of the string, we have a valid IP address -> add it to result
    # NOTE: the final result should only have 3 dots, so we remove the dot at the end when adding to results array
# however, if there are more than 4 dots or "start" is greater than length of string, we backtrack

# TIME COMPLEXITY: O(m^n * n)
    # Let's assume we need to separate the input string into n integers, each integer is at most m digits
        # in this case, m = 3, n = 4, so TC = O(1)
    # there are at most m^(n-1) possibilities, and for each possibility, checking whether all parts are valid takes O(m*n) time, so the final time complexity is O(m^(n-1)) * O(m*n) = O(m^n * n)
# SPACE COMPLEXITY: O(m*n)
    # For each possibility, we save n-1 numbers (the number of digits before each dot) which takes O(n) space
    # And we need temporary space to save a solution before putting it into the answer list
    # The length of each solution string is M⋅N+M−1 = O(M⋅N), so the total space complexity is O(M⋅N) if we don't take the output space into consideration
    # For this question, M = 3, N = 4, so the space complexity is O(1).

def restoreIpAddresses(s):
    result = []

    if len(s) > 12: # if length of s > 12, we know it's impossible for s to be a valid IP address (since there can be at most 4 groups of 3 digits)
        return result

    def backtrack(start, dots, currIp): # start = index of string that we're at, dots = how many dots inserted, currIp = the IP address we're currently building
        if dots == 4 and start == len(s): # NOTE: the final result should only have 3 dots, so we remove the dot at the end when adding to results array
            result.append(currIp[:-1]) # remove last dot
            return
        
        if dots > 4 or start >= len(s): # invalid IP address
            return
        
        for end in range(start, min(start+3, len(s))): # explore each group of 1-char, 2-char and 3-char strings in s, starting from "start"
            if int(s[start:end+1]) <= 255 and (start == end or s[start] != "0"): # if current string group <= 255 and does not start with "0",
                backtrack(end+1, dots+1, currIp+s[start:end+1] + ".") # concatenate string group to currIp and add a "."

    backtrack(0, 0, "")

    return result