# https://leetcode.com/problems/group-anagrams/description/
# MEDIUM
# Tags: hashmaplc, #49

# GIVEN:
    # an array of strings, strs

# TASK:
    # group the anagrams together
        # anagram = word/phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once
    # You can return the answer in any order

# EXAMPLES:
    # Input: strs = ["eat","tea","tan","ate","nat","bat"]
    # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    # Input: strs = [""]
    # Output: [[""]]

    # Input: strs = ["a"]
    # Output: [["a"]]

###########################################################################################################

# ✅ ALGORITHM 1: USE SORTED WORD AS HASHMAP KEY
# Iterate strs array
# for each word, get the sorted version of the word (i.e. sorted alphabetically) and use the sorted word as a key in hashmap
    # value of each key in hashmap = array of anagrams
# return all values (arrays) in hashmap

# TIME COMPLEXITY: O(n * wlogw)
    # n = length of strs array
    # w = average length of word
    # we take O(n) time to iterate each word in strs array
    # for each word, we sort the chars in word -> O(w log w) time
# SPACE COMPLEXITY: O(n * w)
    # hashmap stores n strings (sorted words), each of length w -> O(nw)
    # sort() function takes O(w) space

from collections import defaultdict

def groupAnagrams(strs):
    sorted_to_word = defaultdict(list) # hashmap of sorted words to array of corresponding words
    
    for word in strs:
        sorted_word = ''.join(sorted(word)) # sorted() sorts word alphabetically and returns an array -> use join() to get sorted word string
        sorted_to_word[sorted_word].append(word) # add word to hashmap value (array of anagrams) under sorted_word key
    
    return sorted_to_word.values() # return all values (arrays) in hashmap

#==========================================================================================================

# ✅ ALGORITHM 2: USE CHAR COUNTS ARRAY AS KEY OF HASHMAP (NO SORTING NEEDED)
# Since each char in each word is 1 of 26 alphabets (lowercase a-z), we can use an array to represent counts of each char in word
    # the array will have 26 elements initialized to 0, where the 0th element = count of "a" in word, 1st element = count of "b" in word, and so on...until 25th element = count of "z" in word
# we use this array (converted to tuple) to be key in hashmap, while value = array of corresponding anagrams
# return all hashmap values

# TIME COMPLEXITY: O(n * w)
    # n = length of strs array
    # w = average length of word
    # we take O(n) time to iterate each word in strs array
    # for each word, we traverse each char in word -> O(w) time
# SPACE COMPLEXITY: O(n * w)
    # for hashmap

from collections import defaultdict

def groupAnagrams(strs):
    result = defaultdict(list) # map char_count array (tuple) -> array of anagram words

    for word in strs:
        char_count = [0] * 26 # 1 count for each a-z
        
        for char in word:
            # map each char to corresponding index in char_count, i.e. a -> 0, z -> 25, etc.
            char_count[ord(char) - ord('a')] += 1 # e.g. ord(z) - ord(a) = 25, ord(b) - ord(a) = 1, etc.
        
        result[tuple(char_count)].append(word) # since array cannot be hashmap keys, convert char_count array to tuple; add anagram to corresponding value (array)
    
    return result.values()