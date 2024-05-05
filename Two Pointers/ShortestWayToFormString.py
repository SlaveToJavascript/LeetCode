# 1055. Shortest Way to Form String
# https://leetcode.com/problems/shortest-way-to-form-string/
# MEDIUM
# Tags: twopointerslc, premiumlc, #1055

# GIVEN:
    # 2 strings, source and target

# TASK:
    # return the minimum number of subsequences of source such that their concatenation equals target
        # A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters
            # i.e., "ace" is a subsequence of "abcde" while "aec" is not)
    # If the task is impossible, return -1

# EXAMPLES:
    # Input: source = "abc", target = "abcbc"
    # Output: 2
    # Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

    # Input: source = "abc", target = "acdbc"
    # Output: -1
    # Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.

    # Input: source = "xyz", target = "xzyxz"
    # Output: 3
    # Explanation: The target string can be constructed as follows "xz" + "y" + "xz".

###########################################################################################################

# ✅ ALGORITHM: TWO POINTERS
# main idea: we can iterate through source string as many times as needed, but we only iterate through target string once
# use 2 pointers, 1 for source and 1 for target
# if char in source = char in target, both pointers +1 each
# else if chars are different, only the pointer for source +1
# if pointer for source is at the end of source string, reset pointer to 0 and result+1
# if at any point in time, char at target is not found in source, return -1 (impossible for target to be formed from subsequences of source)

def shortestWay(source, target):
    s = t = 0 # s pointer for source, t pointer for t
    result = 0 # return value

    while t < len(target):
        if s == len(source): # if pointer s reaches the end of source string, reset it to 0 and result+1
            s = 0
            result += 1
        
        if target[t] not in source:
            return -1
        
        if source[s] == target[t]:
            s += 1
            t += 1
        else:
            s += 1
    
    result += 1 # for the last subsequence of source
        # e.g. if source = "abc" and target = "abcbc", we need to do result+1 for "bc" which is the 2nd (and last) subsequence of source that is found in target
    
    return result