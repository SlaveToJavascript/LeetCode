# 833. Find And Replace in String
# https://leetcode.com/problems/find-and-replace-in-string/description/
# MEDIUM
# Tags: stringlc, #833

# GIVEN:
    # string s that you must perform k replacement operations on
    # replacement operations are given as 3 parallel arrays: indices, sources, and targets, all of length k

# TASK:
    # To complete the i'th replacement operation:
        # 1. Check if the substring sources[i] occurs at index indices[i] in the original string s
        # 2. If it does not occur, do nothing
        # 3. Otherwise if it does occur, replace that substring with targets[i]
            # e.g. if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd"
    # All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other (the testcases will be generated such that the replacements will not overlap)
    # TODO: Return the resulting string after performing all replacement operations on s

# EXAMPLES:
    # Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
    # Output: "eeebffff"
    # Explanation:
    # "a" occurs at index 0 in s, so we replace it with "eee".
    # "cd" occurs at index 2 in s, so we replace it with "ffff".

    # Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
    # Output: "eeecd"
    # Explanation:
    # "ab" occurs at index 0 in s, so we replace it with "eee".
    # "ec" does not occur at index 2 in s, so we do nothing.

###########################################################################################################

# ✅ ALGORITHM: REPLACE FROM BACK TO FRONT + ZIP FUNCTION
# MAIN IDEA: sort the indices, sources and targets arrays in DESCENDING ORDER of indices, then do the replacements
    # this ensures that making a replacement will not affect the positions of earlier replacements since you're modifying the string from back to front -> avoids interference among replacements

def findReplaceString(s, indices, sources, targets):
    sorted_replacements = sorted(zip(indices, sources, targets), reverse=True)

    for i, src, tgt in sorted_replacements:
        if s[i:].startswith(src): # only replace if the source matches substring starting at index i
            s = s[:i] + tgt + s[i + len(src):] # tgt is the string that replaced src
    
    return s