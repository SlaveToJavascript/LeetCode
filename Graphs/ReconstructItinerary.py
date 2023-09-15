# https://leetcode.com/problems/reconstruct-itinerary/
# HARD
# Tags: dfslc, graphlc, #332

# GIVEN:
    # a list of airline tickets, where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight

# TASK:
    # Reconstruct the itinerary in order and return it
    # NOTE: All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK"
    # NOTE: If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string
    # You must use all the tickets once and only once

# EXAMPLES:
    # Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    # Output: ["JFK","MUC","LHR","SFO","SJC"]

    # Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    # Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    # Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS

from collections import defaultdict

def findItinerary(tickets):
    # create adjacency list
    adjList = defaultdict(list)
    for src, dest in tickets:
        adjList[src].append(dest)
    
    result = []

    # sort each value (array) in adjacency list
    for key in adjList:
        adjList[key].sort()
    
    def dfs(node):
        while adjList[node]:
            dfs(adjList[node].pop(0)) # recursively visits airport in sorted order of array values in hashmap

        result.append(node) # after all values are visited, start adding these airports to result, starting from last visited airport
    
    dfs("JFK") # start from JFK
    
    return reversed(result) # since airports were added to result array from last airport to first airport visited, return the reversed array