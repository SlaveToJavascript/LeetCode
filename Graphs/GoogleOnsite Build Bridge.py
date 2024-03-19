# GOOGLE ON-SITE TECHNICAL INTERVIEW QUESTION
# 21 August 2023
# Tags: bfslc, graphlc, google, interviewlc

# We are trying to build a bridge across an m x n river
# Each day, we build a bridge cell on the river. The bridge cell can be anywhere on the river and does not have to be in sequential order along a path
# bridges is an array of coordinates of the bridge cells built in order, where bridges[i] is the coordinates of the bridge cell built on the ith day
# Given bridges, return the minimum number of days required to build a complete bridge (made up of bridge cells) across the river, where we can get from the left side to the right side
# if we are unable to build a bridge that connects the left and right sides of the river, return -1

# EXAMPLE:
# bridges = [(4,3), (3,2), (1,0), (1,1), (0,3), (2,1), (3,1), (4,2), (4,0)], m = 5, n = 4
# The bridge cells are marked B in the matrix below
# |   B|
# |BB  |
# | B  |
# | BB |
# |B BB|

# return: 7
# Explanation: A complete bridge can be built from the given bridge cells. We need 7 days to build the complete bridge

###########################################################################################################

# ✅ ALGORITHM: BFS

def minDaysToBuildBridge(bridges, m, n):
    rows, cols = m, n # number of rows and cols
    q = []
    visited = set()
    day_hm = {} # hashmap of each bridge cell coords (key) and the corresponding day i on which it was built (value)
    
    for idx, bridge in enumerate(bridges):
        r,c = bridge
        if c == 0: # if current bridge cell is in the leftmost column
            q.append((r,c,idx)) # add coords of current bridge cell and the day it was built
            visited.add((r,c))
        day_hm[(r,c)] = idx # fill up day_hm hashmap
    
    while q:
        for _ in range(len(q)):
            r, c, days = q.pop(0)
            
            if c == cols-1: # if popped bridge cell is in the rightmost col, we have a valid bridge
                return days + 1 # day_hm values are 0 indexed, so we need to add 1
            
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r+x, c+y # neighbor cell coords
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) in bridges and (nr,nc) not in visited: # if neighbor cell is within bounds and it is a bridge cell and not visited,
                    q.append((nr, nc, max(days, day_hm[(nr, nc)]))) # push the day the bridge at (nr, nc) was constructed
                    visited.add((nr, nc))
    
    return -1