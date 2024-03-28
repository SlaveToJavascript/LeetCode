# 655. Print Binary Tree
# https://leetcode.com/problems/print-binary-tree/description/
# MEDIUM
# Tags: binarytreelc, dfslc, #655

# GIVEN:
    # root of a binary tree

# TASK:
    # construct an m x n string matrix, res, that represents a formatted layout of the tree
        # The formatted layout matrix should be constructed using the following rules:
            # The height of the tree is height and the number of rows m should be equal to height + 1
            # The number of columns n should be equal to 2^(height+1) - 1
            # Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2])
            # For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c - 2^(height-r-1)] and its right child at res[r+1][c + 2^(height-r-1)]
            # Continue this process until all the nodes in the tree have been placed
            # Any empty cells should contain the empty string ""
    # TODO: return the constructed matrix, res

# EXAMPLES:
    # Input: root = [1,2]
    # Output: 
    # [["","1",""],
    #  ["2","",""]]

    # Input: root = [1,2,3,null,4]
    # Output: 
    # [["","","","1","","",""],
    #  ["","2","","","","3",""],
    #  ["","","4","","","",""]]

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
# 1. get height of the tree
# 2. create result matrix with the given dimensions (based on height)
# 3. recursively traverse the tree, and populate the result matrix for each node respective to its parent node

# TIME COMPLEXITY: O(n)
    # in both get_height() and dfs() functions, each node is visited once
# SPACE COMPLEXITY: O((h+1) * (2^(h+1)-1))
    # given a tree with height = h, the matrix dimensions are (h+1) * (2^(h+1)-1)
        # for a balanced binary tree, this space complexity = O(2^h)
    # recursive call stack is O(h)

def printTree(root):
    def get_height(node):
        if not node:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))
    
    height = get_height(root)-1 # -1 bc the "height" defined the question is the max. no. of edges from root to child, but in the get_height function, each node level is considered 1 height
    cols = 2**(height+1) - 1 # cols = n
    result = [["" for _ in range(cols)] for _ in range(height+1)] # string matrix result to be populated

    def dfs(node, r, c): # (r,c) is the indexes of the result matrix where node is to be placed at
        if not node:
            return
        
        result[r][c] = str(node.val) # place node into the correct position in the result matrix
        # recursively place children nodes into the correct position in the resuult matrix (the coords respective to parent's coords (r,c) are given in the question)
        dfs(node.left, r+1, c - 2**(height-r-1))
        dfs(node.right, r+1, c + 2**(height-r-1))
    
    dfs(root, 0, (cols-1)//2) # the coords of matrix result at which to place root node is given in the question
    return result