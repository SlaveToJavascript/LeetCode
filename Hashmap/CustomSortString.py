# 791. Custom Sort String
# https://leetcode.com/problems/custom-sort-string/description/
# MEDIUM
# Tags: hashmaplc, #791

# GIVEN:
    # 2 strings, order and s
        # all the chars of order are unique and were sorted in some custom order previously

# TASK:
    # Permute the characters of s so that they match the order that order was sorted
        # i.e. if a character x occurs before a character y in order, then x should occur before y in the permuted string
    # Return any permutation of s that satisfies this property

# EXAMPLES:
    # Input:  order = "cba", s = "abcd" 
    # Output:  "cbad" 
    # Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
    # Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

    # Input:  order = "bcafg", s = "abcd" 
    # Output:  "bcad" 
    # Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.
    # Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like "bacd" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.

###########################################################################################################

# ✅ ALGORITHM: HASHMAP

from collections import Counter

def customSortString(order, s):
    s_hm = Counter(s) # char : frequency
    result = ""
    for char in order:
        if char in s_hm and s_hm[char] > 0:
            result += s_hm[char] * char
            s_hm[char] = 0

    # check for remaining chars in s that are not added to result yet
    for char in s_hm:
        if s_hm[char] > 0:
            result += s_hm[char] * char
    
    return result