# https://www.structy.net/problems/largest-component

# GIVEN:
    # graph, the adjacency list of an undirected graph

# TASK:
    # return the size (i.e. no. of nodes) of the largest connected component (graph)

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
# define a recursive dfs function that returns the size (i.e. no. of nodes) of a connected graph component
# call the recursive dfs function on every node in graph to get the maximum size

# TIME COMPLEXITY: O(e), e = no. of edges
# SPACE COMPLEXITY: O(n), n = no. of nodes

def largest_component(graph):

    def dfs(graph, current, visited):
        if current in visited: return 0
        visited.add(current)
        size = 1 # for current node that is being visited
        for neighbor in graph[current]:
            size += dfs(graph, neighbor, visited)
        return size
    
    visited = set()
    max_size = 0
    for node in graph:
        max_size = max(max_size, dfs(graph, node, visited))
    
    return max_size