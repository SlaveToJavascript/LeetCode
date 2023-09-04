# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# HARD
# Tags: slidingwindowlc, #30

# GIVEN:
    # a string, s
    # an array of strings, words
        # All the strings of words are of the same length

# TASK:
    # A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated
        # e.g. if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings
        # "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words
    # TODO: Return the starting indices of all the concatenated substrings in s
        # You can return the answer in any order

# EXAMPLES:
    # Input: s = "barfoothefoobarman", words = ["foo","bar"]
    # Output: [0,9]
    # Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
    # The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
    # The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
    # The output order does not matter. Returning [9,0] is fine too.

    # Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
    # Output: []
    # Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
    # There is no substring of length 16 in s that is equal to the concatenation of any permutation of words.
    # We return an empty array.

    # Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
    # Output: [6,9,12]
    # Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
    # The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
    # The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
    # The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.

###########################################################################################################

# ❌ ALGORITHM 1: CHECK EVERY SUBSTRING

def findSubstring(s, words):
    def isValidSubstring(substring, words, n): # returns True if substring is a valid combination of words array
        l = 0
        for r in range(n-1, len(substring), n):
            if substring[l:r+1] in words:
                words.remove(substring[l:r+1])
                l = r+1
            else:
                return False
        return True

    n = len(words[0]) * len(words)
    if len(s) < n:
        return []

    n_word = len(words[0])
    result = []
    l, r = 0, n-1
    while r < len(s):
        if isValidSubstring(s[l:r+1], words[:], n_word):
            result.append(l)
        l += 1
        r = l + n-1

    return result