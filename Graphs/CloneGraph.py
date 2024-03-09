# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/description
# MEDIUM
# Tags: hashmaplc, dfslc, graphlc, topinterviewlc, #133

# GIVEN:
    # a reference of a node in a connected undirected graph

# TASK:
    # Return a deep copy (clone) of the graph

# EXAMPLES:
    # Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
        # note: the input is a node but here the graph is referenced by an adjacency list
    # Output: [[2,4],[1,3],[2,4],[1,3]]
    # Explanation: There are 4 nodes in the graph.
    # 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    # 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    # 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    # 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

    # Input: adjList = [[]]
    # Output: [[]]
    # Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

    # Input: adjList = []
    # Output: []
    # Explanation: This an empty graph, it does not have any nodes.

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
# Create hashmap of original nodes mapped to their cloned nodes
# Every time we create a clone, we add it to hashmap
    # then, we iterate through original node's neighbors and clone each neighbor node, and add each neighbor clone to cloned node's neighbors
# if a node is already in hashmap, it means there is already a clone for it -> return the clone

# TIME COMPLEXITY: O(E+V)
    # We visit each node once, and each edge once
# SPACE COMPLEXITY: O(E+V)

def cloneGraph(node):
    hashmap = {} # hashmap of original node : cloned node

    def clone_graph(node):
        if not node: 
            return
        if node in hashmap: # if node has already been cloned before
            return hashmap[node] # return cloned node
        
        clone = Node(node.val) # create clone of node
        hashmap[node] = clone # add clone to hashmap
        for neighbor in node.neighbors: # iterate through original node's neighbors
            clone.neighbors.append(clone_graph(neighbor)) # clone each neighbor and add cloned neighbor to cloned node's neighbors array
        
        return clone
    
    return clone_graph(node)