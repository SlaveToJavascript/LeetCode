# 797. All Paths From Source to Target
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
# MEDIUM
# Tags: graphlc, dfslc, #797

# GIVEN:
    # a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1
        # graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j])

# TASK:
    # find all possible paths from node 0 to node n - 1 and return them in any order

# EXAMPLES:
    # Input: graph = [[1,2],[3],[3],[]]
    # Output: [[0,1,3],[0,2,3]]
    # Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

    # Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
    # Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

###########################################################################################################

# ✅ ALGORITHM: RECUSRIVE DFS
# Create adjList (hashmap) of nodes and an array of nodes that can be reached
# in dfs() function, when destination is reached, add the path to result (array of paths)
# else, if destination is not reached, add current node to path and keep exploring current node's neighbors
    # NOTE: we cannot do "paths += [src]" as arrays are mutable, and this line modifies the path array in-place -> i.e. you're modifying the same list across all recursive calls

# TIME COMPLEXITY: O(2^n * n)
    # 2^n:
        # no. of possible paths from src to dest can grow exponentially w/ the no. of nodes
            # e.g. in binary tree, each node connects to 2 other nodes -> there are up to 2^d possible paths at depth = d
        # in a densely-connected graph, the branching factor results in no. of paths being exponential to the no. of nodes
    # n:
        # for each recursive call, a new path array is created (path + [src]), which takes O(n) time, where n = length of array
# SPACE COMPLEXITY: O(2^n * n)
    # as explained under time complexity, there are up to ~ 2^n paths, and each path is up to length n -> space needed to store these paths is ~ 2^n * n

from collections import defaultdict

def allPathsSourceTarget(graph):
    adjList = defaultdict(list)
    for idx, arr in enumerate(graph):
        adjList[idx] += arr
    
    paths = [] # result to be returned
    dest = len(graph)-1 # destination: n-1, source: 0

    def dfs(src, path): # path = current path
        if src == dest:
            paths.append(path + [src])
            return
        
        for neighbor in adjList[src]:
            dfs(neighbor, path + [src])
        
    dfs(0, [])
    return paths