# https://leetcode.com/problems/word-search-ii/
# HARD
# Tags: trielc, dfslc, backtracklc, matrixlc, #212

# GIVEN:
    # an m x n board of characters, board
    # a list of strings, words

# TASK: 
    # return all words in words array that can be formed in board
    # NOTE: Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring
    # The same letter cell may not be used more than once in a word

# EXAMPLES:
    # Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
    # Output: ["eat","oath"]

    # Input: board = [["a","b"],["c","d"]], words = ["abcb"]
    # Output: []

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE (BACKTRACKING DFS TO FIND EACH WORD IN WORDS)
# for each word in words, for each cell in board, start DFS from that cell and check if the word is in DFS path

# TIME COMPLEXITY: O(w * mn * 4^l)
    # m = no. of rows, n = no. of cols
    # l = length of longest word in words array
    # 1 DFS across the whole board starting from a cell = O(4^l) at max
        # at max we're going to traverse s amount of letters in 4 directions
    # since we do DFS from every cell on board: O(mn * 4^l)
        # bc no. of cells = mn
    # since we're checking if each word is in DFS path: O(w * mn * 4^l)
        # w = length of words array

#==========================================================================================================

# ✅ ALGORITHM 2: TRIE CONSTRUCTED FROM WORDS ARRAY + DFS + BACKTRACKING
# Construct trie from all words in words array
# curr pointer points to current node in trie, starting from root
# Do DFS starting from every cell in board
    # for each cell visited along DFS path, check if the char in that cell is in the children of curr trie node
        # if curr char in board is a child of curr node, 
            # change curr node to point to that child node
            # add that char to current word constructed from DFS path
            # if that char is the last char of any word in words array (i.e. that char's Node.isWordEnd value is True), add that word (from the current DFS path) to results set
                # NOTE: we have to use a result SET, not result array, as there may be multiple occurrences of the same word on board
                    # e.g. words = ["oa","oaa"], but there are 2 occurrences of "oa" on the board, the return result will be ["oa","oa","oaa"], but we only want to return ["oa","oaa"]
            # visit all 4 neighbors of current char's cell and process those
            # after all the above, remove curr char's cell from visited set
                # so that other DFS paths starting from other cells can still visit that cell
        # else, if curr char in board is not a child of curr trie node, it means there are no words containing current DFS path prefix in words array -> we end the DFS there
    # we also end the DFS path if current cell is in visited array
        # bc we cannot use the same letter more than once in a word
    # return result set converted to list

# TIME COMPLEXITY: O(mn * 4^l)
    # m = no. of rows, n = no. of cols
    # l = length of longest word in words array
    # 1 DFS across the whole board starting from a cell = O(4^l) at max
        # at max we're going to traverse s amount of letters in 4 directions
    # since we do DFS from every cell on board: O(mn * 4^l)
        # bc no. of cells = mn
# SPACE COMPLEXITY: 
    # w = no. of words in words array
    # l = length of longest word in words array
    # Trie takes O(wl) space
    # DFS recursion stack takes O(l) space
        # In DFS, we start from a cell and try to build a word char by char by exploring one of its unvisited neighbors
        # worst case: we go as deep as the length of the longest word in our list of words
    # visited set takes O(mn) space
        # worst case: visited contains all cells in matrix
    # result takes O(w) space

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()

        # construct Trie from words in words array
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
    def findWords(self, board, words):
        rows, cols = len(board), len(board[0])
        trie = Trie(words)
        root = trie.root
        
        result = set() # return value
        visited = set() # trie nodes visited along DFS path

        def dfs(r, c, curr_node, curr_word): # DFS over board matrix
            if r < 0 or r >= rows or c < 0 or c >= cols: # if r,c is out of bounds of board
                return
            if (r,c) in visited: # if cell r,c has been visited in current DFS path
                return
            if board[r][c] not in curr_node.children: # if char at current matrix cell is not part of a valid prefix of any word in trie
                return
            
            visited.add((r,c))
            curr_node = curr_node.children[board[r][c]] # curr_node points to current cell's char's trie node
            curr_word += board[r][c] # add current cell's char to curr_word formed from current DFS path
            if curr_node.isWord: # if current cell's char is the end of a word in trie,
                result.add(curr_word) # add it to result
            
            # visit and process curr cell's 4 neighbors
            dfs(r-1, c, curr_node, curr_word)
            dfs(r+1, c, curr_node, curr_word)
            dfs(r, c-1, curr_node, curr_word)
            dfs(r, c+1, curr_node, curr_word)
            
            visited.remove((r,c)) # remove curr cell from visited set so that other DFS paths starting from other cells can still visit curr cell
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "") # initiate a DFS path starting from each cell in matrix which checks for matching words in trie
        
        return list(result) # result was a set -> convert to list