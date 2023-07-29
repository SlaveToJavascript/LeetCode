# https://leetcode.com/problems/binary-tree-right-side-view/description/
# MEDIUM
# Tags: bfslc, #199

# GIVEN:
    # the root of a binary tree

# TASK:
    #  imagine yourself standing on the right side of it
    # return the values of the nodes you can see ordered from top to bottom
    # NOTE: you will be able to see a node in the tree as long as there are no other nodes on the right blocking it

# EXAMPLES:
    # Input: root = [1,2,3,null,5,null,4,7]
    # Output: [1,3,4,7]

    # Input: root = [1,null,3]
    # Output: [1,3]

    # Input: root = []
    # Output: []

###########################################################################################################

# ✅ ALGORITHM 1: BFS (space complexity not optimized)
# Using BFS, store the node vals of all nodes in each level into separate arrays
# Return an array of the last elements from each level's node val arrays
    # the last element from each level will be the rightmost node (which you see) from that level

# TIME COMPLEXITY: O(n)
    # BFS visits each node once
# SPACE COMPLEXITY: O(2n)
    # O(n) for queue
    # O(n) for level_nodes array

def rightSideView(root):
    rightmost_nodes = [] # this is the return value

    q = [root]
    while q:
        curr_level_nodes = [] # stores the values of all nodes from the current level
        for _ in range(len(q)): # for-loop iterates within the current level
            node = q.pop(0)
            curr_level_nodes.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
        # at this point (i.e. at the end of every for-loop), q contains only elements from next level
        rightmost_nodes.append(curr_level_nodes[-1]) # the last node from current level will be the node you can see
    
    return rightmost_nodes

#==========================================================================================================

# ✅✅✅ ALGORITHM 1A: BFS (slightly optimized with O(n) space complexity)
# Same as above, except instead of using a curr_level_nodes array to store all nodes in the current array, just keep track of the last node in each level
# Space complexity is slightly optimized

# TIME COMPLEXITY: O(n)
    # BFS visits each node once
# SPACE COMPLEXITY: O(n)
    # O(n) for queue

def rightSideView(root):
    rightmost_nodes = [] # this is the return value

    q = [root]
    while q:
        for _ in range(len(q)): # for-loop iterates within the current level
            node = q.pop(0)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
        # at this point (i.e. at the end of every for-loop), node variable will store the last node in that level, since the the current for-loop iterates within the current level
        rightmost_nodes.append(node.val) # the last node from current level will be the node you can see
    
    return rightmost_nodes