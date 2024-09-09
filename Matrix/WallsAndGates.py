# 286. Walls and Gates
# https://leetcode.com/problems/walls-and-gates/
# MEDIUM
# Tags: matrixlc, bfslc, premiumlc, #286 

# GIVEN:
    # an m x n grid rooms initialized with these three possible values.
        # -1 : A wall or an obstacle.
        # 0 : A gate.
        # INF : Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

# TASK:
    # Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF
    # NOTE: Do not return anything, modify rooms in-place instead

# EXAMPLES:
    # Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    # Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

    # Input: rooms = [[-1]]
    # Output: [[-1]]

###########################################################################################################

# ✅ ALGORITHM: BFS
# since we are finding distance between each empty room and its nearest GATE, gate is the source from where we start each BFS
# iterate matrix to find each gate and add it to queue
# since a gate is marked as 0, for each neighbor, change its value (i.e. distance from gate) to matrix[r][c] + 1 (i.e. value of gate cell = 0 + 1 = distance from gate to neighbor)
# enqueue each neighbor into queue and for each popped cell, find its neighbors and update the distance
# NOTE: visited set is not required since matrix is modified in-place -> anything that is not INFINITY is considered visited (i.e. need not be processed)

# TIME COMPLEXITY: O(m*n)
    # BFS visits each cell at most once
# SPACE COMPLEXITY: O(m*n)
    # queue holds at most m*n cells

from collections import deque

def wallsAndGates(rooms):
    rows, cols = len(rooms), len(rooms[0])

    # iterate matrix to find each gate and add it to a queue
    q = deque()
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                q.append((r,c))
    
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    while q:
        r, c = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == 2147483647: # NOTE: 2147483647 represents float('inf')
                rooms[nr][nc] = rooms[r][c] + 1 # increment distance from nearest gate by 1
                q.append((nr,nc))