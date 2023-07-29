# https://leetcode.com/problems/path-sum-ii/description/
# MEDIUM
# Tags: dfslc, #113

# GIVEN:
    # root of a binary tree
    # integer, targetSum

# TASK:
    # return a 2D list of all root-to-leaf paths where the sum of the path = targetSum

# EXAMPLES:
    # Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    # Output: [[5,4,11,2],[5,8,4,5]]
    # Explanation: There are two paths whose sum equals targetSum:
    # 5 + 4 + 11 + 2 = 22
    # 5 + 8 + 4 + 5 = 22

    # Input: root = [1,2,3], targetSum = 5
    # Output: []

    # Input: root = [1,2], targetSum = 0
    # Output: []

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS

def pathSum(root, targetSum):
    result = []

    def dfs(node, curr_sum, path):
        if not node: return

        curr_sum += node.val
        temp = path + [node.val] # need to create a new temp list instead of adding node.val to path, otherwise all nodes will get added to path
        # if we are to append node.val to path instead of using temp, we need to pop the last element from path every time if node is not leaf and/or current sum is not = targetSum

        if not node.left and not node.right and curr_sum == targetSum: # if node is leaf and current sum = targetSum
            result.append(temp)
        if node.left: dfs(node.left, curr_sum, temp)
        if node.right: dfs(node.right, curr_sum, temp)
    
    dfs(root, 0, [])

    return result