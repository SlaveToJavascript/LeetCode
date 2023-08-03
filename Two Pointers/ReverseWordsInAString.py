# https://leetcode.com/problems/reverse-words-in-a-string/description/
# MEDIUM
# Tags: twopointerslc, #151

# GIVEN:
    # an input string, s

# TASK:
    # reverse the order of the words
    # Return a string of the words in reverse order concatenated by a single space
    # NOTE: s may contain leading or trailing spaces or multiple spaces between two words
    # The returned string should only have a single space separating the words

# EXAMPLES:
    # Input: s = "the sky is blue"
    # Output: "blue is sky the"

    # Input: s = "  hello world  "
    # Output: "world hello"
    # Explanation: Your reversed string should not contain leading or trailing spaces.

    # Input: s = "a good   example"
    # Output: "example good a"
    # Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

###########################################################################################################

# ✅✅✅ ALGORITHM 1: ONE LINER USING STRING / ARRAY MANIPULATION

# TIME COMPLEXITY: O(n)
    # reversing string requires O(n) time
# SPACE COMPLEXITY: O(n)
    # for the array of words created

def reverseWords(s):
    return ' '.join(s.split()[::-1])

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: TWO POINTERS

# TIME COMPLEXITY: O(n)
    # array is traversed twice -> O(n + n) ≈ O(n)
# SPACE COMPLEXITY: O(n)
    # at the start of the algorithm, we copy the string into a list of characters to overcome the issue of strings being immutable in Python

import re

def reverse_words(sentence):
    # remove leading, trailing and multiple spaces
    sentence = sentence.strip()
    # We need to convert the updated string to lists of characters as strings are immutable in Python
    sentence = list(sentence)
    n = len(sentence)

    #  We will first reverse the entire string.
    str_rev(sentence, 0, n - 1)

    #  Now all the words are in the desired location, but in reverse order: "Hello World" -> "dlroW olleH"

    start = 0
    end = 0

    # iterate the reversed string and reverse each word in place.
    # "dlroW olleH" -> "World Hello"
    while (start < n):
        # Find the end index of the word. 
        while end < n and sentence[end] != ' ':
            end += 1
        # call our helper function to reverse the word in-place.
        str_rev(sentence, start, end - 1)
        start = end + 1
        end += 1

    return ''.join(sentence)


# helper function that reverses a whole sentence character by character
def str_rev(_str, start_rev, end_rev):
   # Starting from the two ends of the list, and moving in towards the centre of the string, swap the characters
   while start_rev < end_rev:
       temp = _str[start_rev] # temp store for swapping
       _str[start_rev] = _str[end_rev] # swap step 1
       _str[end_rev] = temp # swap step 2


       start_rev += 1 # Move forwards towards the middle
       end_rev -= 1 # Move backwards towards the middle