# https://leetcode.com/problems/count-sub-islands/description/
# MEDIUM
# Tags: matrixlc, graphlc, dfslc

# GIVEN:
    # 2 m x n binary matrices, grid1 and grid2, containing only 0's (water) and 1's (land)

# TASK:
    # An island is a group of 1's connected 4-directionally
    # Any cells outside of the grid are considered water cells
    # An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2
    # Return the number of islands in grid2 that are considered sub-islands

# EXAMPLES:
    # Input: grid1 = [[1,1,1,0,0],
                    # [0,1,1,1,1],
                    # [0,0,0,0,0],
                    # [1,0,0,0,0],
                    # [1,1,0,1,1]], 

            # grid2 = [[1,1,1,0,0],
                    #  [0,0,1,1,1],
                    #  [0,1,0,0,0],
                    #  [1,0,1,1,0],
                    #  [0,1,0,1,0]]
    # Output: 3
    # Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
    # The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.

    # Input: grid1 = [[1,0,1,0,1],
                    # [1,1,1,1,1],
                    # [0,0,0,0,0],
                    # [1,1,1,1,1],
                    # [1,0,1,0,1]], 

            # grid2 = [[0,0,0,0,0],
                    #  [1,1,1,1,1],
                    #  [0,1,0,1,0],
                    #  [0,1,0,1,0],
                    #  [1,0,0,0,1]]
    # Output: 2 
    # Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
    # The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.

###########################################################################################################

# ✅ ALGORITHM 1: DFS ON GRID2, WHILE CHECKING IF GRID1's CELL IS LAND
# Create dfs(r,c) that does dfs on a land cell to find current island and mark them as visited
# do nested for loop over entire grid, run dfs() on the landcells (islands) in grid2 that are water cells in grid1
    # e.g. if grid2(r,c) is land but grid1(r,c) is water, use dfs() to mark current island at grid2(r,c) as visited so we don't consider them when finding sub-islands

# TIME COMPLEXITY: O(m*n)
    # dfs TC = O(V+E)
        # no. of vertices V = n * m
        # no. of edges E = ~ 4 * n * m
# SPACE COMPLEXITY: O(m*n)
    # in the worst case, when the whole grid is filled with 1's

def countSubIslands(grid1, grid2):
    rows, cols = len(grid1), len(grid1[0])
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False # out of bounds
        if grid2[r][c] != 1: 
            return False # if grid(r,c) is not land and hasn't been visited

        grid2[r][c] = 'v' # mark as visited

        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)
        
        return True

    # removing all non-common islands by marking them visited
        # if grid2(r,c) is land but grid1(r,c) is water, mark the current island in grid2(r,c) as visited (not considered as sub-island)
    for r in range(rows):
        for c in range(cols):
            if grid2[r][c] == 1 and grid1[r][c] == 0:
                dfs(r, c)

    # count no. of sub-islands
    sub_islands = 0
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c): 
                sub_islands += 1 # dfs(r,c) returns true, we finished visiting current subisland and marking it visited
    
    return sub_islands