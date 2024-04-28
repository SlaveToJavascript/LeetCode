# 249. Group Shifted Strings
# https://leetcode.com/problems/group-shifted-strings/
# MEDIUM
# Tags: hashmaplc, premiumlc, #249

# We can shift a string by shifting each of its letters to its successive letter.
    # For example, "abc" can be shifted to be "bcd".
# We can keep shifting the string to form a sequence.
    # For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
# GIVEN: an array, strings, group all strings[i] that belong to the same shifting sequence
    # You may return the answer in any order.

# EXAMPLES:
    # Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
    # Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

    # Input: strings = ["a"]
    # Output: [["a"]]

###########################################################################################################

# ✅ ALGORITHM: HASHMAP WITH KEY = TUPLE OF ASCII DIFFERENCES
# MAIN IDEA: for 2 strings to have the same shifting sequence, each string needs to have the same ASCII differences between each chars
    # e.g. string1 = "abd", string2 = "bce"
        # ASCII differences of string1 ("abd") = (1,2)
            # i.e. ascii("b") - ascii("a") = 1, ascii("d") - ascii("b") = 2
        # ASCII differences of string2 ("bce") = (1,2)
            # i.e. ascii("c") - ascii("b") = 1, ascii("e") - ascii("c") = 2
        # therefore, "abd" and "bce" have the same shifting sequences
# use a tuple of ASCII differences (e.g. (1, 2, 4), etc.) as keys in hashmap -> every string with the same shifting sequence will be added to its value

# TIME COMPLEXITY: O(n * k)
    # n = no. of strings in strings array
    # k = maximum length of a string in strings array
    # in the outer for-loop, we iterate each string in strings array; in the inner for-loop, we iterate each char in each string -> n*k complexity
# SPACE COMPLEXITY: O(n)
    # worst case: each string in strings array has a different shifting sequence -> there will be n keys in hashmap

from collections import defaultdict

def groupStrings(strings):
    hashmap = defaultdict(list)

    for string in strings:
        hashmap_key = () # tuple
        
        for i in range(1, len(string)): # calculate the difference in ASCII values between each adjacent character pairs in string
            ascii_difference = (ord(string[i]) - ord(string[i-1])) % 26
            hashmap_key += (ascii_difference,) # NOTE: the comma is necessary to make this a tuple data type instead of an integer
        
        hashmap[hashmap_key].append(string) # if hashmap_key alr exists in hashmap, this adds string to hashmap_key; else, this creates a new hashmap_key in hashmap
    
    return hashmap.values()