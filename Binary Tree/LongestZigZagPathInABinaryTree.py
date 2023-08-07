# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/
# MEDIUM
# Tags: binarytreelc, dfslc, #1372

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

# ✅ ALGORITHM: RECURSIVE DFS
# dfs() function keeps track of whether we traversed to the current node's left child or right child
# if we traversed to the left child, in the next recursion of dfs(), we should traverse to the right child, and vice versa
# dfs() also keeps track of the longest zigzag path so far
# to start the zigzag path from non-root nodes, we can simply reset the longest zigzag path length to 0 and go the child node that is not part of the zigzag direction
    # e.g. if the longest zigzag path is on the right of the root node but the root node cannot access this longest zigzag path because we need to go take 2 right directions, then:
        # from root, go to the right (root.right is the starting node of this longest zigzag path), then go to the right again to continue the path but reset longest zigzag path length to 0

# TIME COMPLEXITY: O(n)
    # we recursively visit both the childrens of every node once -> O(n) time as there are n nodes
    # We iterate over each edge once to visit all the all nodes, which again takes O(n) time as there are n-1 edges in the tree
# SPACE COMPLEXITY: O(n)
    # The recursion stack used by dfs can have no more than n elements in the worst-case scenario where each node is added to it -> It would take up O(n) space in that case

def longestZigZag(root):
    def dfs(node, goLeft, max_zigzag_path_len):
        if not node: return max_zigzag_path_len

        if goLeft: # if we went to the left child in the previous recursion of dfs()
            max_zigzag_path_len = max(
                                    max_zigzag_path_len, 
                                    dfs(node.right, False, max_zigzag_path_len+1), # since we went left in the previous recursion of dfs(), now we go right
                                    dfs(node.left, True, 0) # if we start the zigzag path from the current node, we must reset the max path length to 0
            ) # get the max path length
        
        else: # if we went to the right child in the previous recursion of dfs()
            max_zigzag_path_len = max(
                                    max_zigzag_path_len, 
                                    dfs(node.left, True, max_zigzag_path_len+1), # since we went right in the previous recursion of dfs(), now we go left
                                    dfs(node.right, False, 0) # if we start the zigzag path from the current node, we must reset the max path length to 0
            ) # get the max path length
        
        return max_zigzag_path_len
    
    return max(dfs(root.left, True, 0), dfs(root.right, False, 0))