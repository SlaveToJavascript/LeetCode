# 2192. All Ancestors of a Node in a Directed Acyclic Graph
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph
# MEDIUM
# Tags: topsortlc, topologicalsortlc, toposortlc, bfslc, queuelc, #2192

# GIVEN:
    # a positive integer, n, representing the number of nodes of a Directed Acyclic Graph (DAG)
        # The nodes are numbered from 0 to n - 1 (inclusive)
    # a 2D integer array, edges, where edges[i] = [from_i, to_i] denotes that there is a unidirectional edge from from_i to to_i in the graph

# TASK:
    # Return a list, answer, where answer[i] is the list of ancestors of the i'th node, sorted in ascending order
        # A node u is an ancestor of another node v if u can reach v via a set of edges

# EXAMPLES:
    # Input: n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
    # Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
    # Explanation:
    # The above diagram represents the input graph.
    # - Nodes 0, 1, and 2 do not have any ancestors.
    # - Node 3 has two ancestors 0 and 1.
    # - Node 4 has two ancestors 0 and 2.
    # - Node 5 has three ancestors 0, 1, and 3.
    # - Node 6 has five ancestors 0, 1, 2, 3, and 4.
    # - Node 7 has four ancestors 0, 1, 2, and 3.

    # Input: n = 5, edgeList = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    # Output: [[],[0],[0,1],[0,1,2],[0,1,2,3]]
    # Explanation:
    # The above diagram represents the input graph.
    # - Node 0 does not have any ancestor.
    # - Node 1 has one ancestor 0.
    # - Node 2 has two ancestors 0 and 1.
    # - Node 3 has three ancestors 0, 1, and 2.
    # - Node 4 has four ancestors 0, 1, 2, and 3.

###########################################################################################################

# ✅ ALGORITHM 1: BFS, TOPOLOGICAL SORT
# 1. Build adjacency list from edges
# 2. Get topological sorting of nodes using BFS
    # maintain array "in_degree" where in_degree[i] = no. of incoming edges for node i (i.e. the no. of ancestors)
    # topological sort order: for every edge u -> v, u comes before v in the topological order
    # we need the topological order so that we can perform BFS on these nodes in order -> when we encounter a node v, all nodes that could potentially reach v (its ancestors) are already known, facilitating efficient construction of ancestor lists
# 3. Get ancestors for each node by performing BFS on topological sort order
# 4. Sort the list of ancestors of each node in ascending order

# TIME COMPLEXITY: O(v^2 log v)
    # v = no. of nodes
    # e = no. of edges
    # 1. creating adjacency list takes O(e)
    # 2. topological sort (BFS) takes O(v+e)
    # 3. get ancestors of each node using topologically sorted list takes O(v^2)
        # worst case: each node is connected to every other node -> update v sets for each of the v nodes -> O(v^2)
    # 4. sorting ancestor list for each node: takes O(v log v) for EACH node
        # there are v nodes -> takes O(v^2 log v)
    # -> overall TC = O(v^2 log v)
# SPACE COMPLEXITY: O(v^2)
    # adjacency list takes O(v+e) space
    # in_degree array takes O(v) space
    # topo_order array takes O(v) space
    # ancestors hashmap contains sets for each node; worst case (where every node is an ancestor of every other node): O(v^2) space needed
    # -> overall SC = O(v^2)

from collections import defaultdict, deque

def find_ancestors(n, edges):
    # 1. Build the graph (adjacency list) and compute in-degrees
    graph = defaultdict(set) # ancestor : { children }
    in_degree = [0] * n
    for a, b in edges:
        graph[a].add(b)
        in_degree[b] += 1

    # 2. Get topologically sorted list using BFS
        # topological sort list: for every edge u -> v, u comes before v in the topological order
    q = deque([i for i in range(n) if in_degree[i] == 0])
    topo_order = []
    while q:
        node = q.popleft()
        topo_order.append(node)

        for child in graph[node]: # visit all children that have current node as an ancestor
            in_degree[child] -= 1 # this means we are processing an edge from current node to its child -> child node has 1 less incoming edge to consider
            if in_degree[child] == 0: # all of child's ancestors (incoming edges) have been processed -> we can now process child node
                q.append(child)
    
    # 3. Get ancestors of each node, using the topologically sorted list
    ancestors = defaultdict(set) # node : { ancestors_of_node }
    for parent in topo_order:
        for child in graph[parent]: # for each child of this parent,
            ancestors[child].update(ancestors[parent]) # add all ancestors of parent to the ancestor set of child (since all ancestors of parent are also ancestors of child)
            ancestors[child].add(parent)
    
    # 4. Sort ancestor list of each node in ascending order and return
    return [sorted(list(ancestors[i])) for i in range(n)]

#==========================================================================================================

# ✅ ALGORITHM 2: RECURSIVE DFS
# each node v is an ancestor for all nodes reachable from it
    # -> initiate DFS from each node and designate that node as an ancestor to all nodes it can reach
# add current node as an ancestor to all children of the node we're currently exploring
# then recursively call DFS on each child until all descendents of ancestor are marked with current node's presence

# TIME COMPLEXITY: O(v^2 log v)
    # v = no. of nodes
    # e = no. of edges
    # creating adjacency list takes O(e)
    # DFS takes O(v^2), as in the worst case, every node might visit every other node during its DFS
    # sorting ancestor list for each node: takes O(v log v) for EACH node
        # there are v nodes -> takes O(v^2 log v)
    # -> overall TC = O(v^2 log v)
# SPACE COMPLEXITY: O(v^2)
    # adjacency list takes O(v+e) space
    # ancestors hashmap contains sets for each node; worst case (where every node is an ancestor of every other node): O(v^2) space needed
    # -> overall SC = O(v^2)

from collections import defaultdict

def getAncestors(n, edges):
    # Build the graph (adjacency list)
    graph = defaultdict(set)
    for a, b in edges:
        graph[a].add(b)
    
    ancestors = defaultdict(set)

    def dfs(node, visited):
        for child in graph[node]: # visit each child of the current node
            if child not in visited:
                visited.add(child)
                ancestors[child].add(node) # add current node to child's ancestors set since current node is an ancestor of the child
                ancestors[child].update(ancestors[node]) # update child's ancestors set with node's ancestors; because since node is a parent of child, then node's ancestors are also child's ancestors
                dfs(child, visited)

    for i in range(n):
        visited = set([i]) # visited set to keep track of nodes already visited in the current DFS traversal to avoid cycles and redundant processing
        dfs(i, visited)
    
    return [sorted(list(ancestors[i])) for i in range(n)]