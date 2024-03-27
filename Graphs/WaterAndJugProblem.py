# 365. Water and Jug Problem
# https://leetcode.com/problems/water-and-jug-problem/description/
# MEDIUM
# Tags: dfslc, graphlc, #365

# GIVEN:
    # 2 jugs with capacities x liters and y liters
    # an infinite water supply

# TASK:
    # Return whether the total amount of water in both jugs may reach target using the following operations:
        # Fill either jug completely with water.
        # Completely empty either jug.
        # Pour water from one jug into another until the receiving jug is full, or the transferring jug is empty.

# EXAMPLES:
    # Input: x = 3, y = 5, target = 4
    # Output: true
    # Explanation:
    # Follow these steps to reach a total of 4 liters:

    # Fill the 5-liter jug (0, 5).
    # Pour from the 5-liter jug into the 3-liter jug, leaving 2 liters (3, 2).
    # Empty the 3-liter jug (0, 2).
    # Transfer the 2 liters from the 5-liter jug to the 3-liter jug (2, 0).
    # Fill the 5-liter jug again (2, 5).
    # Pour from the 5-liter jug into the 3-liter jug until the 3-liter jug is full. This leaves 4 liters in the 5-liter jug (3, 4).
    # Empty the 3-liter jug. Now, you have exactly 4 liters in the 5-liter jug (0, 4).

    # Input: x = 2, y = 6, target = 5
    # Output: false

    # Input: x = 1, y = 2, target = 3
    # Output: true
    # Explanation: Fill both jugs. The total amount of water in both jugs is equal to 3 now.

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS
# MAIN IDEA:
    # each node in the graph is the total amount of water in both jugs
    # each edge is the operation to get to the next node, and we have 4 options for an operation:
        # fill jug 1: +x to total amount of water
        # fill jug 2: +y to total amount of water
        # empty jug 1: -x to total amount of water
        # empty jug 2: -y to total amount of water
        # NOTE: for pouring water from 1 jug to another, there is no change to total amount of water since it's just a transfer from 1 jug to another -> no need to consider it an operation

# TIME COMPLEXITY: O(x+y)
    # no. of unique nodes (i.e. amts of water) is in the range [0, x+y], therefore there are x+y+1 unique nodes
    # for each node, DFS explores 4 different operations, but since we keep track of visited nodes, each node is visited once -> O(x+y)
# SPACE COMPLEXITY: O(x+y)
    # recursive call stack takes O(x+y) space in the worst case
    # visited set takes O(x+y) space in the worst case

def canMeasureWater(x, y, target):
    visited = set() # if we have encountered a certain node (i.e. total amount of water) before, no need to revisit it again, otherwise we would keep going in circles back to the same node

    def dfs(total): # total = total amount of water in both jugs
        if total == target:
            return True
        if total in visited:
            return False
        if total < 0 or total > x + y: # it's impossible for there to be -ve amount of water or have more water than the total capacity of both jugs
            return False
        
        visited.add(total)
        operations = [x, y, -x, -y]
        for op in operations:
            if dfs(total + op): # if True, means we've found the target -> return True and end recursion
                return True
        
        return False # if we've tried all operations and none of them led to the target, return False
    
    return dfs(0)

#==========================================================================================================

# ✅ ALGORITHM 2: ITERATIVE BFS (with queue)
# (refer to the notes in ALGORITHM 1)

# TIME COMPLEXITY: O(x+y)
# SPACE COMPLEXITY: O(x+y)

def canMeasureWater(x, y, target):
    visited = set()
    q = [0]

    while q:
        total = q.pop(0)
        if total == target:
            return True
        
        if total not in visited and 0 <= total <= x+y: # if total is unique and within the range of possible total amounts of water
            visited.add(total)
            operations = [x, y, -x, -y]
            for op in operations:
                q.append(total + op)
    
    return False