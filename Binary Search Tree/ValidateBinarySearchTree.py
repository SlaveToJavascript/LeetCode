# https://leetcode.com/problems/validate-binary-search-tree/description/
# MEDIUM
# Tags: bstlc, dfslc, #98

# GIVEN:
    # the root of a binary tree

# TASK:
    # return True if it is a valid binary search tree, False otherwise

# EXAMPLES:
    # Input: root = [2,1,3]
    # Output: true

    # Input: root = [5,1,4,null,null,3,6]
    # Output: false
    # Explanation: The root node's value is 5 but its right child's value is 4.

###########################################################################################################

# ✅ RECURSIVE DFS, LOWER AND UPPER BOUNDARIES
# We create a helper function isValid(node, lower, upper) which returns true if node.val is within the lower and upper boundaries, false otherwise
# For the root, the lower and upper boundaries are -infinity and infinity, because root.val can be anything
# For the left child of the root, the lower boundary is -infinity (doesn't change) and the upper boundary is the minimum of root.val and existing min_val (since nodes in left subtree must be less than parent node)
# For the right child of the root, the lower boundary is the maximum of root.val and existing max_val (since nodes in right subtree must be greater than parent node) and the upper boundary is infinity (doesn't change)
# By setting lower boundary = max(lower, parent.val) and upper boundary = max(upper, parent.val), we ensure that all nodes in the left subtree are less than root, and all nodes in the right subtree are greater than root

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def isValidBST(root):
    def isValid(node, lower, upper): # lower = lower boundary, upper = upper boundary
        if not node:
            return True # binary tree that is null is always BST since don't need to compare anything

        return lower < node.val < upper and isValid(node.left, lower, min(upper, node.val)) and isValid(node.right, max(lower, node.val), upper)
        # when checking if left subtree is valid, we only change the upper boundary since we only care whether nodes in left subtree are < parent
        # when checking if right subtree is valid, we only change the lower boundary since we only care whether nodes in right subtree are > parent
    
    return isValid(root, float('-inf'), float('inf')) # initialize lower = -infinity and upper = infinity which are boundaries for the root node