# 323. Number of Connected Components in an Undirected Graph
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
# MEDIUM
# Tags: graphlc, dfslc, #323

# GIVEN:
    # an integer, n
    # an array, edges, where edges[i] = [a_i, b_i] indicates that there is an edge between a_i and b_i in the graph

# TASK:
    # Return the number of connected components in the graph

# EXAMPLES:
    # Input: n = 5, edges = [[0,1],[1,2],[3,4]]
    # Output: 2

    # Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
    # Output: 1

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS

# TIME COMPLEXITY: O(V+E)
    # n and m = length of edges
# SPACE COMPLEXITY: O(n+m)

from collections import defaultdict

def countComponents(n, edges):
    graph = defaultdict(set)
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)

    result = 0 # no. of connected components
    visited = set()

    def dfs(node):
        if node in visited:
            return False
        
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

        return True
    
    for i in range(n):
        if dfs(i): # if dfs(i) returns true, means there is an additional connected component that has been explored
            result += 1

    return result

#==========================================================================================================

# ✅ ALGORITHM 2: BFS

def countComponents(n, edges):
    graph = defaultdict(set)
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    
    result = 0
    visited = set()
    
    def bfs(start):
        q = [start]
        while q:
            node = q.pop(0)
            if node in visited:
                continue
            visited.add(node)
            for neighbor in graph[node]:
                q.append(neighbor)
    
    for i in range(n):
        if i not in visited:
            bfs(i)
            result += 1
    
    return result