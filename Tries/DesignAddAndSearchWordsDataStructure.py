# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
# MEDIUM
# Tags: trielc, dfslc, designlc, #211

# Design a data structure that supports adding new words and finding if a string matches any previously added string
# Implement the WordDictionary class:
    # WordDictionary() initializes the object.
    # addWord(word) Adds word to the data structure, it can be matched later.
    # search(word) Returns true if there is any string in the data structure that matches word or false otherwise
        # word may contain dots '.' where dots can be matched with any letter

# EXAMPLES:
    # Input
    # ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    # [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    # Output
    # [null,null,null,null,false,true,true,true]

    # Explanation
    # WordDictionary wordDictionary = new WordDictionary();
    # wordDictionary.addWord("bad");
    # wordDictionary.addWord("dad");
    # wordDictionary.addWord("mad");
    # wordDictionary.search("pad"); // return False
    # wordDictionary.search("bad"); // return True
    # wordDictionary.search(".ad"); // return True
    # wordDictionary.search("b.."); // return True

###########################################################################################################

# ✅ ALGORITHM: TRIES + DFS
# We need DFS for the search() function if there are dots "." in the word to be searched for

# TIME COMPLEXITY: O(n * l)
    # n = no. of words in trie
    # l = average length of word
# TIME COMPLEXITY: O(n * l) in the worst case where no words have common prefixes

class WordDictionary(object):
    def __init__(self):
        self.root = {}

    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['end'] = True

    def search(self, word):
        def dfs(idx, node): # idx is the starting index of the remaining portion of the word to search
            if idx == len(word):
                return "end" in node  # return true if we have reached the end of a word in trie

            char = word[idx]
            if char == ".":
                for child in node.values(): # for each child of the current node,
                    if child != True and dfs(idx+1, child): # Avoid treating "end" as a child node
                        # idx+1 means we move to the index of the next char
                        return True
                return False
            else:
                if char not in node:
                    return False
                return dfs(idx+1, node[char])

        return dfs(0, self.root)
    
# NOTE: for the line `if child != True and dfs(idx+1, child):`
    # when you have a word, "a", in trie, trie would look like:
        # root = {'a': {'end': True}}
    # When you're searching through it and you reach the node for 'a', one of the "children" is {'end': True}. But, when we're looking for matches (especially for wildcard characters like "."), we don't want to recurse into this "end" marker as if it's a valid character
        # So we check if the child is not equal to True to ensure we skip the "end" marker