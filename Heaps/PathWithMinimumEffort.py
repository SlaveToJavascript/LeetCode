# https://leetcode.com/problems/path-with-minimum-effort/description/
# MEDIUM
# Tags: bfslc, heaplc, minheaplc, #1631

# GIVEN:
    # array heights, a 2D array of size rows x columns

# TASK:
    # You are situated in the top-left cell and you hope to travel to the bottom-right cell
    # You can move up, down, left, or right
    # TODO: find a route that requires the minimum effort and return the minimum effort of that path
        # a path's effort = max. absolute difference in values between 2 consecutive cells in the path

# EXAMPLES:
    # Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
    # Output: 2
    # Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
    # This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

    # Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
    # Output: 1
    # Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

    # Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    # Output: 0
    # Explanation: This route does not require any effort.

###########################################################################################################

# ✅ ALGORITHM: ITERATIVE BFS + MIN HEAP
# Iterative BFS is used to find minimum path sums (for this question, we are finding minimum effort instead)
# Min heap is used to always pop out the neighbor with the smallest difference, so that we prioritize and firstly visit neighbors that have smallest differences
# Once we pop out the cell at the last row last col (i.e. detination cell), we return the minimum effort
    # Otherwise, if popped cell is not destination, we visit all 4 neighbors of popped cell and add them to queue
    # keep track of visited cells so that we don't visit them again 

# TIME COMPLEXITY: O(m*n log(m*n))
    # each push/pop operation is O(log(m*n))
    # in the worst case, we can push to heap m*n times (1 for each cell)
    # -> Overall TC = O(m*n log(m*n))
# SPACE COMPLEXITY: O(m*n)
    # heap has max m*n cells

from heapq import heappop, heappush

def minimumEffortPath(heights):
    rows, cols = len(heights), len(heights[0])
    min_heap = [(0, 0, 0)] # (diff, r, c)
    visited = set()

    while min_heap:
        diff, r, c = heappop(min_heap)
        if (r, c) in visited:
            continue
        
        visited.add((r,c))
        if r == rows-1 and c == cols-1: # if popped cell is destination cell, return min. diff
            return diff
        
        for x, y in (-1, 0), (1, 0), (0, -1), (0, 1): # visit all 4 neighbors
            nr, nc = r + x, c + y # coords of neighbor cell
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited: # if neighbor cell is out of bounds or has already been visited
                continue
            
            max_diff = max(diff, abs(heights[r][c] - heights[nr][nc])) # if difference between current neighbor and popped cell is greater than diff, update max_diff
            heappush(min_heap, (max_diff, nr, nc)) # add current neighbor to heap