# https://algo.monster/problems/topo_intro

# ! TOPOLOGICAL SORT vs BFS:
    # BFS: push all the neighboring nodes into the queue
    # Topological sort: only push nodes with 0 in-degree into the queue

# ! MAIN IDEA: Given a directed graph does there exist a way to remove the nodes such that each time we remove a node we guarantee that no other nodes point to that particular node?

# OVERVIEW OF TOPOLOGICAL SORT (Kahn's algorithm)
    # 1. for DIRECTED GRAPHS only
    # 2. it is an ordering of nodes such that every node appears in the ordering before all the nodes it points to
        # e.g. for the following graph, [4, 5, 2] and [5, 4, 2] are valid topological sort
            # 4
            #   \
            #     2
            #   /
            # 3
    # 3. NOT for graphs with cycles