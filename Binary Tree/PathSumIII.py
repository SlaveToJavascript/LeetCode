# 437. Path Sum III
# https://leetcode.com/problems/path-sum-iii/description/
# MEDIUM
# Tags: dfslc, hashmaplc, leetcode75lc, lc75lc, #113

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
    result = 0 # no. of paths in tree with sum of target

    def dfs(node, curr_sum):
        nonlocal result # so we can access the num_paths variable declared outside the function

        if not node: 
            return
        
        curr_sum += node.val # add current node's val to curr_sum

        prefix_sum = curr_sum - targetSum
        result += prefix_sums.get(prefix_sum, 0) # if prefix sum found in hashmap, increment result by counts of this prefix sum found; else, result is unchanged
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1 # add curr_sum to hashmap as a prefix sum, with a count of 1 (or if curr_sum already exists in hashmap as a prefix sum, increment its value i.e. count)
        
        # iterate rest of the tree to increment num_paths
        dfs(node.left, curr_sum)
        dfs(node.right, curr_sum)
        prefix_sums[curr_sum] -= 1 # Reduce the count of this prefixSum path (this path has been explored -> not available for later traversals)
        
    dfs(root, 0)
    return result

#==========================================================================================================

# ✅ ALGORITHM 2: WITHOUT HASHMAP (ChatGPT solution)
# consider each node as a starting point and try to find all paths that sum to targetSum starting from this node
# recursively do the same for all child nodes as starting points
    # dfs() function calculates no. of valid paths summing up to targetSum, starting from current node
    # path_finder() function initiates dfs from every node in the tree, treating each node as a potential starting point for valid paths
# This approach ensures you consider every possible path in the tree and correctly count how many of those paths sum up to targetSum

# TIME COMPLEXITY: O(n^2)
    # dfs() takes O(n) time (worst case) as it traverses down through all possible paths starting from that node
        # this operation is proportional to height of tree, which O(n) in the worst case, i.e. a skewed tree
    # path_finder() calls dfs() on every node, and there are n nodes in the tree -> overall TC = O(n) * O(n) = O(n^2)
# SPACE COMPLEXITY: O(n)
    # worst case: depth of recursive call stack = O(n) for skewed tree
        # best/average case: O(log n) for balanced tree

def pathSum(root, targetSum):
    # dfs() calculates no. of valid paths summing up to targetSum, starting from current node
    def dfs(node, curr_sum):
        if not node:
            return 0
        
        curr_sum += node.val
        return (curr_sum == targetSum) + dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
        # adds 1 to return value if current sum = target sum
        # return value: total no. of valid paths rooted from current node = no. of valid paths found in left subtree + no. of valid paths found in right subtree
    
    # path_finder() initiates dfs from every node in the tree, treating each node as a potential starting point for valid paths
        # NOTE: we need this function since every node in tree can be the start of a path, NOT JUST THE ROOT NODE
    def path_finder(node):
        if not node:
            return 0
        
        return dfs(node, 0) + path_finder(node.left) + path_finder(node.right) # returns total no. of valid paths in entire tree
        # 1. calls dfs() for the current node to count all valid paths starting from this node
        # 2. recursively calls itself for left and right children, i.e. treating each child as a new starting point for potential paths
        # -> total no. of valid paths includes paths starting from current node and all paths found in the subtrees rooted at its children
    
    return path_finder(root)
    # path_finder() is called with root of tree as initial argument
        # this explores entire tree, where every node gets a chance to be the starting point of a path, and all paths downward from each node are explored to find those that sum up to the target sum