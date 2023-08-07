# https://leetcode.com/problems/keys-and-rooms/description
# MEDIUM
# dfslc, #841

# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0
# Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

# EXAMPLES:
    # Input: rooms = [[1],[2],[3],[]]
    # Output: true
    # Explanation: 
    # We visit room 0 and pick up key 1.
    # We then visit room 1 and pick up key 2.
    # We then visit room 2 and pick up key 3.
    # We then visit room 3.
    # Since we were able to visit every room, we return true.

    # Input: rooms = [[1,3],[3,0,1],[2],[0]]
    # Output: false
    # Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS
# Create a visited set to store all rooms that have been visited
# Create a recursive function that takes in current room number and visits each room that can be accessed from current room
# Check if no. of visited rooms = total no. of rooms

# TIME COMPLEXITY: O(N + E) 
    # where N = no. of rooms, E = no. of keys
    # We visit each room once and each key once
# SPACE COMPLEXITY: O(N)
    # where N = no. of rooms
    # We store the visited rooms in a set

def canVisitAllRooms(rooms):
    visited = set()

    def dfs(curr_room):
        if curr_room in visited:
            return
        visited.add(curr_room)

        for next_room in rooms[curr_room]:
            dfs(next_room)
    
    dfs(0) # since we start from room 0
    return len(visited) == len(rooms)

#==========================================================================================================

# ✅ ALGORITHM 2: ITERATIVE DFS
# Create a visited set to store all rooms that have been visited
# Create a stack to store all rooms
# For every neighbor of room popped, if neighbor is not visited, append to stack
# Check if no. of visited rooms = total no. of rooms

# TIME COMPLEXITY: O(N + E)
    # where N = no. of rooms, E = no. of keys
    # We visit each room once and each key once
# SPACE COMPLEXITY: O(N)
    # where N = no. of rooms
    # extra space for stack and set

def canVisitAllRooms(rooms):
    visited = set()
    stack = [0] # since we start from room 0

    while stack:
        curr_room = stack.pop()
        visited.add(curr_room)

        for next_room in rooms[curr_room]:
            if next_room not in visited:
                stack.append(next_room)
    
    return len(visited) == len(rooms)