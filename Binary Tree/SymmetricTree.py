# https://leetcode.com/problems/symmetric-tree/description/
# EASY

# GIVEN:
    # Given the root of a binary tree

# TASK:
    # check whether it is a mirror of itself (i.e., symmetric around its center)

###########################################################################################################

# ALGORITHM: RECURSION
# To check if a binary tree is symmetric, compare its left subtree and right subtree
    # To do this, traverse tree recursively and compare left and right subtrees at each level
    # If they are symmetric, we continue the traversal
    # Otherwise, we immediately return false

# define a recursive helper function that takes left and right child nodes as input
# it returns true if both nodes are null, or if their values are equal and their subtrees are symmetric

# TIME COMPLEXITY: O(n)
    # n = no. of nodes in binary tree
    # We need to visit each node once to check if the tree is symmetric
# SPACE COMPLEXITY: O(h)
    # h = height of binary tree
    # worst case: tree is completely unbalanced, and recursion stack goes as deep as height of tree

def isSymmetric(root):
    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        # at this point, left and right are both not null
        return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
    return isMirror(root.left, root.right)