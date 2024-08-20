# 490. The Maze
# https://leetcode.com/problems/the-maze/
# MEDIUM
# Tags: bfslc, matrixlc, dfslc, premiumlc, #490

# There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
# Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.
# You may assume that the borders of the maze are all walls (see examples).

# EXAMPLES:
    # Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
    # Output: true
    # Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

    # Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
    # Output: false
    # Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
        
    # Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
    # Output: false

###########################################################################################################

# ✅✅✅ ALGORITHM 1: BFS
# for each cell (r,c) stored in the queue, we check its 4 neighbors and keep rolling the ball while it is within bounds and not hitting a wall
# check that the cell reached by the ball is not in visited set (to prevent cycles in the maze)
# if the destination is reached, return True

# TIME COMPLEXITY: O(m*n)
    # m = number of rows, n = number of columns
    # worst case: we visit each cell once (since BFS explores the maze level by level and marks cells as visited, no cell will be processed more than once)
    # When processing a cell, all 4 directions are explored. Each direction is processed independently, but the total no. of operations is still bounded by the no. of cells because each cell is only visited once
    # -> TC = no. of cells in the maze
# SPACE COMPLEXITY: O(m*n)
    # for queue and visited set
    # queue and visited set each stores up to m*n cells in the worst case

from collections import deque

def hasPath(maze, start, destination):
    rows, cols = len(maze), len(maze[0])
    q = deque([(start[0], start[1])]) # q = [ (start[0], start[1]), ... ]
    visited = set()

    while q:
        r, c = q.popleft()
        visited.add((nr, nc))
        if [r,c] == destination:
            return True # we reached the destination

        for x, y in [(0,-1), (0,1), (-1,0), (1,0)]:
            nr, nc = r, c # new coords of the ball after rolling
            while 0 <= nr+x < rows and 0 <= nc+y < cols and maze[nr+x][nc+y] == 0:
                # keep rolling the ball in the same direction as long as it is within bounds and not hitting a wall
                nr += x
                nc += y
            if (nr, nc) not in visited:
                q.append((nr, nc))
    
    return False # if this line is reached, it means destination was never reached

#==========================================================================================================

# ✅ ALGORITHM 2: DFS

# TIME COMPLEXITY: O(m*n)
    # m = number of rows, n = number of columns
    # worst case: we visit each cell once (since DFS explores the maze level by level and marks cells as visited, no cell will be processed more than once)
    # When processing a cell, all 4 directions are explored. Each direction is processed independently, but the total no. of operations is still bounded by the no. of cells because each cell is only visited once
    # -> TC = no. of cells in the maze
# SPACE COMPLEXITY: O(m*n)
    # O(m*n) for visited set (stores up to m*n cells in the worst case)
    # O(m*n) for recursion stack

def hasPath(maze, start, destination):
    rows, cols = len(maze), len(maze[0])
    visited = set()

    def dfs(r,c):
        if [r,c] == destination:
            return True
        if (r,c) in visited:
            return False
        
        visited.add((r,c))
        for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nr, nc = r, c
            while 0 <= nr+x < rows and 0 <= nc+y < cols and maze[nr+x][nc+y] == 0: # while ball is within bounds and not hitting a wall
                nr += x
                nc += y
            if dfs(nr, nc):
                return True
        
        return False
    
    return dfs(start[0], start[1])