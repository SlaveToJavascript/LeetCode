# 2265. Count Nodes Equal to Average of Subtree
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/
# MEDIUM
# Tags: binarytreelc, dfslc, #2265

# GIVEN:
    # root of a binary tree

# TASKS:
    # return the no. of nodes where the node's val is equal to the average of the values in its subtree
    # NOTE: The average of n elements is the sum of the n elements divided by n and ROUNDED DOWN to the nearest integer

# EXAMPLES:
    # Input: root = [4,8,5,0,1,null,6]
    # Output: 5
    # Explanation: 
    # For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
    # For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
    # For the node with value 0: The average of its subtree is 0 / 1 = 0.
    # For the node with value 1: The average of its subtree is 1 / 1 = 1.
    # For the node with value 6: The average of its subtree is 6 / 1 = 6.

    # Input: root = [1]
    # Output: 1
    # Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS (return both sum of vals and count of nodes together)
# dfs() function returns the total sum of values and the total count of nodes in the tree/subtree
    # i.e. return (sum_of_vals, count_of_nodes)

# TIME COMPLEXITY: O(n)
    # each node is visited once
# SPACE COMPLEXITY: O(h)
    # h = height of tree = O(log n) on average
    # h = n in worst case (skewed tree)

import math

def averageOfSubtree(root):
    result = 0

    def dfs(node):
        nonlocal result

        if not node:
            return (0,0) # (sum_of_vals, count_of_nodes)
        
        left_sum, left_count = dfs(node.left)
        right_sum, right_count = dfs(node.right)
        
        total_sum = left_sum + right_sum + node.val
        total_count = left_count + right_count + 1
        if math.floor(total_sum / total_count) == node.val: # math.floor() rounds DOWN to nearest integer
            result += 1
        
        return (total_sum, total_count)
    
    dfs(root)
    return result