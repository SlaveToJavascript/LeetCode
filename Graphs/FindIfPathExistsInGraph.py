# 1971. Find if Path Exists in Graph
# https://leetcode.com/problems/find-if-path-exists-in-graph/description/
# EASY
# Tags: graphlc, dfslc, #1971

# GIVEN:
    # undirected graph with n vertices, where each vertex is labeled from 0 to n-1 (inclusive)
    # edges in the graph are represented as 2D integer array, edges

# TASK:
    # determine if there is a valid path that exists from source to destination nodes
    # return true if exists, false otherwise

# EXAMPLES:
    # Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
    # Output: true
    # Explanation: There are two paths from vertex 0 to vertex 2:
    # - 0 → 1 → 2
    # - 0 → 2

    # Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
    # Output: false
    # Explanation: There is no path from vertex 0 to vertex 5.

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
# Convert edges into graph adjacency list
# Use recursive DFS to traverse graph and check if destination node is found

# TIME COMPLEXITY: O(E), where E = no. of edges
# SPACE COMPLEXITY: O(V), where V = no. of vertices

def validPath(n, edges, source, destination):
    # Convert edges into graph adjacency list
    graph = {k:[] for k in range(n)}
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    # Use recursive DFS to traverse graph and check if destination node is found
    def dfs(graph, src, dest, visited):
        if src == dest: return True
        if src in visited: return False
        # since graph is undirected, a set, visited, is needed to track visited nodes to ensure the traversal doesn't go in cycles

        visited.add(src)

        for neighbor in graph[src]:
            if dfs(graph, neighbor, dest, visited):
                return True
        
        return False
    
    return dfs(graph, source, destination, set())