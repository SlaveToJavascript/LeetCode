# https://leetcode.com/problems/count-complete-tree-nodes/description
# EASY
# Tags: dfslc, binarytreelc, #222

# GIVEN:
    # root of a complete binary tree

# TASK:
    # return the number of the nodes in the tree
    # NOTE: In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible
        # It can have between 1 and 2h nodes inclusive at the last level h
        # e.g. this is a complete binary tree:
            #      1
            #    /   \
            #   2     3
            #  / \    /
            # 4   5  6
        # This is not a complete binary tree:
            #     1
            #    / \
            #   2   3
            #  / \   \
            # 4   5   7

# EXAMPLES:
    # Input: root = [1,2,3,4,5,6]
    # Output: 6

    # Input: root = []
    # Output: 0

    # Input: root = [1]
    # Output: 1

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS
# MAIN IDEA: for a complete binary tree, since all nodes in the last level are as far left as possible, at each root node of a tree/subtree, we check if left height = right height
    # if left height = right height for a particular subtree's root, this subtree is a perfect binary tree and no. of nodes = 2^h-1 (h = height of subtree)
        # add no. of nodes = 2^h-1 to result
    # if left height != right height for a particular subtree's root, recursively run the function on the left and right subtrees of the current root
# no. of nodes in a binary tree = 1 + no. of nodes in left subtree + no. of nodes in right subtree
    # the 1 is for the root node

# TIME COMPLEXITY: O((log n)^2)
    # left_height() and right_height() each take O(h) = O(log n) time
    # we make at most O(h) recursive calls
        # for each call, height computations take O(h) time
    # overall TC = O(h) * O(h) = O(log n) * O(log n) = O((log n)^2)
# SPACE COMPLEXITY: O(h) i.e. O(log n)
    # due to recursive call stack

def countNodes(root):
    if not root: return 0

    def left_height(node):
        if not node: return 0
        return 1 + left_height(node.left)
    
    def right_height(node):
        if not node: return 0
        return 1 + right_height(node.right)
    
    left_height = left_height(root)
    right_height = right_height(root)

    if left_height == right_height: # this is a perfect binary tree/subtree
        return 2**left_height - 1 # no. of nodes in perfect binary tree = 2^h - 1
    
    return 1 + countNodes(root.left) + countNodes(root.right) # 1 is for the root