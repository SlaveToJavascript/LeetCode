# 2316. Count Unreachable Pairs of Nodes in an Undirected Graph
# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/
# MEDIUM
# Tags: graphlc, dfslc, #2316

# GIVEN:
    # an integer, n
        # There is an undirected graph with n nodes, numbered from 0 to n - 1
    # a 2D integer array, edges, where edges[i] = [a,b] denotes that there exists an undirected edge connecting nodes a and b

# TASK:
    # Return the number of pairs of different nodes that are unreachable from each other

# EXAMPLES:
    # Input: n = 3, edges = [[0,1],[0,2],[1,2]]
    # Output: 0
    # Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.

    # Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
    # Output: 14
    # Explanation: There are 14 pairs of nodes that are unreachable from each other:
    # [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
    # Therefore, we return 14.

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
# create an adjacency list (hashmap) of each node : [list of nodes that are connected to that node]
# perform dfs to get the size (i.e. no. of nodes) in each connected component
    # add the size of each connected component to an array
# get the no. of unreachable pairs by multiplying each pair of sizes of connected components with each other and summing up the products of each pair

# TIME COMPLEXITY: O(n+e)
    # n = no. of nodes
    # e = no. of edges
# SPACE COMPLEXITY: O(n+e)
    # for the adjacency list

from collections import defaultdict

def countPairs(n, edges):
    adjList = defaultdict(set)
    for a, b in edges:
        adjList[a].add(b)
        adjList[b].add(a)

    visited = set()

    # dfs() returns size of a particular connected component
    def dfs(node):
        if node in visited:
            return 0 # since this node has been visited, we can't visit any more nodes in this connected component
        
        visited.add(node)
        size = 1 # count the current node

        for neighbor in adjList[node]:
            size += dfs(neighbor) # accumulate sizes of all nodes in this connected component
                # NOTE: see **********

        return size
    
    graph_sizes = [] # an array of the graph size of each respective connected component
    for i in range(n):
        if i not in visited:
            graph_sizes.append(dfs(i))
    
    # ***** inefficient way to find no. of unreachable pairs using double for-loop:
        # TIME COMPLEXITY of the following block of code = O(n^2) in the worst case
    result = 0
    for i in range(len(graph_sizes)):
        for j in range(i+1, len(graph_sizes)):
            result += graph_sizes[i] * graph_sizes[j]

    # ***** OR, A BETTER (MORE EFFICIENT WAY TO SOLVE THIS: CALCULATE TOTAL NO. OF PAIRS, THEN CALCULATE NO. OF REACHABLE PAIRS IN THE CONNECTED COMPONENTS, THE RETURN THE DIFFERENCE)
        # formula: no. of unreachable pairs = total no. of pairs - no. of reachable pairs
    total_pairs = n * (n-1) // 2
    reachable_pairs = len(graph_sizes) * (len(graph_sizes)-1) // 2 # len(graph_sizes) = no. of connected components
    result = total_pairs - reachable_pairs # this is the no. of unreachable pairs

    return result


# NOTE: ********** WHY DOES THIS ACCUMULATE THE SIZE OF THE CONNECTED COMPONENT?
    # For each neighbor of the current node, dfs(neighbor) explores that neighbor's part of the connected component, marking nodes as visited and accumulating their count
    # It then returns the size of the connected component accessible from that neighbor
    # Adding this returned size to the "size" variable for the current node ("size += dfs(neighbor)") effectively aggregates the total size of the connected component piece by piece as the recursion unfolds
        # This is because each call to dfs contributes the size of the portion of the component it explored to the cumulative size being calculated by its caller
    
    # EXAMPLE:
        # 1 --- 2
        #  \   /
        #    3
        
        # Starting DFS at node 1, we have size = 1.
        # dfs explores neighbors 2 and 3. Let's say it goes to 2 first.
        # In dfs(2), it finds neighbor 3 (besides 1, which is already visited) and calls dfs on 3, adding 1 to its size.
        # dfs(3) finds both 1 and 2 are visited, so it only contributes its own size, 1, making the size seen by dfs(2) now 2.
        # Returning to dfs(1), the size is updated to 3, reflecting the entire component's size.