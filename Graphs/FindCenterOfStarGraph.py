# 1791. Find Center of Star Graph
# https://leetcode.com/problems/find-center-of-star-graph/
# EASY
# Tags: graphlc, #1791

# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

# EXAMPLES:
    # Input: edges = [[1,2],[2,3],[4,2]]
    # Output: 2
    # Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

    # Input: edges = [[1,2],[5,1],[1,3],[1,4]]
    # Output: 1

###########################################################################################################

# ✅ ALGORITHM: GREEDY
# in a star graph, the center node is connected to all other nodes, which means the center node has an edge with every other node
# hence, in edges array, the center node can be found in EVERY array in edge
    # this means we only need to check the 1st array in edges array, and see which 1 of the 2 nodes is also in the 2nd array (the center is guaranteed to be in every array in edges)
    # if nodes A and B are in the 1st array in edges, and node A is not in the 2nd array in edges, that means the center node must be node B

# TIME COMPLEXITY: O(1)
# SPACE COMPLEXITY: O(1)

def findCenter(edges):
    return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]