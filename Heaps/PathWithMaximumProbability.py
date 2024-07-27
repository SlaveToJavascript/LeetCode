# 1514. Path with Maximum Probability
# https://leetcode.com/problems/path-with-maximum-probability/description/
# MEDIUM
# Tags: graphlc, heaplc, maxheaplc, dijkstralc, bfslc, #1514

# GIVEN:
    # an undirected weighted graph of n nodes represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i]
    # 2 nodes, start and end

# TASK:
    # find the path with the maximum probability of success to go from start to end and return its success probability
    # If there is no path from start to end, return 0

# EXAMPLES:
    # Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
    # Output: 0.25000
    # Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

    # Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
    # Output: 0.30000

    # Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
    # Output: 0.00000
    # Explanation: There is no path between 0 and 2.

###########################################################################################################

# ✅ ALGORITHM: DIJKSTRA'S ALGORITHM
# Dijkstra is used when we are dealing with non-negative weighted edges and trying to find a min/max of those weights
# Create a max heap that pops out the node in the path with the max probability every time
# Once we reached the end node, we can return this max probability

# TIME COMPLEXITY: O(E log V)
    # each push/pop operation is O(log V)
    # in the worst case, we can push to heap E times (1 for each edge)
    # -> Overall TC = O(E log V)
# SPACE COMPLEXITY: O(V^2)
    # worst case: every node is connected to every other node -> SC = O(V^2)

from collections import defaultdict
from heapq import heappop, heappush

def maxProbability(n, edges, succProb, start_node, end_node):
    # create adjacency list of destination nodes and probabilities
    graph = defaultdict(set)
    for i in range(len(edges)):
        a, b = edges[i]
        graph[a].add((b, succProb[i]))
        graph[b].add((a, succProb[i]))
    
    # graph[i] = { source_node: (
    #                             (destination_node1, prob1), 
    #                             (destination_node2, prob2),
    #                             ...
    #                            )
    #             }
    
    max_heap = [ (-1, start_node) ] # initialize probability of start_node to -1 since any x*1 = x; -ve is because max_heap
    visited = set()

    while max_heap:
        prob, node = heappop(max_heap) # max probability will be popped out every time
        visited.add(node)
        
        if node == end_node: # if we reached destination,
            return -prob

        for neighbor, edge_prob in graph[node]:
            if neighbor not in visited:
                heappush(max_heap, (edge_prob * prob, neighbor)) # total probability of current path = prob of current edge * existing probability
    
    return 0