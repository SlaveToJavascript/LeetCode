# 1059. All Paths from Source Lead to Destination
# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/
# MEDIUM
# Tags: graphlc, dfslc, backtracklc, premiumlc, #1059

# GIVEN:
    # edges, the edges of a directed graph
        # edges[i] = [a_i, b_i] indicates there is an edge between nodes a_i and b_i
    # 2 nodes, source and destination, of this graph

# TASK:
    # determine whether or not all paths starting from source eventually, end at destination, that is:
        # 1. At least one path exists from the source node to the destination node
        # 2. If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
        # 3. The number of possible paths from source to destination is a finite number.
    # Return true if and only if all roads from source lead to destination.

# EXAMPLES:
    # Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
    # Output: false
    # Explanation: It is possible to reach and get stuck on both node 1 and node 2.

    # Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
    # Output: false
    # Explanation: We have two possibilities: to end at node 3, or to loop over node 1 and node 2 indefinitely.

    # Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
    # Output: true

###########################################################################################################

# ✅ ALGORITHM 1A: DFS + BACKTRACKING (+ MEMOIZATION)
# construct adjacency list graph from edges
# create a visited set to keep track of visited nodes
# DFS: base cases is when we detect a cycle or when we reach a node with no outgoing edges (in this case, we check if the node is the destination -> if yes, return True, else False)
# for each neighbor of the current node, if dfs(neighbor) is False, it means the path doesn't lead to the destination, so return False
# ! backtrack by removing the current node from visited set so that we can correctly explore other paths that may involve nodes that we have already visited
    # usually for DFS, we are only exploring one path -> don't need to remove the node from visited set since we are not going to visit it again
    # but for this problem, we need to explore all paths from a node, so we need to remove the node from visited set after we finish exploring all paths from that node so that other paths that involve that node can be correctly explored
# NOTE: can use memoization to reduce the time complexity from O(2^n) to O(n)

# TIME COMPLEXITY: O(V+E) with memoization, O(2^V) without memoization
    # WITH memoization: O(E) for constructing adjacency list + O(V) for DFS (we visit each node at most once since we cache a node whenever we visit it during dfs(node) -> if the same node is encountered again during a different DFS path, the cached result is used instead of recomputing the entire DFS from that node)
    # WITHOUT memoization: in the worst case, DFS explores every node and every edge for graphs with many cycles/overlapping paths -> every node could potentially be revisited along different paths, leading to an exponential number of recursive calls)
# SPACE COMPLEXITY: O(V+E)
    # O(V) for @cache
    # O(V) for visited set
    # O(V+E) for adjacency list

from collections import defaultdict
from functools import cache

def leadsToDestination(n, edges, source, destination):
    graph = defaultdict(set)
    for a, b in edges:
        graph[a].add(b)

    visited = set()

    @cache # MEMOIZATION -> reduces TC from O(2^n) to O(n)
        # NOTE: during interviews, skip this line in the 1st solution and if asked for optimization, then add this line
    def dfs(node):
        if node in visited: # if we detect a cycle, return False
            return False
        if not graph[node]: # if node has no outgoing edges,
            return node == destination # return true if node is destination, else False (violates Rule #2 of the 3 requirements)
        
        visited.add(node)
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False # check for the result of dfs(neighbor) immediately to stop the search as soon as you find that one of the paths does not lead to the destination (see ***** NOTE *****)
        
        # backtrack:
        visited.remove(node) # once we finish exploring all paths from current node, we remove the node from visited set

        return True
    
    return dfs(source)

# ***** NOTE *****
    # If you don't check immediately for dfs(neighbor), you might continue exploring other paths even though you already know that one path doesn't lead to the destination. This is inefficient and incorrect for the problem at hand because the requirement is that all paths must lead to the destination. Continuing after detecting a failure would lead to incorrect results
    # In the loop "for neighbor in graph[node]: dfs(neighbor)"", since the result of dfs(neighbor) is not captured or checked, the function doesn’t immediately know that it should stop and return False. It continues iterating over other neighbors even though it has already found a failure.

#==========================================================================================================

# ✅ ALGORITHM 1B: DFS + BACKTRACKING + EXPLICIT MEMOIZATION (i.e. no using @cache)
# same as above, except instead of simply using @cache, we explicitly memoize using an array
# instead of using a visited set, we use a visited array where visited[0] = state of the node (0: not visited, 1: being visited, 2: fully processed, i.e. all paths from this node lead to destination)

# TIME COMPLEXITY: O(V+E)
    # worst case: DFS explores every node and every edge for graphs with many cycles/overlapping paths -> every node could potentially be revisited along different paths, leading to an exponential number of recursive calls)
# SPACE COMPLEXITY: O(V+E)
    # O(V) for visited set
    # O(V+E) for adjacency list

from collections import defaultdict

def leadsToDestination(n, edges, source, destination):
    graph = defaultdict(set)
    for a, b in edges:
        graph[a].add(b)

    # States:
        # visited[node] = 0: node has not been visited
        # visited[node] = 1: node is being visited (part of the current path)
        # visited[node] = 2: node has been fully processed (all paths from this node lead to destination)
    visited = [0] * n

    def dfs(node):
        if visited[node] == 1:  # Found a cycle
            return False
        if visited[node] == 2:  # Already processed node
            return True
        if not graph[node]:  # If the node has no outgoing edges
            return node == destination  # Should be true only if it's the destination

        visited[node] = 1  # Mark node as being visited
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        visited[node] = 2  # Mark node as fully processed
        return True

    return dfs(source)
