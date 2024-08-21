# 1197. Minimum Knight Moves
# https://leetcode.com/problems/minimum-knight-moves/
# MEDIUM
# Tags: bfslc, dfslc, premiumlc, #1197

# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
# https://imgur.com/ozn2z0G
# Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

# EXAMPLES:
    # Input: x = 2, y = 1
    # Output: 1
    # Explanation: [0, 0] → [2, 1]

    # Input: x = 5, y = 5
    # Output: 4
    # Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

###########################################################################################################

# ✅✅✅ ALGORITHM 1: BFS
# since we are trying to find the shortest path between two nodes in a graph, we should use BFS
# ! MAIN IDEA: starting from the origin, we explore the neighborhood following the order that is determined by the distance to the origin, i.e. we first explore all the points within a single step from the origin, then we explore all the points that can be reached with two steps, so on and so forth. During the exploration process, as soon as we reach the target point, we then can call the current path the shortest path, since our exploration follows the order of distance.
# STEPS:
    # 1. create a queue data structure to store the places to be visited during the next step and a set data structure named visited to keep track of all the places that we have visited so far
    # 2. The process of BFS consists of a loop that spins around the queue. The loop ends either when we reach the target or when the queue is empty
    # 3. Within the main loop, we use a nested loop to iterate over the current elements in the queue. All of the elements are of the same distance from the starting point
    # 4. Within the nested loop, we prepare the elements that will be visited during the next step

from collections import deque

def minKnightMoves(x, y):
    q = deque([(0, 0)]) # (r,c)
    visited = set()
    steps = 0 # return value
    
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            if (r,c) == (x,y):
                return steps
            
            for x_dir, y_dir in [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]:
                nr, nc = r + x_dir, c + y_dir
                if (nr,nc) not in visited:
                    visited.add((nr,nc))
                    q.append((nr,nc))
        steps += 1 # once we reach this point, it means we finished processing another 1 layer (all directions) around the knight

#==========================================================================================================

# ✅✅ ALGORITHM 2: DFS (better TC)
# ! MAIN IDEA: since the board is vertically, horizontally and diagonally symmetric, the target (x,y), its horizontally, vertically, and diagonally symmetric points (i.e. (x,−y),(−x,y),(−x,−y)) share the same answer as the target point
# Based on the above insight, we can focus on the first quadrant of the coordinate plane where both x and y are positive
    # Any target that is outside of the first quadrant, can be shifted to its symmetric point in the first quadrant by taking the absolute value of each coordinate, i.e. (∣x∣,∣y∣)

# WIP