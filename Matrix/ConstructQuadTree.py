# https://leetcode.com/problems/construct-quad-tree/
# MEDIUM
# Tags: matrixlc, treelc, binarytreelc, designlc, #427

# GIVEN:
    # n * n matrix, grid, of 0's and 1's

# TASK:
    # Return the root of the Quad-Tree representing grid
    # Quad-tree = a tree where each non-leaf node has exactly 4 children
        # Each node has 2 properties: 
            # 1) val (node.val = 0 if node represents grid of all 0's; node.val = 1 if node represents grid of all 1's)
            # 2) isLeaf (node.isLeaf = 1 if node is leaf node; node.isLeaf = 0 otherwise)
        # Each non-leaf node also has 4 more properties: topLeft, topRight, bottomLeft, bottomRight (for its 4 children respectively)
    # To construct a quad-tree from a 2D array:
        # If all vals within current grid/subgrid are the same (i.e all 1's or all 0's), set isLeaf = 1 and set val = value of the grid and set the 4 children (topLeft, topRight, bottomLeft, bottomRight) to null and stop
        # If cells within current grid/subgrid have different values, set isLeaf = 0 and set val = any value and divide the current grid into 4 subgrids (which would represent its 4 children respectively)
        # Recurse for each of the children with the smaller subgrid

# EXAMPLES:
    # Input: grid = [[0,1],[1,0]]
    # Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
    # Explanation: The explanation of this example is shown below:
    # Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.

    # Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    # Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
    # Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
    # The topLeft, bottomLeft and bottomRight each has the same value.
    # The topRight have different values so we divide it into 4 sub-grids where each has the same value.

###########################################################################################################

# ✅ ALGORITHM 1: RECURSION
# Starting with original grid, check if all vals in grid are the same
    # If yes, create and return leaf node and end
    # If no, split grid into 4 subgrids and recursively pass each subgrid into the function
        # Create a root node and set its 4 children to the 4 nodes returned from the recursive function
# Return the root

# TIME COMPLEXITY: O(n^2 log n)
    # n^2 = max possible no. of leaf nodes (when every cell in grid is a leaf node)
    # log n = height of the resulting quad tree (since we divide n/2 for every level)
    # at every level in the tree, we are iterating over the entire tree
        # n^2 = original grid split into 4 quadrants -> check if all cells within each quadrant has the same value
        # n^2 = each 1/4 quadrant of original grid is split into 4 quadrants -> we have 4 smaller quadrants, but we still have to iterate each smaller quandrant to check if all values within a quadrant are the same
        # ...repeat the splitting until each quandrant has length = 1 -> total complexity = n^2 + n^2 + n^2 + ... = log n * n^2
# SPACE COMPLEXITY: O(log n)
    # the recurrence relation follows a binary tree structure, where each level of the tree represents a subproblem of size n/(2^k), where k is the level number
    # no. of levels in the tree = log(n) because the subproblem size reduces by half at each level

"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

def construct(grid):
    def buildTree(n, r, c): # n = length of current grid/subgrid, (r,c) = coords of topleft cell of current grid/subgrid
    # buildTree returns the subtree of the resulting root node
        
        # Check if all values in current grid/subgrid are the same
        all_same = True # initialize to True (i.e. all values in current grid/subgrid are the same)
        # iterate current grid/subgrid to find any values that are different
        for i in range(n):
            for j in range(n):
                if grid[r + i][c + j] != grid[r][c]: # if current cell's value is not same as value of 1st cell in current grid/subgrid
                    all_same = False
        
        if all_same: # if all vals in current grid/subgrid are the same, create a new node (which will be leaf) and return it (since it doesn't have further children)
            return Node(grid[r][c], 1) # node.val = grid[r][c], node.isLeaf = 1
        
        # if we reach this point, it means not all vals in current grid/subgrid are the same
        # so we split current grid into 4 subgrids and recurse

        n //= 2
        topLeft = buildTree(n, r, c) # top left quadrant
        topRight = buildTree(n, r, c + n) # top right quadrant
        bottomLeft = buildTree(n, r + n, c) # bottom left quadrant
        bottomRight = buildTree(n, r + n, c + n) # bottom right quadrant

        return Node(1, 0, topLeft, topRight, bottomLeft, bottomRight) # val = 1 (can be 0, doesn't matter), isLeaf = 0 (since it has 4 children, it's not leaf node)
    
    return buildTree(len(grid), 0, 0) # n = len(grid), (0,0) = coords of topleft cell of grid