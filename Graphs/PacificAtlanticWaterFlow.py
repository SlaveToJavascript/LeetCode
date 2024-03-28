# 417. Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# MEDIUM
# Tags: grapflc, dfslc, #417

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean
    # The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height
    # Water can flow from any cell adjacent to an ocean into the ocean.
# TODO: Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans

# EXAMPLES:
    # Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    # Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    # Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
    # [0,4]: [0,4] -> Pacific Ocean 
    #        [0,4] -> Atlantic Ocean
    # [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
    #        [1,3] -> [1,4] -> Atlantic Ocean
    # [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
    #        [1,4] -> Atlantic Ocean
    # [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
    #        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
    # [3,0]: [3,0] -> Pacific Ocean 
    #        [3,0] -> [4,0] -> Atlantic Ocean
    # [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
    #        [3,1] -> [4,1] -> Atlantic Ocean
    # [4,0]: [4,0] -> Pacific Ocean 
    #        [4,0] -> Atlantic Ocean
    # Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
        
    # Input: heights = [[1]]
    # Output: [[0,0]]
    # Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE DFS
# For each cell (r,c), we check if it's accessible to the Atlantic Ocean and we check if it's accessible to the Pacific Ocean
    # so for each cell (r,c), we traverse in 4 directions and see if it can reach the (right OR bottom border) for Atlantic Ocean AND the (top OR left border) for Pacific Ocean
# if it's possible, we add this cell (r,c) to the result array

# TIME COMPLEXITY: O((m*n)^2) ❌

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: ITERATIVE BFS
# we need to maintain a different set of visited hashset + queue for each ocean
    # ❌ single queue for both oceans: mix up the flow directions, as the water flow towards each ocean is handled independently
    # having a different visited set for each ocean makes it easier to track which are the respective target cells that can reach the respective ocean
        # the respective visited set holds the target cells that can reach the respective ocean!

# TIME COMPLEXITY: O(m * n) ✅
    # worst case: each cell is visited once per ocean
    # checking each cell's neighbors and determining if it can flow into either ocean involves constant time checks and updates per cell
# SPACE COMPLEXITY: O(m * n)
    # worst case: visited stores every cell in the matrix twice (once for each ocean) -> O(m * n)
    # worst case: result takes O(m * n) space

def pacificAtlantic(heights):
    rows, cols = len(heights), len(heights[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(cells): # cells is an array of cells from which BFS should commence from (in this context, they should be the border cells)
        visited = set(cells)
        q = cells # NOTE: cells input should be a list

        while q:
            r,c = q.pop(0)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]: # if (nr,nc) is a valid cell that can reach the respective ocean,
                    visited.add((nr, nc))
                    q.append((nr, nc))
        
        return visited # visited set holds the target cells that can reach the respective ocean!
    
    # cells bordering the Pacific Ocean and Atlantic Ocean -> we start BFS from these cells as they can definitely reach the respective ocean
    pacific_starts = [(0,c) for c in range(cols)] + [(r, 0) for r in range(rows)]
    atlantic_starts = [(rows-1,c) for c in range(cols)] + [(r, cols-1) for r in range(rows)]

    # bfs() returns the target cells that can reach the respective ocean
    pacific_reachable = bfs(pacific_starts)
    atlantic_reachable = bfs(atlantic_starts)

    return list(pacific_reachable.intersection(atlantic_reachable)) # we only return cells that can reach BOTH oceans -> return intersection of the 2 sets

#==========================================================================================================

# ✅ ALGORITHM 3: RECURSIVE DFS
# We know the border cells can definitely reach one or both oceans, so we start from border cells and do DFS from those cells to identify which neighbor nodes can reach the respective oceans
    # if we start from border cells and look inward for neighbor cells that can access the ocean, we're looking for INCREASE in height
# when we get to a visited cell, we do not visit it again

# TIME COMPLEXITY: O(m * n) ✅
    # each cell is visited once
# SPACE COMPLEXITY: O(m * n)
    # recursion call stack (worst case: m*n) + visited sets for both oceans (worst case: keep track of each cell 2x – once for each ocean)

def pacificAtlantic(heights):
    rows, cols = len(heights), len(heights[0])

    def dfs(r, c, visited, prev_height):
        if ((r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prev_height): # if current cell has been visited or out of bounds or cannot reach the respective ocean
            return
        
        visited.add((r, c))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            dfs(r + dr, c + dc, visited, heights[r][c]) # this is to fill up visited set (i.e. pacific_reachable and atlantic_reachable)

    pacific_reachable = set()
    atlantic_reachable = set()

    # start DFS from top and bottom cells
    for c in range(cols):
        dfs(0, c, pacific_reachable, heights[0][c]) # top edge (Pacific Ocean)
        dfs(rows-1, c, atlantic_reachable, heights[rows - 1][c]) # bottom edge (Atlantic Ocean)

    # start DFS from left and right border cells
    for r in range(rows):
        dfs(r, 0, pacific_reachable, heights[r][0]) # left edge (Pacific Ocean)
        dfs(r, cols - 1, atlantic_reachable, heights[r][cols - 1]) # right edge (Atlantic Ocean)

    return list(pacific_reachable & atlantic_reachable) # cells that can reach both oceans