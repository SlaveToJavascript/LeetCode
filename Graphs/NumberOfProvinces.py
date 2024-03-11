# 547. Number of Provinces
# https://leetcode.com/problems/number-of-provinces/description/
# MEDIUM
# Tags: graphlc, dfslc, #547

# GIVEN:
    # an n x n matrix, isConnected, where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise

# TASK:
    # Return the total number of provinces
        # A province is a group of directly or indirectly connected cities and no other cities outside of the group

# EXAMPLES:
    # Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    # Output: 2

    # Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    # Output: 3

###########################################################################################################

# ✅ ALGORITHM 1A: RECURSIVE DFS (my solution – attempted 10/03/2024)

from collections import defaultdict

def findCircleNum(isConnected):
    # create adjacency list
    graph = defaultdict(set)
    for i in range(len(isConnected)):
        for j in range(len(isConnected[i])):
            if isConnected[i][j] == 1 and i != j:
                graph[i].add(j)
    
    result = 0 # no. of provinces
    visited = set()

    def dfs(city):
        if city in visited:
            return False
        visited.add(city)
        
        for neighbor in graph[city]:
            if neighbor not in visited:
                dfs(neighbor)
        
        return True
    
    for city in range(len(isConnected)):
        if dfs(city): # if True is returned, means this is a new city that is unvisited, hence it's a new province
            result += 1
    
    return result

#==========================================================================================================

# ✅ ALGORITHM 1B: RECURSIVE DFS

def findCircleNum(isConnected):
    n = len(isConnected) # n = no. of cities
    visited = set()

    def dfs(city):
        for neighbor, is_connected in enumerate(isConnected[city]): # index = neighbor city, is_connected = 1 if city and neighbor city are connected, 0 if not connected
            if is_connected and neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)
    
    provinces = 0
    
    for city in range(n):
        if city not in visited:
            dfs(city) # this line's purpose is to populate the "visited" set
            provinces += 1 # since current city is not visited, this is a new province -> result +1
    
    return provinces