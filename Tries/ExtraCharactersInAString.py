# 2707. Extra Characters in a String
# https://leetcode.com/problems/extra-characters-in-a-string/
# MEDIUM
# Tags: dplc, hashmaplc, trielc, #2707

# GIVEN:
    # a string, s
    # a dictionary of words, dictionary

# TASK:
    # You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary
        # There may be some extra characters in s which are not present in any of the substrings
    # Return the minimum number of extra characters left over if you break up s optimally

# EXAMPLES:
    # Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
    # Output: 1
    # Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

    # Input: s = "sayhelloworld", dictionary = ["hello","world"]
    # Output: 3
    # Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.

###########################################################################################################

# ✅ ALGORITHM 1: DYNAMIC PROGRAMMING (RECURSIVE, TOP DOWN) WITH MEMOIZATION
# dp(start) returns the min. no. of leftover chars by breaking up substring s[start:]
    # i.e. start is the starting index of the substring of s
# NOTE: even if a char in s is part of a substring of s that is a word in dictionary, we might still choose to skip that char as the min. no. of leftover chars as a result of skipping this char might be greater
    # e.g. s = "abcdef", dictionary = ["abc", "bcdef"]
        # if we match the 1st 3 chars of s ("abc") with the dictionary word "abc", we'll skip "def" in s -> result = 3 ❌
        # BUT, if we skip the 1st char of s ("a") and match substring "bcdef" with the dictionary word "bcdef", result = 1 ✅
# Steps:
    # Iterate through each char in s
    # At each char in s, initiate result = result if we skip current char (i.e. result = 1 + result for substring with starting index = start+1)
    # nested for-loop iterates over each char after current char (this will be the ending index of the susbtring of s)
        # if substring s[start]...s[end] is a word in dictionary, update result = the minimum between previously initialized result (i.e. result if we skip char at index start) VS result if we didn't skip char
            # since s[start]...s[end] is a word in dictionary, result if we didn't skip char = result if start index become the next char after end index
    # return result

# TIME COMPLEXITY: O(n^3)
    # dp(start) will be called max n times, since start = 0 to n
    # within each dp() call, there is a for-loop that loops up to n times
    # within each iteration of the for-loop within each dp() call, we are checking if the substring s[start]...s[end] is in dictionary -> O(n)
    # -> overall TC = O(n^3)
# SPACE COMPLEXITY: O(n)
    # O(n) for recursive call stack
    # O(n) for memoization (cache)

from functools import cache

def minExtraChar(s, dictionary):
    words = set(dictionary) # convert array dictionary into set so lookup time = O(1)

    @cache # @cache decorator automatically caches and maps each value of start (key) -> return value
    def dp(start): # returns the min. no. of leftover chars, where start is starting index of substring of s
        if start == len(s): # if index is out of bounds
            return 0
        
        result = 1 + dp(start+1) # result if we skip current char (at index start)
        for end in range(start, len(s)): # iterate every char after and incl. start char to get substring from start to end indexes
            if s[start : end+1] in words: # if substring s[start]...s[end] is in dictionary,
                result = min(result, dp(end+1)) # take the minimum between result if we skip char at start index VS result if we don't skip char at start index
                    # since substring s[start]...s[end] is in dictionary, result if we don't skip char at start index = result if starting index is the char after end index
        
        return result
    
    return dp(0)

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: TRIE
# Use a trie to implement the above solution so that we would not need the line "if s[start : end+1] in words:" which takes O(n) time, reducing the overall time from O(n^3) for the above solution to O(n^2) for this trie solution
# In this trie solution, we are building a trie using dictionary words, then checking if each character in s is a node in the trie, not checking the whole substring

# TIME COMPLEXITY: O(n^2)
    # dp(start) will be called max n times, since start = 0 to n
    # within each dp() call, there is a for-loop that loops up to n times
    # -> overall TC = O(n^2)
# SPACE COMPLEXITY: O(n)
    # O(n) for recursive call stack
    # O(n) for memoization (cache)

from functools import cache

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False

class Trie:
    def __init__(self, dictionary):
        self.root = TrieNode()

        for word in dictionary:
            curr = self.root # start inserting each word into root of trie
            for char in word:
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    curr.children[char] = TrieNode()
                    curr = curr.children[char]
            curr.isWordEnd = True # mark current char as end of word

class Solution:
    def minExtraChar(self, s, dictionary):
        root = Trie(dictionary).root # root of trie constructed from dictionary words

        @cache
        def dp(start):
            if start == len(s):
                return 0 # start is out of bounds of s
            
            result = 1 + dp(start+1) # result if we skip current char (at index start)
            curr = root
            for end in range(start, len(s)): # iterate each char after/incl. start index
                if s[end] not in curr.children: # unable to match curr char to any word in dictionary
                    break
                # else, if s[end] in curr.children,
                curr = curr.children[s[end]] # move curr pointer to end char
                
                if curr.isWordEnd: # if current trie node is the end of a word
                    result = min(result, dp(end+1)) # update result = minimum between result if curr char (at start index) is ignored VS result if curr char (at start index) is not ignored
                        # since substring s[start]...s[end] is a valid dictionary word in trie, result if we don't skip char at start index = result if starting index is the char after end index
            
            return result

        return dp(0)