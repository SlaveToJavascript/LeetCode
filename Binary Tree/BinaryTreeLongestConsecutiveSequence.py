# 298. Binary Tree Longest Consecutive Sequence
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/
# MEDIUM
# Tags: binarytreelc, premiumlc, #298

# GIVEN:
    # the root of a binary tree

# TASK:
    # return the length of the longest consecutive sequence path
        # A consecutive sequence path is a path where the values increase by one along the path
        # Note that the path can start at any node in the tree, and you cannot go from a node to its parent in the path

# EXAMPLES:
    # Input: root = [1,null,3,2,4,null,null,null,5]
    # Output: 3
    # Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

    # Input: root = [2,null,3,2,null,1]
    # Output: 2
    # Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
# recursively check left and right subtrees for the max length of their paths
# if node is null, it means that we have reached the end of a path -> return the length of the current path we have so far
# keep checking for the max value between the current length (i.e. up till and including current node) vs left path length vs right path length

# TIME COMPLEXITY: O(n)
    # each node is visited once
# SPACE COMPLEXITY: O(h)
    # h = height of tree

def longestConsecutive(root):
    def dfs(node, parent_val, length):
        if not node:
            return length # since we reached the end of a path, return the path length
        
        if node.val == parent_val + 1: # if current node's value is 1 more than previous (parent) node's value,
            length += 1 # we can count the current node as part of the path
        else:
            length = 1 # reset the path length to 1 (1 is for the current node, as a new path is started from the current node)

        # get left and right max path lengths
        left_len = dfs(node.left, node.val, length)
        right_len = dfs(node.right, node.val, length)

        return max(length, left_len, right_len) # get overall max path length
    
    return dfs(root, root.val-1, 0) # for parent_val of the function call, we can arbitrarily set it to root.val-1 as we know that the root node will always be part of a path