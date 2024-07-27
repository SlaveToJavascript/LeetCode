# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/description/
# MEDIUM
# Tags: graphlc, heaplc, minheaplc, dijkstralc, bfslc, #743

# GIVEN:
    # a network of n nodes, labeled from 1 to n
    # array, times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target

# TASK:
    # We will send a signal from a given node k
    # Return the minimum time it takes for all the n nodes to receive the signal
    # If it is impossible for all the n nodes to receive the signal, return -1

# EXAMPLES:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1

# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1

###########################################################################################################

# ✅ ALGORITHM: DIJKSTRA'S ALGORITHM
    # https://youtu.be/EaphyqKU4PQ?si=fabMEdIgHrYav5AH&t=279
# ! MAIN IDEA: we are looking for the SHORTEST PATH that takes the most amount of time to reach
    # e.g. find the shortest amount of time to reach A -> C, where A -> C takes the longest time to reach within the graph
# Create a min heap that pops out the node in the path with the min total time
# Once we have visited all n nodes, we can return this min total time

# TIME COMPLEXITY: O(E log V)
    # each push/pop operation is O(log V)
    # in the worst case, we can push to heap E times (1 for each edge)
    # -> overall TC = O(E log V)
# SPACE COMPLEXITY: O(E+V)
    # adjacency list takes O(E+V) space

from collections import defaultdict
from heapq import heappop, heappush

def networkDelayTime(times, n, k):
    # build adjacency list of destination nodes and times
    graph = defaultdict(set)
    for src, dest, time in times:
        graph[src].add((dest, time))
    
    # graph[i] = { source_node: (
    #                             (destination_node1, time1), 
    #                             (destination_node2, time2),
    #                             ...
    #                            )
    #             }
    
    heap = [ (0, k) ] # add source node to heap
    visited = set()

    while heap:
        total_time, node = heappop(heap) # pop the node in the path with minimum total time
        visited.add(node)

        if len(visited) == n: # if we visited all nodes, i.e. all nodes have received signal
            return total_time # this total_time is the min. time needed visit all nodes

        for neighbor, time in graph[node]: # for each neighbor of current node,
            if neighbor not in visited:
                heappush(heap, (total_time + time, neighbor)) # visit neighbor by adding to heap
        
    return -1 # if no min. total time has been returned, it means we can't visit all nodes -> return -1