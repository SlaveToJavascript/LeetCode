# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
# MEDIUM
# Tags: graphlc, dijkstralc, bfslc, heaplc, minheaplc, #1334

# There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
# Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

# EXAMPLES:
    # Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
    # Output: 3
    # Explanation: The figure above describes the graph. 
    # The neighboring cities at a distanceThreshold = 4 for each city are:
    # City 0 -> [City 1, City 2] 
    # City 1 -> [City 0, City 2, City 3] 
    # City 2 -> [City 0, City 1, City 3] 
    # City 3 -> [City 1, City 2] 
    # Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

    # Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
    # Output: 0
    # Explanation: The figure above describes the graph. 
    # The neighboring cities at a distanceThreshold = 2 for each city are:
    # City 0 -> [City 1] 
    # City 1 -> [City 0, City 4] 
    # City 2 -> [City 3, City 4] 
    # City 3 -> [City 2, City 4]
    # City 4 -> [City 1, City 2, City 3] 
    # The city 0 has 1 neighboring city at a distanceThreshold = 2.

###########################################################################################################

# ✅ ALGORITHM: DIJKSTRA'S ALGORITHM (SHORTEST PATH)
    # https://youtu.be/--wKPR3ByJc?t=421&si=cslssHb9LKfUiS0N
# ! MAIN IDEA: since we have a distance threshold, it means we should find the SHORTEST PATH from each city to other cities (within reach) to stay within threshold as much as possible while finding how many cities are within reach from each city
    # since we are finding the SHORTEST PATH, i.e. the minimum distance, we use MIN-HEAP
# create adjacency list where key = source city, value = set of tuples (destination_city, distance)
# run Djiikstra's algorithm from each city (source) to find the no. of cities reachable from source city within distanceThreshold
# get the source city with the smallest no. of reachable cities (if there is a tie, return the city with the greater city #)

# TIME COMPLEXITY: O(E log V)
    # each push/pop operation is O(log V)
    # in the worst case, we can push to heap E times (1 for each edge)
    # we perform the above O(E log V) operation for each of the n cities
    # -> overall TC = O(n * (E log V))
# SPACE COMPLEXITY: O(E+V)
    # adjacency list takes O(E+V) space

from collections import defaultdict
from heapq import heappop, heappush

def findTheCity(n, edges, distanceThreshold):
    adj_list = defaultdict(set) # { source_city: set((dest_city1, distance1), (dest_city2, distance2), ...) }
    for a, b, dist in edges:
        adj_list[a].add((b, dist))
        adj_list[b].add((a, dist))
    
    def dijkstra(src): # return no. of cities that can be reached from src that are within distanceThreshold
        min_heap = [(0, src)] # [ (distance_from_src, dest_city) ]
        visited = set() # all the cities we can reach starting from src that are within distanceThreshold

        while min_heap:
            dist_from_src, city = heappop(min_heap)
            if city in visited:
                continue
            visited.add(city)

            for neighbor, dist2 in adj_list[city]: # dist2 = distance between current city and neighbor
                dist_from_src_to_neighbor = dist_from_src + dist2
                if dist_from_src_to_neighbor <= distanceThreshold:
                    heappush(min_heap, (dist_from_src_to_neighbor, neighbor))
        
        return len(visited) - 1 # -1 to exclude src city since it'll be included in visited set
    
    result = -1 # the city no. to be returned (i.e. has the smallest no. of reachable cities within distanceThreshold)
    min_reachable_cities = float('inf') # the smallest no. of reachable cities within distanceThreshold
    for src in range(n): # run dijkstra's algorithm with each city as source city
        cities_count = dijkstra(src)
        if cities_count <= min_reachable_cities: # we use <= so that if there is a tie, we return the city with the greater city #
            min_reachable_cities = cities_count
            result = src
    
    return result