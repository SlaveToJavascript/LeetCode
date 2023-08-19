# https://leetcode.com/problems/implement-trie-prefix-tree/description/
# MEDIUM
# Tags: trielc, designlc, #208

# A trie or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings
# There are various applications of this data structure, such as autocomplete and spellchecker

# Implement the Trie class:
    # Trie() Initializes the trie object.
    # insert(String word) Inserts the string word into the trie.
    # search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    # startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

# EXAMPLES:
    # Input
    # ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    # [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    # Output
    # [null, null, true, false, true, null, true]

    # Explanation
    # Trie trie = new Trie();
    # trie.insert("apple");
    # trie.search("apple");   // return True
    # trie.search("app");     // return False
    # trie.startsWith("app"); // return True
    # trie.insert("app");
    # trie.search("app");     // return True

###########################################################################################################

# ✅ ALGORITHM: TRIE
# TrieNode is a node of the Trie tree, while Trie is the overall tree itself

class TrieNode():
    def __init__(self):
        self.children = {} # hashmap of 26 possible children; key = character, value = TrieNode for this character
        self.isEnd = False # boolean to indicate if this character (child) is the end of a word
    
class Trie():
    def __init__(self):
        self.root = TrieNode() # create root node
    

    
    # TIME COMPLEXITY of insert(): O(n), where n = length of word
        # since we need to perform n iterations to finish inserting word into trie
    # SPACE COMPLEXITY of insert(): O(n), where n = length of word
        # since n new trie nodes are added
    def insert(self, word): # insert word into trie
        curr = self.root # pointer starting from root node, since we'll be inserting chars at root node
        
        for char in word: # for each char in word
            if char in curr.children:
                curr = curr.children[char] # move curr to point to the node of current char (child)
            else: # if char is not a child of curr
                curr.children[char] = TrieNode() # create a new node for this char
                curr = curr.children[char] # move curr to point to this new char node
        
        # at this point, curr is pointing to the trie node of the last char
        curr.isEnd = True # set isEnd to True to indicate that this char is the end of a word
    


    # TIME COMPLEXITY of search(): O(n), where n = length of word
        # since we need to travel down the length of the word
    def search(self, word): # search for word in trie
        curr = self.root # pointer starting from root node, since we'll be searching for word from root

        for char in word:
            if char in curr.children: # if char is a child of current node,
                curr = curr.children[char] # move curr pointer to this char node to continue search
            else: # if char is not a child of current node,
                return False # word does not exist in trie
        
        # at this point, all chars in word exist in trie
        # curr now points to the node of the last char in word
        return curr.isEnd # return True if this char is the end of a word, else return False



    # TIME COMPLEXITY of startsWith(): O(n), where n = length of prefix
        # since we need to travel down the length of the prefix
    def startsWith(self, prefix): # search for existence of words starting with prefix in trie
        curr = self.root # pointer starting from root node, since we'll be searching for prefix from root

        for char in prefix:
            if char in curr.children: # if char is a child of current node,
                curr = curr.children[char] # move curr pointer to this char node to continue search
            else: # if char is not a child of current node,
                return False # prefix does not exist in trie
        
        # at this point, all chars in prefix exist in trie
        # curr now points to the node of the last char in prefix
        return True # return True since prefix exists in trie