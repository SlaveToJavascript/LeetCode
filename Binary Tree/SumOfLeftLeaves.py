# 404. Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/description/
# EASY
# Tags: dfslc, binarytreelc, #404

# GIVEN:
    # the root of a binary tree

# TASK:
    # return the sum of all left leaves
        # A left leaf is a leaf that is the left child of another node

# EXAMPLES: 
    # Input: root = [3,9,20,null,null,15,7]
    # Output: 24
    # Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

    # Input: root = [1]
    # Output: 0

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS
# at each node, check if its left child is a leaf
    # if yes, add left child's value to the sum

def sumOfLeftLeaves(root):
    if not root:
        return 0
    
    left_sum = 0 # *** see NOTE

    if root.left and not root.left.left and not root.left.right: # check if left child is leaf
        left_sum += root.left.val # add left child's val to left_sum

    return left_sum + sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right) # add up the sums of left leaves in the current subtree, left subtree and right subtree



# *** NOTE: "left_sum = 0" is not meant to keep a running total across all recursive calls
    # The accumulation of sums across the entire tree happens through the return values of the recursive calls
    # Each call in the line "sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)" calculates the sum of left leaves of left and right subtrees and returns this sum to the caller