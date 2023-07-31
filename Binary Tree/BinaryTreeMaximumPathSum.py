# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# HARD
# Tags: binarytreelc, dfslc, #124

# GIVEN:
    # the root of a binary tree

# TASK:
    # return the maximum path sum of any non-empty path
    # path sum of a path is the sum of the node's values in the path
    # NOTE: path does not need to pass through the root or start from root

# EXAMPLES:
    # Input: root = [1,2,3]
    # Output: 6
    # Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

    # Input: root = [-10,9,20,null,null,15,7]
    # Output: 42
    # Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS
# Define helper function, dfs(node), that returns the max path sum without splitting at node
    # splitting = we add node val and consider both left and right subtrees for max path sum
    # no splitting = we add node val and consider only 1 subtree, left or right, to our max path sum
        # this is because there is another parent node above that has already split -> we cannot split again at the current node as we can only split once so we get 1 continuous path
# Define a global variable, result, to store the max path sum

# TIME COMPLEXITY: O(n)
    # we visit each node once
# SPACE COMPLEXITY: O(h)
    # h = height of tree

def maxPathSum(root):
    result = 0 # initialize max path sum to whatever's at the root

    def dfs(node):
        if not node: return 0
        
        # calculate max path sum if we split at node
            # max path sum if split at node = node.val + max path sum of left subtree + max path sum of right subtree
        leftMax = dfs(node.left)
        rightMax = dfs(node.right)
        # but since leftMax and rightMax may be -ve (in the case of -ve node vals), we can choose not to include the left/right subtrees if including these subtrees reduces the max path sum at node
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        result = max(result, node.val + leftMax + rightMax) # max path sum if we split at node

        # the return value is max path sum WITHOUT splitting
            # why? Because when we run dfs() to calculate leftMax and rightMax above, we are already splitting at the parent node of left and right subtrees -> we cannot split again at the left and right children nodes since we can only have 1 split in a max path sum
            # max path sum without splitting at node = node.val + max(max path sum of left subtree, max path sum of right subtree)
        return node.val + max(leftMax, rightMax)
    
    dfs(root)
    return result