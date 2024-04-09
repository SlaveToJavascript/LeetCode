# 186. Reverse Words in a String II
# https://leetcode.com/problems/reverse-words-in-a-string-ii
# MEDIUM
# Tags: twopointerslc, stringlc, #186

# GIVEN:
    # a character array, s

# TASK:
    # reverse the order of the words
        # A word is defined as a sequence of non-space characters. The words in s will be separated by a single space
    # NOTE: Your code must solve the problem in-place, i.e. without allocating extra space

# EXAMPLES:
    # Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    # Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

    # Input: s = ["a"]
    # Output: ["a"]

###########################################################################################################

# ✅ ALGORITHM: REVERSE ENTIRE STRING, THEN REVERSE EACH WORD USING 2 POINTERS
# reverse entire array s
# then reverse each word in s, in-place (each word is separated by a space in between)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def reverseWords(s):
    s.reverse() # reverse entire array s

    l = 0 # l = start of word
    for r in range(len(s)):
        if s[r] == " " or r == len(s)-1: # if char at r is a space or r is the last char in array s,
            if r == len(s)-1:
                r += 1 # due to 0-based indexing, if r points to the last char in array s, r+1 is the correct exclusive indexing for an array slicing operation where s[r] is the last char in the slice
            s[l:r] = s[l:r][::-1] # this operation replaces the chars of the slice s[l:r] with the reversed chars of the slice s[l:r]
            l = r+1 # shift l to become the starting index of the next word to reverse