# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# MEDIUM
# Tags: binarytreelc, bfslc, #103

# GIVEN:
    # the root of a binary tree

# TASK:
    # return the zigzag level order traversal of its nodes' values
        # i.e., from left to right, then right to left for the next level and alternate between

# EXAMPLES:
    # Input: root = [3,9,20,null,null,15,7]
    # Output: [[3],[20,9],[15,7]]

    # Input: root = [1]
    # Output: [[1]]

    # Input: root = []
    # Output: []

###########################################################################################################

# ✅ ALGORITHM: ITERATIVE BFS, REVERSE LEVEL-NODES FOR ODD LEVELS
# We keep track of the level no. of each level we're at
    # e.g. root level = 0, next level = 1, etc.
# at odd levels (e.g. level = 1, 3, etc.), we reverse the array of nodes in that level before adding it to result array

# TIME COMPLEXITY: O(N)
    # N = number of nodes in tree
    # we visit each node once
# SPACE COMPLEXITY: O(N)

def zigzagLevelOrder(root):
    if not root: return []

    q = [root]
    result = [] # return value
    level = -1 # root level will become level 0
    
    while q:
        nodes = [] # array of nodes in this level
        level += 1
        for _ in range(len(q)):
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            nodes.append(node.val)

        if level % 2 != 0: # if odd level,
            nodes = nodes[::-1] # reverse list of nodes before adding to result
        
        result.append(nodes)
    
    return result