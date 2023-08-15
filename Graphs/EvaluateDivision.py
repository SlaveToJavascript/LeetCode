# https://leetcode.com/problems/evaluate-division/description/
# MEDIUM
# Tags: graphlc, bfslc, #399

# GIVEN:
    # an array of variable pairs, equations
        # where equations[i] = [Ai, Bi]
    # an array of real numbers, values
        # where values[i] represent the equation Ai / Bi = values[i]
    # Each Ai or Bi is a string that represents a single variable
    # array queries
        # where queries[j] = [Cj, Dj] represents a query where you must find the answer for Cj / Dj = ?

# TASK:
    # Return the answers to all queries
    # If a single answer cannot be determined, return -1.0

# EXAMPLES:
    # Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    # Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    # Explanation: 
    # Given: a / b = 2.0, b / c = 3.0
    # queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
    # return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
    # note: x is undefined => -1.0

    # Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    # Output: [3.75000,0.40000,5.00000,0.20000]

    # Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
    # Output: [0.50000,2.00000,-1.00000,-1.00000]

###########################################################################################################

# ✅ ALGORITHM 1: GRAPH DFS
# The problem can be represented as a graph problem, where each numerator (node) points to the denominator (node), and the edges between 2 nodes (a numerator and a denominator) is the value of their division
    # This works because e.g. we have a/b = 2 and b/c = 3, now the query we want to find the solution for is a/c, so we simply take 2*3 = 6 which is the answer for a/c
    # In algebra, if we do (a/b) * (b/c), we get a/c since the b is cancelled out -> we use the same multiplication to get a/c
    # e.g. the 1st example would look like:
    
    #   2    3
    # a -> b -> c

    # a/c = 2 * 3

# For this example, if we want to find c/a, we would traverse the inverse direction of graph above
    # i.e. traverse a <- b <- c
    # and the weights of the edges would be the inverse
    # e.g. for the example above, to find c/a:

    #   1/2   1/3
    # a <-- b <-- c

    # c/a = 1/3 * 1/2 = 1/6

# STEPS:
    # build adjacency list using the equations and values array (do the inverse also e.g. b/a)
    # implement BFS function bfs(numerator, denominator) that returns the result of numerator/denominator
        # can do DFS or BFS, but easier for BFS to do cycle detection, and it's possible that graph has a cycle
    # For each query in queries array, run bfs function on the 2 values in query and append division result to result array

# TIME COMPLEXITY: O(q * e)
    # q = no. of queries
    # e = no. of equations
    # we have to traverse all the equations to build the adjacency list
    # and we have to traverse all the queries to get the result
# SPACE COMPLEXITY: O(V+E)
    # for adjacency list

from collections import defaultdict

def calcEquation(equations, values, queries):
    adjList = defaultdict(list) # key = numerator, value = 2D list of [denominator, division value]

    for i, eqn in enumerate(equations):
        numerator, denominator = eqn
        # add numerator to lists
        adjList[numerator].append((denominator, values[i]))
        # add denominator to list (inverse)
        adjList[denominator].append((numerator, 1/values[i]))
    
    # returns the result of src/target, e.g. a/b
        # we need to find the product of the path from a -> b
    def bfs(src, target):
        if src not in adjList or target not in adjList:
            return -1
        
        q = [ (src, 1) ] # q[i] = (src, product of edges so far i.e. from src to current node)
            # product of edges is initialized to 1
        visited = set()
        visited.add(src)

        while q:
            node, product = q.pop(0)
            if node == target:
                return product
            
            for neighbor, weight in adjList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, product * weight))
        
        return -1 # both src and target exist in the graph, but there are no edges connecting them
    
    result = []
    for query in queries:
        result.append(bfs(query[0], query[1]))
    
    return result
    # or instead of the 4 lines above, you can simply do:
        # return [bfs(query[0], query[1]) for query in queries]