# 549. Binary Tree Longest Consecutive Sequence II
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/
# MEDIUM
# Tags: binarytreelc, dfslc, premiumlc, #549

# GIVEN:
    # the root of a binary tree

# TASK:
    # return the length of the longest consecutive path in the tree
        # A consecutive path is a path where the values of the consecutive nodes in the path differ by one. This path can be either increasing or decreasing
            # For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid.
        # On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

# EXAMPLES:
    # Input: root = [1,2,3]
    # Output: 2
    # Explanation: The longest consecutive path is [1, 2] or [2, 1].

    # Input: root = [2,1,3]
    # Output: 3
    # Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
# for every node, there are 2 values, "incr" and "decr"
    # "incr" = length of the longest INCREASING path (downward direction) below the current node including itself
        # i.e. if a child node is 3, and the parent node is 2, this is an INCREASING path (in the downward direction)
    # # "decr" = length of the longest DECREASING path (downward direction) below the current node including itself
        # if a child node is 2, and the parent node is 3, this is an DECREASING path (in the downward direction)
# recursive dfs() function returns [incr, decr] of the current node
# start by setting incr = decr = 1 for the current node
    # because the node ITSELF (on its own) always forms a consecutive increasing as well as decreasing path of length 1
# base case: if node is invalid, [0,0] is returned
# if current node has a LEFT child, and:
    # left child's value is one LESS than the current node:
        # it forms a DECREASING sequence with the current node -> decr of current node = decr of left child +1
    # left child's value is one MORE than the current node:
        # it forms an INCREASING sequence with the current node -> incr of current node = incr of left child +1
# do the same for the right child, but to get the incr and decr for the current node from the right child, we need to consider the maximum value out of the two values obtained from the left and the right child for both inr and dcr (since we need to consider the longest sequence possible)
# after getting the final values of incr and decr for a node, update the length of the longest consecutive path found so far stemming from current node
    # FORMULA: max_path_len = max(incr + decr - 1)
        # -1 so that the current node is not counted twice, as both incr and decr include the current node in the path length

# TIME COMPLEXITY: O(n), n = no. of nodes
# SPACE COMPLEXITY: O(n), n = no. of nodes
    # The recursion goes up to a depth of n in the worst case

def longestConsecutive(root):
    def dfs(node):
        nonlocal max_len # return value

        if not node:
            return [0, 0]  # incr, decr

        incr = decr = 1 # the node ITSELF (on its own) always forms a consecutive increasing as well as decreasing path of length 1
        if node.left:
            left_incr, left_decr = dfs(node.left)
            if node.val == node.left.val + 1: # downward decreasing sequence
                decr = left_decr + 1
            elif node.val == node.left.val - 1: # downward increasing sequence
                incr = left_incr + 1

        if node.right:
            right_incr, right_decr = dfs(node.right)
            if node.val == node.right.val + 1: # downward decreasing sequence
                decr = max(decr, right_decr + 1)
            elif node.val == node.right.val - 1: # downward increasing sequence
                incr = max(incr, right_incr + 1)

        max_len = max(max_len, incr + decr - 1) # -1 so that the current node is not counted twice, as both incr and decr include the current node in the path length
        return [incr, decr]

    max_len = 0
    dfs(root) # this updates max_len
    return max_len