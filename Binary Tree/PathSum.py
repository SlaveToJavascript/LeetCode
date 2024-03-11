# https://leetcode.com/problems/path-sum/description/
# EASY
# Tags: dfslc, #112

# GIVEN:
    # a binary tree, root
    # an integer, targetSum

# TASK:
    # return true if the tree has a root-to-leaf path with a sum = targetSum

# EXAMPLES:
    # Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    # Output: true
    # Explanation: 5 + 4 + 11 + 2 = 22

    # Input: root = [1,2,3], targetSum = 5
    # Output: false
    # Explanation: There two root-to-leaf paths in the tree:
    # (1 --> 2): The sum is 3.
    # (1 --> 3): The sum is 4.
    # There is no root-to-leaf path with sum = 5.

    # Input: root = [], targetSum = 0
    # Output: false
    # Explanation: Since the tree is empty, there are no root-to-leaf paths.

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS

def hasPathSum(root, targetSum):

    def dfs(node, current_sum):
        if not node: 
            return False
        current_sum += node.val
        if not node.left and not node.right: # if leaf node
            return current_sum == targetSum
        
        return dfs(node.left, current_sum) or dfs(node.right, current_sum)
    
    return dfs(root, 0)

#==========================================================================================================

# ✅ ALGORITHM 2: ITERATIVE DFS

def hasPathSum(root, targetSum):
    stack = [(root, 0)]
    curr_sum = 0

    while stack:
        node, curr_sum = stack.pop()
        if not node: 
            return False # this handles the edge case where root is null
        
        curr_sum += node.val
        if not node.left and not node.right and curr_sum == targetSum: # if node is leaf node and targetSum is reached
            return True
        
        if node.right: 
            stack.append((node.right, curr_sum))
        if node.left: 
            stack.append((node.left, curr_sum))
    
    return False