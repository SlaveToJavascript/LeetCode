# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/description/
# EASY
# Tags: binarytreelc, dfslc, #572

# GIVEN:
    # the roots of 2 binary trees, root and subRoot

# TASK:
    # return True if there is a subtree of root with the same structure and node values of subRoot
        # A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants

#==========================================================================================================

# ✅ ALGORITHM: RECURSIVE DFS
    # https://www.youtube.com/watch?v=E36O5SWp-LE
# (similar to another problem: Same Tree)
# helper function isSubtree() that recursively checks if trees are identical
# if not identical, check if root's left or right subtree is identical to subRoot

# TIME COMPLEXITY: O(n*m)
    # n and m = no. of nodes in root and subRoot respectively
    # worst case: we have to check each node in root against each node in subRoot for a match
# SPACE COMPLEXITY: O(max(h1, h2))
    # h1 and h2 = heights of root and subRoot respectively
    # worst case: space complexity is the deepest recursion needed to compare 2 subtrees or traverse root

def isSubtree(root, subRoot):
    # recursively check if tree1 and tree2 are identical
    def isSameTree(tree1, tree2):
        if not tree1 and not tree2:
            return True # if both trees are null, they are definitely identical
        
        if not tree1 or not tree2:
            return False # if either tree is null (but not both), they are definitely not identical
        
        return tree1.val == tree2.val and isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right) # if both trees' values are the same and their left and right subtrees are identical, they are identical
    
    if not subRoot:
        return True # if subroot is null, it will always be a subtree of root!
    # NOTE: actually you don't even need the above 2 lines since isSameTree() already checks this condition

    if not root:
        return False # here, subroot is not null but root is null, so subroot cannot possibly be a subtree of root
    
    if isSameTree(root, subRoot):
        return True
    
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot) # if root and subroot do not have the same val, check if root's left/right children are identical to subroot