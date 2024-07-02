# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# EASY
# Tags: binarytreelc, dfslc, #111

# GIVEN:
    # a binary tree

# TASK:
    # find its minimum depth
    # min. depth is the no. of nodes along the shortest path from the root node down to the nearest leaf node
    # e.g. if there is only a root node with no leaf nodes, min. depth = 1

# EXAMPLES:
    # Input: root = [3,9,20,null,null,15,7]
    # Output: 2

    # Input: root = [2,null,3,null,4,null,5,null,6]
    # Output: 5

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS

def minDepth(root):
    if not root: 
        return 0
    path_depths = []

    def dfs(node, depth):
        if not node: 
            return 
        if not node.left and not node.right: 
            path_depths.append(depth)
        
        if node.left: 
            dfs(node.left, depth+1)
        if node.right: 
            dfs(node.right, depth+1)
    
    dfs(root, 1) # start with depth = 1 for the root node
    return min(path_depths)