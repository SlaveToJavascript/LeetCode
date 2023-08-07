# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description
# MEDIUM
# Tags: binarytreelc, dfslc, #1466

# GIVEN:
    # There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one direction to travel between two different cities
    # Roads are represented by an array, connections, where connections[i] = [a, b] represents a road from city a to city b (1 direction only)

# TASK:
    # Change the direction of some roads such that each city can visit the city 0
    # Return the minimum number of edges changed
    # NOTE: It's guaranteed that each city can reach city 0 after reorder

# EXAMPLES:
    # Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    # Output: 3
    # Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

    # Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
    # Output: 2
    # Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

    # Input: n = 3, connections = [[1,0],[2,0]]
    # Output: 0

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
# Convert connections array into a set of tuples for more efficient read operations
# Create neighbors hashmap where, if there is a road between cities a and b, then a is b's neighbor and b is a's neighbor (undirectional)
# Create visited set to keep track of visited cities
# Create a counter to keep track of number of edges changed (this is the return value)
# dfs(city) takes in a city and updates the no. of direction changes needed for all of city's neighbors to be able to reach city; then it recursively takes in each of city's neighbors and repeats the same for each
# return the final counter value (i.e. no. of direction changes)

# TIME COMPLEXITY: O(n)
    # n = no. of cities
    # dfs() function visits each node once, which takes O(n) time in total
    # Because we have undirected edges, each edge can only be iterated twice, resulting in O(e) operations in total (e = no. of edges = n-1) while visiting all nodes
    # Overall TC = O(n) + O(n-1) = O(n)
# SPACE COMPLEXITY: O(n)
    # edges set and neighbors hashmap have a maximum possible length of n each

def minReorder(n, connections):
    # convert connections 2D array into set of tuples for more efficient read operations
    edges = { (a, b) for a, b in connections }

    # create neighbors hashmap to track the neighbors of each city
    # 2 cities a and b are neighbors if there is an edge between them (undirectional)
        # i.e. a is b's neighbor and b is a's neighbor
    neighbors = { i: [] for i in range(n) }
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)

    visited = set()
    counter = 0 # return value; no. of direction changes needed

    def dfs(city):
        nonlocal counter # this line allows us to modify counter from inside dfs() function

        visited.add(city) # since we visited current city, add it to visited set

        for neighbor in neighbors[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                if (neighbor, city) not in edges: # if we cannot get from current neighbor to city
                    counter += 1 # then we need to change the direction
                dfs(neighbor) # recursively call dfs() on each neighbor of city
    
    dfs(0) # we want to get to the 0th city
    return counter

#==========================================================================================================

# ✅ ALGORITHM: ITERATIVE BFS
# Create an integer variable, count, to count the number of edges that are to be flipped
# Create an adjacency list adj that contains a list of pairs of integers such that adj[node] contains all the neighbors of node in the form of (neighbor, sign) where neighbor is the neighboring node of node and sign denotes the direction of the edge, i.e. if the direction is a -> b then adj[a] = [(b, 1), ...] while adj[b] = [(a, 0), ...]
# Start a BFS traversal:
    # Create a visited array of length n to keep track of nodes that have been visited.
    # We initialize a queue q of integers and push 0 into it. We also mark 0 as visited.
    # While the queue is not empty, we dequeue the first element node from the queue and iterate over all its neighbors using adj[node]
        # For each neighbor, sign in adj[node], we check if neighbor has been visited already
        # If neighbor has not yet been visited, we mark it visited, perform count += sign, and push neighbor into the queue.
# Return count.

def minReorder(n, connections):
    graph = [ [] for _ in range(n) ]
    for a, b in connections:
        graph[a].append((b, 1))
        graph[b].append((a, 0))
    
    q = [0]
    visited = set()
    visited.add(0)
    counter = 0

    while q:
        city = q.pop(0)
        for neighbor, direction in graph[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                counter += direction
                q.append(neighbor)
    return counter