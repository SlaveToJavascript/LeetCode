# https://leetcode.com/problems/path-sum-iii/description/
# MEDIUM
# Tags: dfslc, hashmaplc, #113

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
# Maintain prefix sums while doing dfs from root to leaf
# If currentSum - prefixSum = targetSum, then we've found a path that has a value of target
# If we encountered prefixSum n times, then we've found n such paths

def pathSum(root, targetSum):
    # hashmap of prefix sums encountered in current path, and their frequencies
    prefix_sums = {}
    prefix_sums[0] = 1

    def dfs(node, curr_sum):
        if not node: return 0

        num_paths = 0
        
        curr_sum += node.val

        prefix_sum = curr_sum - targetSum
        num_paths += prefix_sums[prefix_sum]
        
        prefix_sums[curr_sum] += 1 # add value of this prefix sum to prefix sums hashmap
        num_paths += dfs(node.left, curr_sum) + dfs(node.right, curr_sum) # explore children
        prefix_sums[curr_sum] -= 1 # Remove value of this prefixSum (path's been explored)
        
        return num_paths
    
    return dfs(root, 0)