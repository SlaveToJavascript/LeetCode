# https://leetcode.com/problems/number-of-matching-subsequences/description/
# MEDIUM
# Tags: hashmaplc, google, #792

# GIVEN:
    # a string, s
    # an array of strings, words

# TASK:
    # return the number of words[i] that is a subsequence of s
    # A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters
        # e.g. "ace" is a subsequence of "abcde"

# EXAMPLES:
    # Input: s = "abcde", words = ["a","bb","acd","ace"]
    # Output: 3
    # Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

    # Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
    # Output: 2

###########################################################################################################

# ❌ ALGORITHM 1: TWO POINTERS + BRUTE FORCE (TLE)
# For each word in words,
    # maintain 2 pointers, 1 for the current word, 1 for s
    # shift both pointers forward if the current char in word matches current char in s, else shift only s pointer forward
# return the no. of words in words array that are subsequences of s

# TIME COMPLEXITY: O(n * m) 👎
    # n = no. of words in words array, m = length of s

def numMatchingSubseq(s, words):
    count = 0

    for word in words:
        word_pointer = 0 # pointer for current word
        s_pointer = 0 # pointer for s

        while word_pointer < len(word) and s_pointer < len(s):
            if word[word_pointer] == s[s_pointer]:
                word_pointer += 1
                s_pointer += 1
            else:
                s_pointer += 1
        
        if word_pointer == len(word):
            count += 1
    
    return count

###########################################################################################################

# ✅ ALGORITHM 2: HAHSMAP
# store all the indexes of each character of s in a hashmap
    # e.g. if s = 'abcded', indexes = {'a': [0], 'b': [1], 'c': [2], 'd': [3,5], 'e':[4]}
    # How will this help? When we are checking for sequences, we can directly check based on increasing indexes

# TRUE EXAMPLE: if word = acded
    # we can maintain a variable called curr_pos = -1,
    # Now, we look for position of 'a' -> pos = 0, curr_pos -1 < pos 0, so curr_pos = pos = 0
    # Then, we look for position of 'c' -> pos = 2, curr_pos 0 < pos 2, curr_pos = pos = 2
    # Then, we look for position of 'd' -> pos = 3 (we choose from left to right), curr_pos 2 < pos 3, curr_pos = pos = 3
    # Then, we look for position of 'e' -> pos = 4, curr_pos 3 < pos 4, curr_pos = pos = 4
    # Then, we look for position of 'd' -> pos = 3 (we choose from left to right), curr_pos >= pos
        # is there any other position of 'd'? -> Yes, pos = 5, now curr_pos 4 < pos 5, so curr_pos = pos = 5
    # Now, we have found all the characters in word in the indexes hashmap, and in increasing order of their indexes. Hence return true

# FALSE EXAMPLE: if word = bb
    # curr_pos = -1
    # Then, we look for position of 'b' -> pos = 1, curr_pos -1 < pos 1, curr_pos = pos = 1
    # Then, we look again for position of second 'b', pos = 1, curr_pos 1 >= pos 1, is there any other position of b? -> NO, so we did not find the desired subsequence
    # Hence return False

# Binary search on indexes:
# E.g.: we are looking for 'c' in indexes hashmap and curr_pos = 3, and indexes[c] = [1,2,4,6]
    # Here the correct position to insert curr_pos = 3 would be the index 2 with value 4. Such that it becomes [1,2,3,4,6]
        # but wait... we are not going to insert. we just want the index, once we got the index, we can choose that element and make it pos, now curr_pos 3 < pos 4, so we can update the curr_pos = pos = 4
    # bisect_right performs binary search and gives us the last occurance of element '<=x' + 1 in a sorted array
        # we have used bisect_right here as we want the greater element (i.e. 4 instead of 2)

# TIME COMPLEXITY: O(m log n)
    # m = length of s
    # n = no. of words in words array
# SPACE COMPLEXITY: O(n)
    # for indexes hashmap

from bisect import bisect_right

def numMatchingSubseq(s, words):
    # create indexes hashmap for s where key = each char in s and value = the index(es) of the char in s
    indexes = {}
    for i, char in enumerate(s):
        if char not in indexes:
            indexes[char] = [i]
        else:
            indexes[char].append(i)

    def isSubsequence(word):
        curr_pos = -1

        for char in word:
            if char in indexes:
                pos = bisect_right(indexes[char], curr_pos)
                if pos == len(indexes[char]): # if there are no elements in indexes[i] that are greater than curr_pos,
                    return False # current word is not subsequence
                curr_pos = indexes[char][pos] # update curr_pos to element at pos in indexes[char]
            else: # if current char is not in s
                return False # current word is not subsequence
        
        return True # if we reached this line, that means False has not been returned and current word is subsequence of s
    
    count_subsequences = 0 # return value
    for word in words:
        if isSubsequence(word):
            count_subsequences += 1
    
    return count_subsequences