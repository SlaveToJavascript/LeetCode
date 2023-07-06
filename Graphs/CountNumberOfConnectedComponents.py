# https://www.structy.net/problems/connected-components-count

# GIVEN:
    # graph, the adjacency list of an undirected graph

# TASK:
    # return the number of connected components in the graph
        # i.e. return the number of separate connected graphs

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
# define a recursive dfs function that returns False if current node is in visited; returns True after completely traversing across a connected graph
# Traverse graph and call dfs() on each node while keeping track of visited nodes
    # if True is returned, it means one connected graph has finished traversing -> increment counter
# return counter

# TIME COMPLEXITY: O(e), e = no. of edges
# SPACE COMPLEXITY: O(n), n = no. of nodes

def connected_components_count(graph):
  
  def dfs(graph, current, visited):
    if current in visited: return False
    visited.add(current)
    
    for neighbor in graph[current]:
      dfs(graph, neighbor, visited)
    return True
  
  visited = set()
  count = 0
  for node in graph:
    if dfs(graph, node, visited):
      count += 1
  
  return count