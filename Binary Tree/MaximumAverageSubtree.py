# 1120. Maximum Average Subtree
# https://leetcode.com/problems/maximum-average-subtree/
# MEDIUM
# Tags: dfslc, binarytreelc, #1120

# GIVEN:
    # the root of a binary tree
    
# TASK:
    # return the maximum average value of a subtree of that tree
    # A subtree of a tree is any node of that tree plus all its descendants
    # The average value of a tree is the sum of its values, divided by the number of nodes

# EXAMPLES:
    # Input: root = [5,6,1]
    # Output: 6.00000
    # Explanation: 
    # For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
    # For the node with value = 6 we have an average of 6 / 1 = 6.
    # For the node with value = 1 we have an average of 1 / 1 = 1.
    # So the answer is 6 which is the maximum.

    # Input: root = [0,null,1]
    # Output: 1.00000

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS (my solution)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def maximumAverageSubtree(root):
    result = 0

    def dfs(node): # returns [total_val, num_nodes]
        nonlocal result

        if not node:
            return [0, 0]
        
        left_total, left_nodes = dfs(node.left)
        right_total, right_nodes = dfs(node.right)

        total = left_total + right_total + node.val
        nodes = left_nodes + right_nodes + 1 # +1 for the current node
        result = max(result, total/nodes) # update result with the max average value
        return [total, nodes]

    dfs(root)
    return result