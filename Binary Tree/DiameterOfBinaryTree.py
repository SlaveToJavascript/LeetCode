# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/description/
# EASY
# Tags: binarytreelc, dfslc, #543

# GIVEN:
    # the root of a binary tree

# TASK:
    # return the length of the diameter of the tree
    # diameter of a binary tree = length of the longest path between any two nodes in a tree
        # This path may or may not pass through the root

# EXAMPLES:
    # Input: root = [1,2,3,4,5]
    # Output: 3
    # Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

    # Input: root = [1,2]
    # Output: 1

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
    # https://www.youtube.com/watch?v=bkxqA8Rfv04
# NOTE: diameter of binary tree = max(left height, right height)
    # height = no. of edges in longest path from node to a leaf
# for each node, calculate height of left and right subtrees, and calculate diameter at each node (left subtree height + right subtree height), updating max diameter found so far

# TIME COMPLEXITY: O(n)
    # DFS visits each node once
# SPACE COMPLEXITY: O(h)
    # h = height of tree

def diameterOfBinaryTree(root):
    max_diameter = 0

    def getHeight(node):
        nonlocal max_diameter

        if not node:
            return 0
        
        # get heights of the left and right subtrees
        left_height = getHeight(node.left)
        right_height = getHeight(node.right)
        max_diameter = max(max_diameter, left_height + right_height)

        return 1 + max(left_height, right_height) # height of tree rooted at this node
            # the "1 + " is for the edge between this node and either of its children
    
    getHeight(root)
    return max_diameter