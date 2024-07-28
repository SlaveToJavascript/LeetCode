# 2093. Minimum Cost to Reach City With Discounts
# https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts
# MEDIUM
# Tags: graphlc, heaplc, minheaplc, dijkstralc, premiumlc, #2093

# A series of highways connect n cities numbered from 0 to n - 1. You are given a 2D integer array highways where highways[i] = [city1i, city2i, tolli] indicates that there is a highway that connects city1i and city2i, allowing a car to go from city1i to city2i and vice versa for a cost of tolli.
# You are also given an integer discounts which represents the number of discounts you have. You can use a discount to travel across the ith highway for a cost of tolli / 2 (integer division). Each discount may only be used once, and you can only use at most one discount per highway.
# Return the minimum total cost to go from city 0 to city n - 1, or -1 if it is not possible to go from city 0 to city n - 1.

# EXAMPLES:
    # Input: n = 5, highways = [[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]], discounts = 1
    # Output: 9
    # Explanation:
    # Go from 0 to 1 for a cost of 4.
    # Go from 1 to 4 and use a discount for a cost of 11 / 2 = 5.
    # The minimum cost to go from 0 to 4 is 4 + 5 = 9.

    # Input: n = 4, highways = [[1,3,17],[1,2,7],[3,2,5],[0,1,6],[3,0,20]], discounts = 20
    # Output: 8
    # Explanation:
    # Go from 0 to 1 and use a discount for a cost of 6 / 2 = 3.
    # Go from 1 to 2 and use a discount for a cost of 7 / 2 = 3.
    # Go from 2 to 3 and use a discount for a cost of 5 / 2 = 2.
    # The minimum cost to go from 0 to 3 is 3 + 3 + 2 = 8.

    # Input: n = 4, highways = [[0,1,3],[2,3,2]], discounts = 0
    # Output: -1
    # Explanation:
    # It is impossible to go from 0 to 3 so return -1.

###########################################################################################################

# ✅ ALGORITHM: DIJKSTRA'S ALGORITHM WITH MIN HEAP
# use min-heap to store (current_cost, current_city, number_of_discounts_used)
# ! MAIN IDEA: use a 2D array, disc, which is used to update the min cost to reach each node with 0 to all discounts used (disc[i][j] = min cost to reach node i with j discounts used)
    # CASE 1: WITHOUT DISCOUNT
        # For each neighbor node of the current node, calculate the total cost to reach that node without using a discount
        # If this cost is less than the previously recorded cost for that neighbor, update disc and push the new  (current_cost, current_city, number_of_discounts_used) tuple into the min-heap
    # CASE 2: WITH DISCOUNT (if available)
        # calculate the total cost + discounted current toll cost
        # if this total cost is less than the previously recorded cost for that neighbor, update disc and push the new  (current_cost, current_city, number_of_discounts_used) tuple into the min-heap
# NOTE: visited set is not needed as we can leverage the fact that any node expansion can be pruned if the current accumulated cost to reach a node is already higher than the recorded minimum cost for that node and discount state
    # Recall that in Dijkstra's algorithm, we choose the nodes with the lowest accumulated cost to expand at each iteration
    # For example, consider a graph with nodes A, B, and C, where the edges are as follows: highways[0] = [A, B, 5], highways[1] = [B, C, 10], and highways[2] = [A, C, 12]. Suppose we have one discount available
        # If we find a path from A to B to C with a total cost of 15 (5 from A to B and 10 from B to C), and record this in disc[C][0], we can later skip expanding any path to C with a higher accumulated cost, such as 20, since it exceeds the recorded minimum cost of 15

# TIME COMPLEXITY: O(ED log(ED))
    # constructing graph: O(E) where E is the number of edges (highways)
    # each push/pop takes O(log n) time, where n = no. of elements in heap, which is O(log(E * (D+1))), where D = no. of discounts
        # This is because the heap can grow to include multiple states for each edge and each discount level
    # updating disc: Since each city can be visited multiple times with different discount levels, the updates to disc and the pushes to the heap are bounded by O(E * (D+1))
    # Combining these observations, overall TC = no. of times the min-heap operations are performed and the no. of updates to the disc array
        # the no. of heap operations = O(E * (D+1) log(E * (D+1)) ≈ O(ED log(ED))
# SPACE COMPLEXITY: O((E+V)D)
    # graph adjacency list takes O(E+V) space
    # disc 2D array takes O(V * (D+1)) space in the worst case (since each node/vertice can be added with 0 to D discounts)
    # min-heap can grow up to O(E * (D+1)) elements
    # -> overall SC = O(E+V + V * (D+1) + E * (D+1)) ≈ O((E+V)D)

from collections import defaultdict
from heapq import heappop, heappush

def minimumCost(n, highways, discounts):
    graph = defaultdict(set) # adjacency list
    for a, b, toll in highways:
        graph[a].add((b, toll))
        graph[b].add((a, toll))
    
    min_heap = [(0, 0, 0)] # (current_cost, current_city, number_of_discounts_used)
    disc = [[float('inf')] * (discounts+1) for _ in range(n)] # disc[i][j] = min cost of traveling to city i with j discounts used
    disc[0][0] = 0 # cost to reach city 0 with 0 discounts used is 0

    while min_heap:
        curr_cost, city, discounts_used = heappop(min_heap)
        if city == n-1: # reached destination
            return curr_cost
        
        for neighbor, toll in graph[city]:
            # 1) Go to neighbor city WITHOUT DISCOUNT
            if curr_cost + toll < disc[neighbor][discounts_used]: # if traveling to neighbor without using a discount results in lower cost than previously recorded,
                disc[neighbor][discounts_used] = curr_cost + toll # update disc array with the min cost to go from current node to neighbor without using a discount
                heappush(min_heap, (curr_cost+toll, neighbor, discounts_used))
            
            # 2) Go to neighbor city WITH DISCOUNT (if available)
            if discounts_used < discounts: # if there are discounts available
                new_cost_with_discount = curr_cost + toll//2 # total cost to reach neighbor with discount
                if new_cost_with_discount < disc[neighbor][discounts_used+1]: # if traveling to neighbor with a discount results in lower cost than previously recorded,
                    disc[neighbor][discounts_used+1] = new_cost_with_discount # update disc array with the min cost to go from current node to neighbor with a discount
                    heappush(min_heap, (new_cost_with_discount, neighbor, discounts_used+1))

    return -1 # destination not reachable