# 530. Minimum Absolute Difference in BST
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
# EASY
# Tags: bstlc, inorderlc, #530

# GIVEN:
    # a binary search tree root

# TASK:
    # return the minimum absolute difference between the values of any two different nodes in the tree

# EXAMPLES:
    # Input: root = [4,2,6,1,3]
    # Output: 1
    # Explanation: The minimum absolute difference is 1, which is the difference between 2 and 1

    # Input: root = [1,0,48,null,null,12,49]
    # Output: 1

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# Get every pair of nodes in the tree and compare them to get the minimum difference between any 2 nodes in the tree

# TIME COMPLEXITY: O(n^2) ❌
    # if there are n nodes, there would be approx. n^2 pairs of nodes to compare

#==========================================================================================================

# ✅ ALGORITHM 2: INORDER TRAVERSAL
# Since we know it is a BST, we can do inorder traversal of the tree to get the values in ascending order
    # we can compare the difference between each pair of consecutive values to get the minimum difference
# have a prev node that represents the node that came before current node in the inorder traversal
    # so that we can compare diff in values between prev and current node
# at every node, update the minimum absolute difference

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def getMinimumDifference(root):
    min_diff = float('inf') # initialize min. diff to infinity
    prev = None # initialize prev to null

    def dfs(node):
        nonlocal min_diff, prev

        if not node:
            return
        
        # inorder: left -> current node -> right
        dfs(node.left)

        if prev: # if prev is not null,
            min_diff = min(min_diff, node.val-prev.val) # we don't even have to use abs() here bc in a BST inorder traversal, values are always increasing
        prev = node # update prev node to current node

        dfs(node.right) # don't need to return anything bc we are updating min_diff in place
    
    dfs(root)
    return min_diff