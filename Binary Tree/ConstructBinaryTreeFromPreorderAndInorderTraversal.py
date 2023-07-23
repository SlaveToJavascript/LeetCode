# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# MEDIUM

# GIVEN:
    # 2 integer arrays, preorder and inorder,
    # where preorder is the preorder traversal of a binary tree
    # and inorder is the inorder traversal of the same tree

# TASK:
    # construct and return the binary tree

# EXAMPLES:
    # Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    # Output: [3,9,20,null,null,15,7]

    # Input: preorder = [-1], inorder = [-1]
    # Output: [-1]

###########################################################################################################

# ✅ ALGORITHM 1: My recursive solution (not optimized)
# NOTES:
# preorder = root -> left -> right
# inorder = left -> root -> right

# 1. In any preorder sequence, the 1st element in array will always be the root node's value
# 2. In any inorder sequence, the elements before the root node value are the left subtree's inorder sequence; the elements after the root node value are the right subtree's inorder sequence
# 3. After taking away the first element (root node) in preorder:
    # if x = length of left subtree inorder sequence (from Step 2), the next x elements after root node would be the preorder sequence of left subtree
    # if y = length of right subtree inorder sequence (from Step 2), the next y elements after root node would be the preorder sequence of right subtree

# TIME COMPLEXITY: O(n^2)
    # O(n) for each recursive call
# SPACE COMPLEXITY:

def buildTree(preorder, inorder):
    # get root node value from preorder's 1st element
    if not preorder or not inorder: return
    root = preorder.pop(0)

    # get left and right subtree inorder sequences from index of root node value in preorder array
    root_idx = inorder.index(root)
    left_subtree_inorder = []
    if inorder[0] != root:
        left_subtree_inorder = inorder[:root_idx]
    right_subtree_inorder = []
    if inorder[-1] != root:
        right_subtree_inorder = inorder[root_idx+1:]
    
    # get left and right subtree preorder sequences from length of left/right subtree's inorder sequence
    left_subtree_preorder = []
    if left_subtree_inorder:
        for _ in range(len(left_subtree_inorder)):
            val = preorder.pop(0)
            left_subtree_preorder.append(val)
    right_subtree_preorder = []
    if right_subtree_inorder:
        for _ in range(len(right_subtree_inorder)):
            val = preorder.pop(0)
            right_subtree_preorder.append(val)
    
    # build the tree
    return TreeNode(root, buildTree(left_subtree_preorder, left_subtree_inorder), buildTree(right_subtree_preorder, right_subtree_inorder))

#==========================================================================================================

# ✅✅ ALGORITHM 1A: My recursive solution (slightly cleaner code)
# Same algorithm as above, except the code is slightly cleaner and less verbose

# TIME COMPLEXITY: O(n^2)

def buildTree(preorder, inorder):
    if not preorder or not inorder: return
    root = preorder.pop(0) # root node value
    mid = inorder.index(root) # mid is root node's index in the inorder array
    left_inorder, left_preorder = inorder[:mid], preorder[:mid] # left subtree's inorder and preorder sequence
    right_inorder, right_preorder = inorder[mid+1:], preorder[mid:] # right subtree's inorder and preorder sequence
    
    return TreeNode(root, buildTree(left_preorder, left_inorder), buildTree(right_preorder, right_inorder))