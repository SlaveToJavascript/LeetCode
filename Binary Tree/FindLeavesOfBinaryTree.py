# https://leetcode.com/problems/find-leaves-of-binary-tree/
# MEDIUM
# Tags: binarytreelc, google, #366

# Given a binary tree, collect and remove all leaf nodes, repeat until the tree is empty
# Return a 2D array of all deleted leaf nodes' values by layer

# EXAMPLES:
    # Input: root =
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    # Output: [[4,5,3],[2],[1]]
    # For more examples, see https://www.lintcode.com/problem/650/description

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
# Since we're deleting leaf nodes by layers, we need to track the nodes deleted and their layers
    # we can use a hashmap where key = layer, value = array of deleted leaf nodes from that layer
        # e.g. hashmap = {
                        # 0: [4,5,3], 
                        # 1: [2], 
                        # 2: [1]
        # }
# We use postorder traversal
    # because every time, we're going to the children first, deleting them if they are leaves, then going to the parents

import collections

def findLeaves(root):
    result = collections.defaultdict(list) # result[i] = level -> [leaf nodes deleted from level]
    
    def dfs(node, level):
        if not node:
            return level # return the level where previously passed node was from
        
        # postorder traversal: left -> right -> parent
        left = dfs(node.left, level)
        right = dfs(node.right, level)

        level = max(left, right) # update level to be the max of left and right
            # *** why do we pick the max of left and right's levels and not min? Check comments below code

        result[level].append(node.val)

        return level + 1
    
    dfs(root, 0)

    return result.values()

# *** WHY DO WE PICK THE MAX OF THE LEFT AND RIGHT'S LEVELS? ***
    # If we pick the min between the left and right's levels, we could potentially be going back in time
    # if the larger value is the one we need, then we could be deleting a node from a level above (i.e. from a larger level), which is wrong

    # e.g. step-by-step walkthrough:
        # Input: root =
        #     1
        #    / \
        #   2   3
        #  / \
        # 4   5
    
    # 1. left = dfs(node.left, level) means when we pass in the root, we will first go to the leftmost node in the tree
    # 2. When we reach node 4, because its left and right children are None, max(0, 0) = 0 is returned to node 4
    # 3. Add node 4 to hashmap at level 0 -> result = {0: [4]}
    # 4. Node 4 returns level+1 = 0+1 = 1 to node 2
    # 5. We go into the right subtree of node 2, which is node 5
        # because node 5 has no children, max(0, 0) will be returned to node 5
    # 6. Add node 5 to hashmap at level 0 -> result = {0: [4,5]}
    # 7. Node 5 returns level+1 = 0+1 = 1 to node 2
    # 8. Now, at node 2, level = max(1,1) = 1
    # 9. Add node 2 to hashmap at level 1 -> result = {0: [4,5], 1: [2]}
    # 10. Node 2 returns level+1 = 1+1 = 2 to node 1
    # 11. We go into the right subtree of node 1, which is node 3
        # because node 3 has no children, max(0, 0) will be returned to node 3
    # 12. Add node 3 to hashmap at level 0 -> result = {0: [4,5,3], 1: [2]}
    # 13. Node 3 returns level+1 = 0+1 = 1 to node 1
    #  ************* 14. Now, at node 1, level = max(2,1) = 2
        # we choose level=2 previously returned by node 2, instead of level=1 returned by node 3
        # choose the max level so that 1 can be added to the hashmap at the max level
            # if we choose level=1 (i.e. min level), node 1 will be added to the result hashmap at level=1, i.e. the same level as node 2, which is not what we want