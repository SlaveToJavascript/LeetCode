# 616. Add Bold Tag in String
# https://leetcode.com/problems/add-bold-tag-in-string/
# MEDIUM
# Tags: intervalslc, premiumlc, #616

# GIVEN:
    # a string, s
    # an array of strings, words

# TASK:
# You should add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in words.
    # If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag.
    # If two substrings wrapped by bold tags are consecutive, you should combine them.
# Return s after adding the bold tags.

# EXAMPLES:
    # Input: s = "abcxyz123", words = ["abc","123"]
    # Output: "<b>abc</b>xyz<b>123</b>"
    # Explanation: The two strings of words are substrings of s as following: "abcxyz123".
    # We add <b> before each substring and </b> after each substring.

    # Input: s = "aaabbb", words = ["aa","b"]
    # Output: "<b>aaabbb</b>"
    # Explanation: 
    # "aa" appears as a substring two times: "aaabbb" and "aaabbb".
    # "b" appears as a substring three times: "aaabbb", "aaabbb", and "aaabbb".
    # We add <b> before each substring and </b> after each substring: "<b>a<b>a</b>a</b><b>b</b><b>b</b><b>b</b>".
    # Since the first two <b>'s overlap, we merge them: "<b>aaa</b><b>b</b><b>b</b><b>b</b>".
    # Since now the four <b>'s are consecutive, we merge them: "<b>aaabbb</b>".

###########################################################################################################

# ✅ ALGORITHM: MARK BOLD CHARS USING BOOLEAN ARRAY
    # https://youtu.be/WXb3ItOlRfQ?si=YJY6qK-vSc-Iaxld&t=241
# Use a boolean array, to_bold, where to_bold[i] is True if s[i] needs to be bolded, or False if otherwise
# after filling up this boolean array, we can identify contiguous groups of "True" and bold them
# NOTE: why is the outer for-loop iterating words array instead of string s?
    # ✅ By iterating over words, we handle each word independently, ensuring that even if words overlap or are part of different patterns, they are all considered
    # ✅ Words may overlap or appear in different parts of the string. By iterating over each word, you ensure that all occurrences are found, regardless of their positions or overlaps
    # ❌ Iterating over s and checking for each word at every position can be redundant and inefficient. You would end up checking each substring of s against all words, leading to a lot of unnecessary comparisons

# TIME COMPLEXITY: O(w * s)
    # s = len(s)
    # w = no. of words in words array
    # l = average length of a word
    # technically it should be O(w * (s+l)), since outer for-loop ("for word in words") takes O(w) time, while-loop iterating s takes O(s) time and "to_bold[start : start+len(word)] = [True] * len(word)" takes O(l) time; these last 2 loops are both in O(w) loop -> TC = O(w * (s+l))
    # BUT l is usually always less than s (since l = length of a word in s), so we can disregard l in the equation -> TC = O(w * s)
# SPACE COMPLEXITY: O(n)
    # for to_bold array

def addBoldTag(s, words):
    to_bold = [False] * len(s)

    for word in words: # iterate over each word in words
        start = 0 # start searching from beginning of string s
        while start < len(s):
            start = s.find(word, start) # find start position of current word in string s starting from 'start'
            if start == -1: # if word is not found,
                break # break the while-loop
            to_bold[start : start+len(word)] = [True] * len(word) # Mark positions corresponding to the found word as True in to_bold
            start += 1 # Move start to the next position to find overlapping occurrences
    
    string_builder = []
    i = 0
    while i < len(s):
        if to_bold[i]:
            string_builder.append("<b>")

            while i < len(s) and to_bold[i]:
                string_builder.append(s[i])
                i += 1
            
            string_builder.append("</b>")
        else:
            string_builder.append(s[i])
            i += 1
        
    return ''.join(string_builder)