# https://leetcode.com/problems/replace-words/description/
# MEDIUM
# Tags: trieslc, #648

# GIVEN:
    #  a dictionary consisting of many roots
    # a sentence consisting of words separated by spaces

# TASK:
    # replace all the words in the sentence with the root forming it
    # If a word can be replaced by more than one root, replace it with the root that has the shortest length
    # Return the sentence after the replacement

# EXAMPLES:
    # Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
    # Output: "the cat was rat by the bat"

    # Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
    # Output: "a a b c"

###########################################################################################################

# ✅ ALGORITHM 1: FIND PREFIXES
# convert dictionary to a set
# For each word in sentence,
    # first initiate root_found as False
        # if a root is found in dictionary for this word, root_found will be True
    # get all prefixes that can be formed from word and check if this prefix is found in dictionary
        # if found, append this root to output array, mark root_found = True and break out of loop
    # if all prefixes are not found in dictionary, append the word itself to output
# return the output as a string joined by spaces

# TIME COMPLEXITY: O(n*m)
    # n = no. of words in sentence
    # m = average length of word in sentence

def replaceWords(dictionary, sentence):
    output = []
    roots = set(dictionary)

    for word in sentence.split(' '):
        root_found = False
        for i in range(1, len(word)):
            if word[:i] in roots: # if prefix in root words
                output.append(word[:i]) # add root to output
                root_found = True
                break
        if not root_found:
            output.append(word)
    
    return " ".join(output)

#==========================================================================================================

# ✅ ALGORITHM 2: TRIE

# TIME COMPLEXITY: O(n)
    # n = length of sentence
    # Every query of a word is in linear time
# SPACE COMPLEXITY: O(n)
    # this is the size of the trie

class Trie:
    def __init__(self, dictionary):
        self.root = {}
        for word in dictionary:
            self.insert(word) # insert all roots in dictionary to trie
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char in curr:
                curr = curr[char]
            else:
                curr[char] = {}
                curr = curr[char]
        curr["is_word"] = True # mark this curr node as word
    
    def search(self, word):
        curr = self.root
        prefix = ''
        for char in word:
            if 'is_word' in curr: # if we found a root in tree that is a prefix for word,
                return prefix # return the root (i.e. prefix)
            
            if char not in curr: # if char is not a child of current node, there is no reason to continue
                break

            # keep adding chars to prefix
            prefix += char
            curr = curr[char]
        
        return word # there is no root in trie for the current word, so we return the original word
    

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        trie = Trie(dictionary)

        words = sentence.split(' ')

        for i, word in enumerate(words):
            words[i] = trie.search(word) # replace current word in words array with either the root of the word (if a matching root in trie is found) or the original word (if a matching root in trie is not found)
        
        return ' '.join(words)