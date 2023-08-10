# https://leetcode.com/problems/rotting-oranges/
# MEDIUM
# Tags: bfslc, graphlc, matrixlc, #994

# GIVEN:
    # an m x n grid where each cell can have one of three values:
        # 0 representing an empty cell,
        # 1 representing a fresh orange, or
        # 2 representing a rotten orange

# TASK:
    # Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten
    # Return the minimum no. of minutes that must elapse until no cell has a fresh orange
    # If this is impossible, return -1

# EXAMPLES:
    # Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    # Output: 4

    # Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    # Output: -1
    # Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

    # Input: grid = [[0,2]]
    # Output: 0
    # Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

###########################################################################################################

# ✅ ALGORITHM: ITERATIVE BFS
# First, iterate through all cells in grid to add all rotten oranges to q
    # also keep track of the no. of fresh oranges, since our objective is to find the minimum time required for all fresh oranges to be rotten
# Use a counter to keep track of no. of minutes
# while q is not empty and no. of fresh oranges > 0:
    # for each BFS level,
        # pop first item from q
        # for each of its 4 neighbors (of the cell popped),
            # if neighbor is within bounds of grid and is fresh orange,
                # mark it as rotten, no. of fresh oranges - 1
                # add this neihgbor to q
    # increment counter for no. of minutes (we increment after the for-loop because after each iteration of for-loop ends, the remaining elements in q would be from the 2nd bfs layer)
# after the while loop, q would be empty; if there are still fresh oranges in grid, return -1
# if there are no fresh oranges, that means all fresh oranges are now rotten -> return minutes counter

# TIME COMPLEXITY: O(m*n)
    # m = number of rows
    # n = number of columns
    # In the worst-case scenario, we may have to visit O(m⋅n) cells before the iteration stops
# SPACE COMPLEXITY: O(max(m,n))
    # because this is bfs, in the worst case, the q can either store all cells in the row or all cells in the column -> overall space complexity = O(max(m,n))

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    q = []
    minutes = 0 # counter for no. of minutes that have passed
    fresh = 0 # no. of fresh oranges counter

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r,c)) # if orange is rotten, add to queue
            elif grid[r][c] == 1:
                fresh += 1 # if orange is fresh, increment fresh oranges counter
    
    while q and fresh > 0: # while q is not empty and there are still fresh oranges in grid,
        for _ in range(len(q)): # for current bfs layer
            r, c = q.pop(0)
            for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # iterate 4 neighbors of popped cell
                nr, nc = r + x, c + y
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1: # if neighbor is within bounds of grid and it is a fresh orange
                    grid[nr][nc] = 2 # make it a rotten orange
                    fresh -= 1 # since it's rotten, fresh oranges -1
                    q.append((nr, nc)) # add this neighbor to q
        minutes += 1 # increment minutes counter; at this point (i.e. at the end of current iteration of for loop, all elements left in q are from the next bfs layer)
    
    return minutes if fresh == 0 else -1 # if there are still fresh oranges left on grid, return -1 as we cannot make them rot