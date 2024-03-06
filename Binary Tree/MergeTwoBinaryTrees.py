# 617. Merge Two Binary Trees
# https://leetcode.com/problems/merge-two-binary-trees/description/
# EASY
# Tags: binarytree, dfslc, #617

# GIVEN:
    # 2 binary trees, root1 and root2

# TASK:
    # merge the two trees into a new binary tree
    # if 2 nodes overlap, then sum node values up as the new value of the merged node
    # Otherwise, the non-null node will be used as the node of the new tree

# EXAMPLES:
    # Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
    # Output: [3,4,5,5,4,null,7]

    # Input: root1 = [1], root2 = [1,2]
    # Output: [2,2]

###########################################################################################################

# ✅ ALGORITHM 1A: RECURSIVELY BUILD TREE (my attempt – 7 Mar 2024)
# for every node where either or both trees have a node, create a new node with val = sum of the node vals from both trees
# then recursively build the left and right subtrees of the new tree

# TIME COMPLEXITY: O(n)
    # n = total no. of nodes in both trees combined
# SPACE COMPLEXITY: O(n)
    # space used by merged tree = O(n)
        # n = no. of nodes in merged tree
        # worst case: n = total no. of nodes in both trees combined
    # recursion stack: O(h)
        # h = height of merged tree
        # worst case: trees are completely unbalanced -> O(n)
        # best case: trees are balanced -> O(log n)
    # -> OVERALL SPACE COMPLEXITY: O(n)

def mergeTrees(root1, root2):
    if not root1 and not root2:
        return 

    node = TreeNode()
    node.val = (root1.val if root1 else 0) + (root2.val if root2 else 0)
    node.left = mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
    node.right = mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
    return node

#==========================================================================================================

# ✅✅✅ ALGORITHM 1B: LESS VERBOSE VERSION OF 1A
# directly return the other tree if one of the trees is null -> eliminates explicit checks for null trees before accessing .left and .right
    # if both trees are null, null will be returned anyway under the 1st if-block
# does not make use of 0's for null nodes in the sum calculation – e.g. when root1 is null, there's no value to add to, so root2 takes its place in the merged tree structure (and is henced returned in place of root1)

def mergeTrees(root1, root2):
    # If one of the trees is empty, return the other tree in its place
    if not root1:
        return root2
    if not root2:
        return root1

    # If both trees are non-empty, merge them
    root1.val += root2.val  # Update the value of root1 to be the sum of both nodes
    root1.left = mergeTrees(root1.left, root2.left)  # Recursively merge the left children
    root1.right = mergeTrees(root1.right, root2.right)  # Recursively merge the right children

    return root1