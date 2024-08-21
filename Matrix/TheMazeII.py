# 505. The Maze II
# https://leetcode.com/problems/the-maze-ii/
# MEDIUM
# Tags: matrixlc, bfslc, premiumlc, dijkstralc, dijkstraslc, heaplc, minheaplc, #505

# There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
# Given the m x n maze, the ball's start position and the destination, where start = [start_row, start_col] and destination = [destination_row, destination_col], return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.
# The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).
# You may assume that the borders of the maze are all walls (see examples).

# EXAMPLES:
    # Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
    # Output: 12
    # Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
    # The length of the path is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

    # Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
    # Output: -1
    # Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
        
    # Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
    # Output: -1

###########################################################################################################

# ✅✅✅ ALGORITHM 1: BFS + DIJKSTRA'S ALGORITHM (my solution)
# in a min-heap, for each cell that is visited, add (distance_from_src, r, c)
    # distance_from_src = distance between current cell and source cell
    # r,c = coords of current cell
# every time a cell with the shortest distance from src is popped, add it to the visited set
# for each current cell (r,c) stored in the min heap, we check its 4 neighbors and keep rolling the ball while it is within bounds and not hitting a wall
# if the destination is reached, return the distance_from_src (this will be the shortest distance)

# TIME COMPLEXITY: O(m * n * max(m,n))
    # m = number of rows, n = number of columns
    # worst case: we visit each cell once (since BFS explores the maze level by level and marks cells as visited, no cell will be processed more than once) -> O(m*n)
    # For each cell, the inner while loop rolls in one of the four possible directions until it hits a wall. In the worst case, this could take O(max(m,n)) time for each direction
    # -> overall TC = O(m * n * max(m,n))
        # NOTE: the TC for this is greater than TC for 490. The Maze because in THIS question (Djikstra's approach), each cell might be considered multiple times until its shortest path is confirmed. This leads to the need for more heap operations, which increases the overall complexity
            # Whereas in 490. The Maze, once a cell is processed, it's NEVER revisited. The BFS approach processes each cell at most once. The while loop that rolls the ball across the maze still runs, but because no cell is revisited, the total number of cells processed, and hence the total number of operations, is proportional to the total no. of cells m*n
# SPACE COMPLEXITY: O(m*n)
    # for heap and visited set
    # heap and visited set each stores up to m*n cells in the worst case

from heapq import heappop, heappush

def shortestDistance(maze, start, destination):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    min_heap = [ (0, start[0], start[1]) ] # (distance_from_src, r, c)

    while min_heap:
        dist_from_src, r, c = heappop(min_heap)
        if [r,c] == destination:
            return dist_from_src
        visited.add((r,c)) # *****

        for x, y in [(0,-1), (0,1), (-1,0), (1,0)]:
            nr, nc = x, y
            # keep rolling the ball until it gets out of bounds/hits a wall
            while 0 <= nr+x < rows and 0 <= nc+y < cols and maze[nr+x][nc+y] == 0:
                nr += x
                nc += y
            if (nr,nc) not in visited:
                heappush(min_heap, (dist_from_src+abs(nr-r)+abs(nc-c), nr, nc)) # dist_from_src+abs(nr-r)+abs(nc-c) is the new distance between src and cell (nr,nc)
    
    return -1

# ***** WHY SHOULD THE LINE "visited.add((r,c))" be added after each heappop, instead of added after each heappush at the end?
    # ! The key point of Dijkstra's algorithm is that a node/cell should only be marked as visited once the shortest path to it has been confirmed
    # in the above correct code, cell (r, c) is only marked as visited after it has been popped from the min_heap, meaning the shortest distance to this cell has already been confirmed. This ensures that the algorithm explores all possible paths and only marks a cell as visited when the shortest path to it has been determined
    # if the line "visited.add((r,c))" is added after the heappush line, the problem is that other paths might lead to this same cell (nr, nc) with a shorter distance. However, since the cell is already marked as visited, those potentially shorter paths will never be explored, leading to suboptimal or incorrect results

#==========================================================================================================

# ✅ ALGORITHM 2: DFS

# WIP