# 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/description
# EASY
# Tags: bstlc, #700

# GIVEN:
    # root of a binary search tree (BST)
    # an integer, val

# TASK:
    # Find the node in the BST that the node's value equals val and return the subtree rooted with that node
    # If such a node does not exist, return null

# EXAMPLES:
    # Input: root = [4,2,7,1,3], val = 2
    # Output: [2,1,3]

    # Input: root = [4,2,7,1,3], val = 5
    # Output: []

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
# if root is null, return null
# if root's val == val, return root
# if root's val < val, search right subtree (since right subtree's values are > root.val)
# if root's val > val, search left subtree (since left subtree's values are < root.val)

# TIME COMPLEXITY: O(n)
    # average: O(h) -> O(log n), if the BST is balanced
    # worst: O(n), if BST is skewed (where h = n)
# SPACE COMPLEXITY: O(n)
    # average: O(h) -> O(log n), if the BST is balanced
    # worst: O(n), if BST is skewed (where h = n)

def searchBST(root, val):
    if not root:
        return
    if root.val == val:
        return root
    
    if root.val < val:
        return searchBST(root.right, val)
    if root.val > val:
        return searchBST(root.left, val)