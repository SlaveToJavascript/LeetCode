# 366. Find Leaves of Binary Tree
# https://leetcode.com/problems/find-leaves-of-binary-tree/
# MEDIUM
# Tags: binarytreelc, google, premiumlc, #366

# GIVEN:
    # the root of a binary tree

# TASK:
    # collect a tree's nodes as if you were doing this:
        # Collect all the leaf nodes.
        # Remove all the leaf nodes.
        # Repeat until the tree is empty.
    # Return a 2D array of all deleted leaf nodes' values by layer

# EXAMPLES:
    # Input: root = [1,2,3,4,5]
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    # Output: [[4,5,3],[2],[1]]
    # Explanation:
    # [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each layer it does not matter the order on which elements are returned.

    # Input: root = [1]
    # Output: [[1]]

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS (POSTORDER)
    # https://youtu.be/1T7vwABgiys?si=Jw-JMtj54n77NHr5&t=76
# Since we're deleting leaf nodes by layers, we need to track the nodes deleted and their layers
    # we can use a hashmap where key = layer, value = array of deleted leaf nodes from that layer
        # e.g. hashmap = {
                        # 0: [4,5,3], 
                        # 1: [2], 
                        # 2: [1]
        # }
# We use postorder traversal
    # because every time, we're going to the children first, deleting them if they are leaves, then going to the parents

# TIME COMPLEXITY: O(n)
    # DFS visits each node once
# SPACE COMPLEXITY: O(n)
    # O(n) for hashmap
    # O(n) for recursion stack

from collections import defaultdict

def findLeaves(root):
    result_hashmap = defaultdict(list) # result[i] = layer_number -> [leaf nodes deleted from this layer]
    
    def dfs(node, layer):
        if not node:
            return layer # return the layer where previously passed node was from
        
        # postorder traversal: left -> right -> parent
        left_layer = dfs(node.left, layer)
        right_layer = dfs(node.right, layer)

        curr_layer = max(left_layer, right_layer) # update layer to be the max of left and right
            # *** why do we pick the max of left and right's layers and not min? Check comments below code
        result_hashmap[curr_layer].append(node.val)
        return curr_layer + 1
    
    dfs(root, 0)

    return result_hashmap.values()

# *** WHY DO WE PICK THE MAX OF THE LEFT AND RIGHT'S LAYERS? ***
    # If we pick the min between the left and right's layers, we could potentially be going back in time
    # if the larger value is the one we need, then we could be deleting a node from a layer above (i.e. from a larger layer), which is wrong

    # e.g. step-by-step walkthrough:
        # Input: root =
        #     1
        #    / \
        #   2   3
        #  / \
        # 4   5
    
    # 1. left = dfs(node.left, layer) means when we pass in the root, we will first go to the leftmost node in the tree
    # 2. When we reach node 4, because its left and right children are None, max(0, 0) = 0 is returned to node 4
    # 3. Add node 4 to hashmap at layer 0 -> result = {0: [4]}
    # 4. Node 4 returns layer+1 = 0+1 = 1 to node 2
    # 5. We go into the right subtree of node 2, which is node 5
        # because node 5 has no children, max(0, 0) will be returned to node 5
    # 6. Add node 5 to hashmap at layer 0 -> result = {0: [4,5]}
    # 7. Node 5 returns layer+1 = 0+1 = 1 to node 2
    # 8. Now, at node 2, layer = max(1,1) = 1
    # 9. Add node 2 to hashmap at layer 1 -> result = {0: [4,5], 1: [2]}
    # 10. Node 2 returns layer+1 = 1+1 = 2 to node 1
    # 11. We go into the right subtree of node 1, which is node 3
        # because node 3 has no children, max(0, 0) will be returned to node 3
    # 12. Add node 3 to hashmap at layer 0 -> result = {0: [4,5,3], 1: [2]}
    # 13. Node 3 returns layer+1 = 0+1 = 1 to node 1
    #  ************* 14. Now, at node 1, layer = max(2,1) = 2
        # we choose layer=2 previously returned by node 2, instead of layer=1 returned by node 3
        # choose the max layer so that 1 can be added to the hashmap at the max layer (i.e. layer = max(2,1) = 2 + 1 = 3)
            # if we choose layer=1 (i.e. min layer), node 1 will be added to the result hashmap at layer=1, i.e. the same layer as node 2, which is not what we want