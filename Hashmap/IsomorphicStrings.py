# https://leetcode.com/problems/isomorphic-strings
# EASY

# GIVEN: 
    # 2 strings, s and t

# TASK:
    # determine if they are isomorphic
        # Isomorphic = if the characters in s can be replaced to get t
    # All occurrences of a character must be replaced with another character while preserving the order of characters
    # No two characters may map to the same character, but a character may map to itself
    # NOTE: len(s) == len(t)

# RETURN:
    # Boolean (True if isomorphic, False otherwise)

# EXAMPLES:
    # Input: s = "egg", t = "add"
    # Output: true

    # Input: s = "foo", t = "bar"
    # Output: false

    # Input: s = "paper", t = "title"
    # Output: true

###########################################################################################################

# ✅ ALGORITHM: HASHMAP
# in a hashmap, maintain the mappings of chars in s to the corresponding char in t
# for each char in s, add it to the hashmap, mapped to the respective char in the SAME INDEX of t
# if any char in s has been previously added to the hashmap mapped to a certain char in t but is now not mapped to that same char in t, return False
# check if there are any duplicates in hashmap values
    # if there are, return False as it means there are 2 chars in s mapped to the same char in t

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def isIsomorphic(s, t):
    hm = {}

    for idx, char in enumerate(s):
        if char in hm:
            if hm[char] != t[idx]:
                return False
        else:
            hm[char] = t[idx]
    
    return len(hm.values()) == len(set(hm.values())) # ensures there are no duplicates in the values of hm
                                                    # i.e. no 2 characters are mapped to the same char