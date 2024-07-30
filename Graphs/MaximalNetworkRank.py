# 1615. Maximal Network Rank
# https://leetcode.com/problems/maximal-network-rank/description/
# MEDIUM
# Tags: graphlc, #1615

# There is an infrastructure of n cities with some number of roads connecting these cities
    # Each roads[i] = [a_i, b_i] indicates that there is a bidirectional road between cities a_i and b_i
# The network rank of two different cities is defined as the total number of directly connected roads to either city
    # If a road is directly connected to both cities, it is only counted once
# The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities
# TODO: Given the integer n and the array roads, return the maximal network rank of the entire infrastructure

# EXAMPLES:
    # Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
    # Output: 4
    # Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.

    # Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
    # Output: 5
    # Explanation: There are 5 roads that are connected to cities 1 or 2.

    # Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
    # Output: 5
    # Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.

###########################################################################################################

# ✅ ALGORITHM: FIND IN-DEGREES
# In-degree of a node = no. of incoming or outgoing paths from the node
    # since the graph is non-directional, in-degree = out-degree
# To calculate in-degree, create an adjacency list
# To get the network rank between 2 nodes, add their in-degrees and -1 if these 2 nodes have a path connecting each other
# NOTE: simply picking the top two nodes with the highest degrees does not always give the correct maximal network rank because there may be more than two nodes with the highest degrees, and we need to check all pairs of these nodes

# TIME COMPLEXITY: O(E+V^2)
    # O(E) to construct the adjacency list
    # O(V^2) to iterate over all pairs of nodes
    # -> overall TC = O(E + V^2)
# SPACE COMPLEXITY: O(E+V)
    # adjacency list takes O(E+V) space

from collections import defaultdict

def maximalNetworkRank(n, roads):
    # create adjList of each city -> {set of cities it's connected to}
    adjList = defaultdict(set)
    for road in roads:
        a, b = road
        adjList[a].add(b)
        adjList[b].add(a)

    max_rank = 0 # return value

    for i in range(n):
        for j in range(i+1, n): # for each pair (i,j) in range(n),
            rank = len(adjList[i]) + len(adjList[j])
            if i in adjList[j]: # or vice versa
                rank -= 1 # there is a road between cities i and j -> rank-1
            max_rank = max(max_rank, rank)
    
    return max_rank