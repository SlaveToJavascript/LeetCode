# https://leetcode.com/problems/detonate-the-maximum-bombs/description/
# MEDIUM
# Tags: dfslc, graphlc

# GIVEN:
    # a 2D list of bombs, where the ith bomb i.e. bombs[i] = [x, y, r], where x,y are coords of the bomb and r is the radius of the range of the bomb
        # range of a bomb is defined as the area where its effect can be felt
        # This area is in the shape of a circle with the center as the location of the bomb

# TASK:
    # You may choose to detonate only a single bomb
    # When a bomb is detonated, it will detonate all bombs that lie in its range
    # These bombs will further detonate the bombs that lie in their ranges
    # return the max no. of bombs that can be detonated if you are allowed to detonate only one bomb

# EXAMPLES:
    # Input: bombs = [[2,1,3],[6,1,4]]
    # Output: 2
    # Explanation:
    # The above figure shows the positions and ranges of the 2 bombs.
    # If we detonate the left bomb, the right bomb will not be affected.
    # But if we detonate the right bomb, both bombs will be detonated.
    # So the maximum bombs that can be detonated is max(1, 2) = 2.

    # Input: bombs = [[1,1,5],[10,10,5]]
    # Output: 1
    # Explanation:
    # Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.

    # Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
    # Output: 5
    # Explanation:
    # The best bomb to detonate is bomb 0 because:
    # - Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
    # - Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
    # - Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
    # Thus all 5 bombs are detonated.

###########################################################################################################

# ✅ ALGORITHM 1: DFS WITH ADJACENCY LIST
# Create an adjacency list, where key = i (for the ith bomb) and value = list of bombs that the ith bomb can reach
# Iterate the bombs list, find the distance between each pair of bombs to find out if any 1 (or both) of the pair of bombs can reach the other, given its range
    # if ith bomb can reach another jth and kth bombs, add j and k to the array value of i
    # i.e. adjList[i] = [j, k]
# Define dfs(i) that returns the no. of bombs that ith bomb can detonate in sequence (one after another) by making use of the adjacency list
# iterate bombs array again, and run dfs(i) on each ith bomb, while tracking the max no. of bombs that an ith bomb can detonate
# Return this max number

# TIME COMPLEXITY: O(n^3)
    # 1st for-loop: O(n^2)
    # dfs: O(n^2)
        # time complexity of dfs = O(V+E)
        # no. of vertices V = no. of bombs = n
        # max no. of edges E = n^2 (since graph is directed)
    # last for-loop: O(n^3)
        # O(n) for the for-loop * O(n^2) for dfs
# SPACE COMPLEXITY: O(n^2)
    # max no. of edges = n^2

import math

def maximumDetonation(bombs):
    adjList = {}

    for i in range(len(bombs)):
        if i not in adjList: adjList[i] = []
        for j in range(i+1, len(bombs)):
            if j not in adjList: adjList[j] = []

            x1, y1, r1 = bombs[i]
            x2, y2, r2 = bombs[j]
            distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            if r1 >= distance: # bombs[i] can reach bombs[j]
                adjList[i].append(j)
            if r2 >= distance: # bombs[j] can reach bombs[i]
                adjList[j].append(i)

    # dfs() returns the no. of bombs that bombs[i] can detonate one after another
    def dfs(i, visited):
        # every bombs[i] would have a different visited list as visited is the list of bombs detonated by i
        if i in visited: return 0
        visited.add(i)
        
        for neighbor in adjList[i]:
            dfs(neighbor, visited)
        
        return len(visited)
    
    max_detonated = 0 # return value; the max no. of bombs detonated by any bombs[i]
    for i in range(len(bombs)):
        max_detonated = max(max_detonated, dfs(i, set()))
    
    return max_detonated