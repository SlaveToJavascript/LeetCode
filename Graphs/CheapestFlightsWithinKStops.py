# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# MEDIUM

# GIVEN:
    # number of cities, n
    # array, flights, where flights[i] = [from_i, to_i, price_i]
    # integer, src
    # integer, dst
    # integer, k

# TASK:
    # return the cheapest price from src to dst with at most k stops
    # If there is no such route, return -1

# EXAMPLES:
    # Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
    # Output: 700
    # Explanation:
    # The graph is shown above.
    # The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
    # Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

    # Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
    # Output: 200
    # Explanation:
    # The graph is shown above.
    # The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

    # Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
    # Output: 500
    # Explanation:
    # The graph is shown above.
    # The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

###########################################################################################################

# ALGORITHM 1: BELLMAN-FORD ALGORITHM
# Similar to BFS
# Start from src node
# While traversing, simultaneously keep track of, for each node that has been visited, what's the min. price it takes to reach that node 
# do k+1 layers of BFS
    # since there can be k stops, that means there can be k+1 edges from src to dst

# TIME COMPLEXITY: O(E * k), where E = no. of edges

def findCheapestPrice(n, flights, src, dst, k):
    prices = [float('inf')] * n
    prices[src] = 0 # price to get from src to src is 0

    for _ in range(k+1): # k+1 is bc there are max. k stops = there are max. k+1 edges from src to dest
        temp_prices = prices[:] # tracks updates in prices before being copied to prices array
        for source, destination, price in flights:
            # if prices[source] == float('inf'): continue # this line is optional
            if prices[source] + price < temp_prices[destination]:
                temp_prices[destination] = prices[source] + price
        prices = temp_prices
    return -1 if prices[dst] == float('inf') else prices[dst]