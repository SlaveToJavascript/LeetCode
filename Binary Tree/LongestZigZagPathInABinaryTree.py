# 1372. Longest ZigZag Path in a Binary Tree
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/
# MEDIUM
# Tags: binarytreelc, dfslc, leetcode75lc, lc75lc, #1372

# GIVEN:
    # the root of a binary tree

# TASK:
    # Return the longest ZigZag path contained in that tree
    # A ZigZag path for a binary tree is defined as follows
        # Choose any node in the binary tree and a direction (right or left).
        # If the current direction is right, move to the right child of the current node; 
            # otherwise, move to the left child
        # Change the direction from right to left or from left to right
        # Repeat the second and third steps until you can't move in the tree
    # Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0)

# EXAMPLES:
    # Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
    # Output: 3
    # Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

    # Input: root = [1,1,1,null,1,null,null,1,1,null,1]
    # Output: 4
    # Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

    # Input: root = [1]
    # Output: 0

###########################################################################################################

# ✅✅✅ ALGORITHM 1A: RECURSIVE DFS
# maxZigzagPath() function keeps track of whether we traversed to the current node's left child or right child
# if we traversed to the left child, in the next recursion of maxZigzagPath(), we should traverse to the right child, and vice versa
# maxZigzagPath() also keeps track of the longest zigzag path so far
# to start the zigzag path from non-root nodes, we can simply reset the longest zigzag path length to 0 and go the child node that is not part of the zigzag direction
    # e.g. if the longest zigzag path is on the right of the root node but the root node cannot access this longest zigzag path because we need to go take 2 right directions, then:
        # from root, go to the right (root.right is the starting node of this longest zigzag path), then go to the right again to continue the path but reset longest zigzag path length to 0

# TIME COMPLEXITY: O(n)
    # we recursively visit both the childrens of every node once -> O(n) time as there are n nodes
    # We iterate over each edge once to visit all the all nodes, which again takes O(n) time as there are n-1 edges in the tree
# SPACE COMPLEXITY: O(n)
    # The recursion stack used by dfs can have no more than n elements in the worst-case scenario where each node is added to it -> It would take up O(n) space in that case

def longestZigZag(root):
    def maxZigzagPath(node, goLeft, max_path_len):
        if not node: 
            return max_path_len # if node is null, we have reached the end of the path, return max path length

        if goLeft: # if we went to the left child in the previous recursion of maxZigzagPath()
            max_path_len = max(
                                max_path_len, 
                                maxZigzagPath(node.right, False, max_path_len+1), # since we went left in the previous recursion, now we go right
                                maxZigzagPath(node.left, True, 0) # if we start the zigzag path from the current node, we must reset the max path length to 0
            ) # get the max path length
        
        else: # if we went to the right child in the previous recursion of maxZigzagPath()
            max_path_len = max(
                                max_path_len, 
                                maxZigzagPath(node.left, True, max_path_len+1), # since we went right in the previous recursion, now we go left
                                maxZigzagPath(node.right, False, 0) # if we start the zigzag path from the current node, we must reset the max path length to 0
            ) # get the max path length
        
        return max_path_len
    
    return max(maxZigzagPath(root.left, True, 0), maxZigzagPath(root.right, False, 0))

#==========================================================================================================

# ✅ ALGORITHM 1B: RECURSIVE DFS (ChatGPT solution)
# at each node, you track two things:
    # 1. The longest ZigZag path starting at this node and going left first
    # 2. The longest ZigZag path starting at this node and going right first
# For each node, you recursively calculate these values for its children, and then update the global maximum ZigZag path seen so far

def longestZigZag(root):
    # dfs() returns a tuple containing two integers:
        # 1. The longest ZigZag path going left first from the current node
        # 2. The longest ZigZag path going right first from the current node
    # It also updates the global variable 'max_length' to keep track of the longest path seen so far.
    def dfs(node):
        if not node:
            return (-1, -1)  # Base case: If the node is null, return (-1, -1) because we are one step before the starting node
        
        # Recursively find the longest ZigZag paths for the left and right children
        left_zigzag, right_zigzag = dfs(node.left), dfs(node.right)
        
        # The longest ZigZag path going left first at the current node is 1 + the ZigZag path going right first of its left child
        # Similarly, the longest ZigZag path going right first at the current node is 1 + the ZigZag path going left first of its right child
        curr_max_left = 1 + left_zigzag[1]
        curr_max_right = 1 + right_zigzag[0]
        
        # Update the global maximum length of the ZigZag path
        max_length[0] = max(max_length[0], curr_max_left, curr_max_right)
        
        # Return the tuple for the current node
        return (curr_max_left, curr_max_right)
    
    max_length = [0]  # Initialize the global maximum length of the ZigZag path
    dfs(root)  # Start the DFS from the root
    return max_length[0]  # Return the global maximum length