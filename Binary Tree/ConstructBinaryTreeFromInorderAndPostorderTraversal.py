# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
# MEDIUM
# Tags: binarytreelc, inorderlc, postorderlc, #106

# GIVEN:
    # two integer arrays, inorder and postorder
        # where inorder is the inorder traversal of a binary tree
        # postorder is the postorder traversal of the same tree

# TASK:
    # construct and return the binary tree

# EXAMPLES:
    # Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    # Output: [3,9,20,null,null,15,7]

    # Input: inorder = [-1], postorder = [-1]
    # Output: [-1]

###########################################################################################################

# ✅ ALGORITHM: My recursive solution

# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(n)
    # for the function call stack

def buildTree(inorder, postorder):
    # inorder: left -> parent -> right
    # postorder: left -> right -> parent
    if not inorder or not postorder:
        return
    root = postorder.pop() # parent node val is the last node in postorder
    root_idx = inorder.index(root)
    left_in, right_in = inorder[:root_idx], inorder[root_idx+1:]
    left_post, right_post = postorder[:root_idx], postorder[root_idx:]
    
    parent = TreeNode(root)
    parent.left = buildTree(left_in, left_post)
    parent.right = buildTree(right_in, right_post)

    return parent