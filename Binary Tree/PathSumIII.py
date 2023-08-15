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

# ✅ ALGORITHM: RECURSIVE DFS
# Maintain prefix sums in hashmap while doing dfs from root to leaf
# If currentSum - prefixSum found in hashmap = targetSum, then we've found a path that has a value of target
# If we encountered prefixSum n times, then we've found n such paths -> increment num_paths by n
# for each curr_sum (i.e. sum of previous nodes' vals encountered), add it to prefix sums hashmap as it may be a prefix to a valid path in the tree

# TIME COMPLEXITY: O(n)
    # n = no. of nodes in tree
    # we visit each node once
# SPACE COMPLEXITY: O(n)
    # n = no. of nodes in tree
    # hashmap can contain up to n entries (if each node has a unique value)

def pathSum(root, targetSum):
    prefix_sums = {} # hashmap of prefix sums encountered in current path, and their frequencies
    prefix_sums[0] = 1 # initiate the no. of 0 prefixes = 1
    num_paths = 0 # return value (i.e. no. of paths in tree with sum of target)

    def dfs(node, curr_sum):
        nonlocal num_paths # so we can access the num_paths variable declared outside the function

        if not node: return
        
        curr_sum += node.val # add current node's val to curr_sum

        prefix_sum = curr_sum - targetSum
        num_paths += prefix_sums.get(prefix_sum, 0) # if prefix sum found in hashmap, incremeent num_paths by counts of this prefix sum found; else, num_paths is unchanged
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1 # add curr_sum to hashmap as a prefix sum, with a count of 1 (or if curr_sum already exists in hashmap as a prefix sum, increment its value i.e. count)
        
        # iterate rest of the tree to increment num_paths
        dfs(node.left, curr_sum)
        dfs(node.right, curr_sum)
        prefix_sums[curr_sum] -= 1 # Reduce the count of this prefixSum path (this path has been explored -> not available for later traversals)
        
    dfs(root, 0)
    return num_paths