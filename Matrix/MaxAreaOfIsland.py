# https://leetcode.com/problems/max-area-of-island/
# MEDIUM
# Tags: matrixlc, graphlc, dfslc

# GIVEN:
    # m x n 2D binary grid, grid, which represents a map of '1's (land) and '0's (water)
    # You may assume all four edges of the grid are surrounded by water

# TASK:
    # Return the maximum area of an island in grid
    # The area of an island is the number of cells with a value 1 in the island

# EXAMPLES:
    # Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                #    [0,0,0,0,0,0,0,1,1,1,0,0,0],
                #    [0,1,1,0,1,0,0,0,0,0,0,0,0],
                #    [0,1,0,0,1,1,0,0,1,0,1,0,0],
                #    [0,1,0,0,1,1,0,0,1,1,1,0,0],
                #    [0,0,0,0,0,0,0,0,0,0,1,0,0],
                #    [0,0,0,0,0,0,0,1,1,1,0,0,0],
                #    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    # Output: 6
    # Explanation: The answer is not 11, because the island must be connected 4-directionally.

    # Input: grid = [[0,0,0,0,0,0,0,0]]
    # Output: 0

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS
# nested for loop to visit each node and call recursive dfs function on each node
# recursive dfs function returns 0 if node is out of bounds, or is water, or is visited
# returns size after it finishes traversing an island

# TIME COMPLEXITY: O(mn)
# SPACE COMPLEXITY: O(mn)

def maxAreaOfIsland(grid):
    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]): 
            return 0 # if r, c out of bounds
        if grid[r][c] != 1: 
            return 0 # if current node is water or is visited (i.e. is not land)
        
        grid[r][c] = 'v' # mark current node as visited
        size = 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1) # the 1 is for current node
        
        return size

    max_size = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            max_size = max(max_size, dfs(r, c))
    return max_size