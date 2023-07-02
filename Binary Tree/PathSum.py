# https://leetcode.com/problems/path-sum/description/
# EASY

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
        if not node: return False
        current_sum += node.val
        if not node.left and not node.right: # if leaf node
            return current_sum == targetSum
        
        return dfs(node.left, current_sum) or dfs(node.right, current_sum)
    
    return dfs(root, 0)

#==========================================================================================================

# ✅ ALGORITHM 2: ITERATIVE DFS

def hasPathSum(root, targetSum):
    stack = [(root, targetSum)]
    while stack:
        curr_node, curr_sum = stack.pop()
        if not curr_node: return False
        if not curr_node.left and not curr_node.right and curr_sum == curr_node.val:
            return True
        
        if curr_node.left: 
            stack.append((curr_node.left, curr_sum - curr_node.val))
        if curr_node.right: 
            stack.append((curr_node.right, curr_sum - curr_node.val))
    return False