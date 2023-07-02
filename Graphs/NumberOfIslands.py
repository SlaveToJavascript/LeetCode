# https://leetcode.com/problems/number-of-islands/
# MEDIUM

# GIVEN:
    # m x n 2D binary grid, grid, which represents a map of '1's (land) and '0's (water)

# TASK:
    # return the number of islands
        # An island is surrounded by water and formed by connecting adjacent lands
        # You may assume all four edges of the grid are all surrounded by water

# EXAMPLES:
    # Input: grid = [
    #   ["1","1","1","1","0"],
    #   ["1","1","0","1","0"],
    #   ["1","1","0","0","0"],
    #   ["0","0","0","0","0"]
    # ]
    # Output: 1

    # Input: grid = [
    #   ["1","1","0","0","0"],
    #   ["1","1","0","0","0"],
    #   ["0","0","1","0","0"],
    #   ["0","0","0","1","1"]
    # ]
    # Output: 3

###########################################################################################################

# ✅✅ ALGORITHM 1: RECURSIVE DFS
# nested for loop to visit each node and call recursive dfs function on each node
# recursive dfs function returns false if node is out of bounds, or is water, or is visited
# returns True after it finishes traversing an island
    # if true is returned, number of islands +1

# TIME COMPLEXITY: O(mn)
# SPACE COMPLEXITY: O(mn)

def numIslands(grid):
    # recursive dfs
    def dfs(grid, r, c, visited):
        # if current row and/or column is out of bounds
        if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[0])): return False
        if grid[r][c] == "0": return False # if current node is water
        if (r,c) in visited: return False # if current node in visited
        visited.add((r,c)) # add current node to visited in the form of "r,c"

        # visit all the 4 nodes surrounding each node
        dfs(grid, r+1, c, visited)
        dfs(grid, r-1, c, visited)
        dfs(grid, r, c+1, visited)
        dfs(grid, r, c-1, visited)
        
        return True # if True is returned, it means I finished expanding a new island

    visited = set()
    island_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if dfs(grid, row, col, visited): island_count += 1 # True means I finished expanding a new island
    return island_count

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: RECURSIVE DFS OPTIMIZED (WITHOUT VISITED)
# Instead of maintaining a visited set, mark islands that are visited and not visit them again

def numIslands(grid):
    # recursive dfs
    def dfs(grid, r, c):
        # if current row and/or column is out of bounds
        if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[0])): return False
        if grid[r][c] != "1": return False # if current node is water OR is visited
        grid[r][c] = 'v' # mark current node as visited

        # visit all the 4 nodes surrounding each node
        dfs(grid, r+1, c)
        dfs(grid, r-1, c)
        dfs(grid, r, c+1)
        dfs(grid, r, c-1)
        
        return True # if True is returned, it means I finished expanding a new island

    island_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if dfs(grid, row, col): island_count += 1 # True means I finished expanding a new island
    return island_count

#==========================================================================================================

# ✅ ALGORITHM 3: ITERATIVE BFS
