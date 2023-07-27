# https://leetcode.com/problems/shortest-bridge/description/
# MEDIUM
# Tags: graphlc, bfslc, dfslc, matrixlc

# GIVEN:
    # an n x n binary matrix, grid, where 1 represents land and 0 represents water
    # An island is a 4-directionally connected group of 1's not connected to any other 1's
    # There are exactly 2 islands in grid

# TASK:
    # You may change 0's to 1's to connect the two islands to form one island
    # Return the smallest number of 0's you must flip to connect the two islands

# EXAMPLES:
    # Input: grid = [[0,1],[1,0]]
    # Output: 1

    # Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
    # Output: 2

    # Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    # Output: 1

###########################################################################################################

# ✅ ALGORITHM 1: DFS + BFS
# Question is basically asking for the shortest path between the 2 islands
# After doing DFS to get all coords of land cells of the 1st island, do BFS to get shortest path between 2 islands
    # BFS lets us get the layers that are 4-directionally surrounding the 1st island
    # As we get each layer, we increase our bridge length by 1
    # When any cell from the 2nd island falls within a layer, we return our bridge length
# NOTE: we don't need to visit 2nd island or do DFS for it, since we just need to find bridge length between the 2 islands, so we return bridge length as soon as any cells from 2nd island falls within the BFS layers that we get from the BFS function

# TIME COMPLEXITY: O(n^2)
    # nested for-loop iterating grid
# SPACE COMPLEXITY: O(n^2)
    # for visited hashset and BFS queue

def shortestBridge(grid):
    n = len(grid) # n x n grid has same no. of rows and cols (i.e. rows = cols = n)
    visited = set() # after DFS, visited would contain all coordinates (x, y) of the 1st island
        # e.g. visited = { (x, y), (i, j), ... }

    def dfs(r, c): # DFS to get all coordinates of an island
    # DFS doesn't return anything, just fills up visited hashset with coords of land cells of 1st island
        if r < 0 or r >= n or c < 0 or c >= n:
            return
        if grid[r][c] != 1: # if grid(r,c) is not land
            return
        if (r,c) in visited: # if grid(r,c) has been visited
            return

        visited.add((r,c)) # add

        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)

    def bfs(q): # BFS finds shortest bridge length between 2 islands
    # this function uses the visited hashset as it is the set of coords of our first island's cells
    # but we must convert visited hashset into array as we cannot pop from a hashset
        bridge_len = 0 # return value; this will be the shortest bridge length between the 2 islands
        while q:
            for _ in range(len(q)): # every iteration of the for-loop finishes iterating 1 layer of the surrounding nodes of the 1st island
                r, c = q.pop()

                # visit all 4 neighbors by layers
                for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    curr_r, curr_c = r + x, c + y # curr_r, curr_c are grid(r,c)'s neighbors' coords
                    if curr_r < 0 or curr_r >= n or curr_c < 0 or curr_c >= n or (curr_r, curr_c) in visited: # if curr_r and/or curr_c is out of bounds, OR, grid(curr_r, curr_c) is already visited:
                        continue # skip current neighbor and visit the next one
                    if grid[curr_r][curr_c] == 1: # if current neighbor is a land cell (i.e. it would be part of the 2nd island)
                        return bridge_len # we found a cell of the 2nd island, means we reached the 2nd island with our bridge
                    q.append((curr_r, curr_c)) # we add current neighbor to our queue bc it's water and we want to continue finding a bridge path on water
                    visited.add((curr_r, curr_c)) # add current neighbor to visited so we don't visit again
            
            bridge_len += 1 # increment bridge_len outside the 1st for-loop since every finished iteration of the 1st for-loop means we finished iterating another layer of 1st island's neighbors
    
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1: # if current cell is land (i.e. we're at the 1st island)
                dfs(r,c) # fill up visited hashset with coords of all cells of FIRST island
                return bfs(list(visited)) # convert hashset visited to array since the q in bfs(q) must be an array as we cannot pop from hashsets