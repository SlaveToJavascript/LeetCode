# https://leetcode.com/problems/longest-common-prefix/
# EASY
# Tags: trielc, #14

# GIVEN:
    # an array of strings, strs

# TASK:
    # find and return the longest common prefix string amongst the array of strings
    # If there is no common prefix, return an empty string ""

# EXAMPLES:
    # Input: strs = ["flower","flow","flight"]
    # Output: "fl"

    # Input: strs = ["dog","racecar","car"]
    # Output: ""
    # Explanation: There is no common prefix among the input strings.

###########################################################################################################

# ✅ ALGORITHM 1: DOUBLE FOR-LOOP
# Get the minimum length amongst all strings in the array
# result = empty string
# For each char i in minimum length, check if each string has the same char at index i
    # if any char does not have the same string at i, return existing result
# after iterating through all words, if all words have the same char at i, add the char to result
# return result

# TIME COMPLEXITY: O(n * m)
    # n = no. of words
    # m = min. length of words
    # since we need to iterate through all words and check all chars in each word
# SPACE COMPLEXITY: O(1)

def longestCommonPrefix(strs):
    min_len = len(min(strs, key=len)) # minimum length amongst all strings in array
    result = "" # return

    for i in range(min_len):
        for word in strs: # for each word in array,
            if word[i] != strs[0][i]: # if current word's char at i is not the same as the other chars,
                return result # return existing result
        result += word[i] # if all words have the same char at i, add char to result
    
    return result

#==========================================================================================================

# ✅ ALGORITHM 2: TRIE
# Construct trie tree from all words in strs array
# To get common prefix of trie, keep checking if current trie node has only 1 child and current trie char is not last char in word -> if yes, add current trie char to result
    # if any trie node has more than 1 child, it means 1 or more of the words have different chars at the same index -> current char is no longer part of prefix
# return result

# TIME COMPLEXITY: O(n * w)
    # n = no. of words
    # w = max. length of word
    # when constructing trie tree, we are adding every char of every word to trie -> worst case: there are no common prefixes -> each char in each word is a separate node in trie
        # therefore we are visiting each char of each word once
# SPACE COMPLEXITY: O(n * w)
    # worst case: there are no common prefixes -> each char in each word is a separate node in trie -> there are n*w nodes in trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()

        # construct trie from each word in words array
        for word in words:
            curr = self.root
            for char in word:
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    curr.children[char] = TrieNode()
                    curr = curr.children[char]
            curr.isWord = True

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if "" in strs:
            return ""
            
        trie = Trie(strs)
        curr = trie.root
        result = "" # return
        
        while len(curr.children) == 1 and not curr.isWord: # while current node has only 1 child and is not end of word,
            char = curr.children.keys()[0] # get current char
            result += char # since parent node has only 1 child which is current char, add current char to result
            curr = curr.children[char] # shift curr pointer to current char node
        
        return result