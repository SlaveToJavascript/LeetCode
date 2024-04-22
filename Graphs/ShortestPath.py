# https://www.structy.net/problems/shortest-path

# GIVEN:
    # list of edges for an undirected graph
    # source node
    # destination node

# TASK:
    # find and return the length of the shortest path between source and destination nodes
    # each edge has a length of 1
    # if there is no path is found between source and destination, return -1

###########################################################################################################

# ✅ ALGORITHM: ITERATIVE BFS
# NOTE: BFS is typically used for questions looking for "shortest path"
    # because BFS traverses the graph level-by-level outwards from the start -> the first time we encounter the destination, that must be 
# Create a 2D array queue which is used to store each node + its distance from source
    # i.e. [node, distance]
# Create a set visited which is used to store visited nodes (since it's an undirected graph)

# TIME COMPLEXITY: O(e), e = no. of edges
# SPACE COMPLEXITY: O(n), n = no. of nodes

def shortest_path(edges, source, destination):
    # build the graph's adjacency list
    graph = {}
    for a, b in edges:
        if a not in graph: 
            graph[a] = []
        if b not in graph: 
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    q = [ (source, 0) ] # format: (node, distance_from_source)
    # here, distance from source to source is 0
    visited = set()
    
    while q:
        curr, dist = q.pop(0)
        if curr == destination: 
            return dist
        visited.add(curr)

        for neighbor in graph[curr]:
            if neighbor not in visited:
                q.append((neighbor, dist+1))
