# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description
# MEDIUM
# Tags: binarytreelc, dfslc, leetcode75lc, lc75lc, #1448

# GIVEN:
    # binary tree root

# TASK:
    # Return the number of good nodes in the binary tree
        # a node is good if, in the path from root to X, there are no nodes with value greater than X

# EXAMPLES:
    # Input: root = [3,1,4,3,null,1,5]
    # Output: 4
    # Explanation: Nodes in blue are good.
    # Root Node (3) is always a good node.
    # Node 4 -> (3,4) is the maximum value in the path starting from the root.
    # Node 5 -> (3,4,5) is the maximum value in the path
    # Node 3 -> (3,1,3) is the maximum value in the path.

    # Input: root = [3,3,null,4,2]
    # Output: 3
    # Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

    # Input: root = [1]
    # Output: 1
    # Explanation: Root is considered as good.

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
    # https://www.youtube.com/watch?v=7cp5imvDzl4
# Recursively iterate through binary tree
# if current node's value is >= max value, counter +1
# update max value if needed
# return counter result for left and right children of current node

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(h)
    # h = height of tree

def goodNodes(root):
    def getNumberOfGoodNodes(node, max_val):
        if not node: 
            return 0
        current_count = 1 if node.val >= max_val else 0 # if current node is a good node, count=1
        max_val = max(max_val, node.val) # update max val if needed
        return current_count + getNumberOfGoodNodes(node.left, max_val) + getNumberOfGoodNodes(node.right, max_val)
    
    return getNumberOfGoodNodes(root, float('-inf')) # must use -ve infinity instead of 0 since node values may be < 0