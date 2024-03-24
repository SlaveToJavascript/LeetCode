# 1110. Delete Nodes And Return Forest
# https://leetcode.com/problems/delete-nodes-and-return-forest/description/
# MEDIUM
# Tags: dfslc, postorderlc, binarytreelc, #1110

# GIVEN:
    # root of a binary tree
    # list of node values to delete

# TASK:
    # After deleting nodes with values in to_delete, we are left with a forest (disjoint union of trees)
    # Return the roots of the trees in the remaining forest

# EXAMPLES:
    # Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
    # Output: [[1,2,null,4],[6],[7]]

    # Input: root = [1,2,4,null,3], to_delete = [3]
    # Output: [[1,2,4]]

###########################################################################################################

# ✅ ALGORITHM 1: DFS (POSTORDER)
    # https://www.youtube.com/watch?v=tr-HUE_cEQ0&t=667s
# When we delete a node, we also have to deal with its children
    # Recursively, we try to delete smaller and smaller trees
# When we delete a node, its children (if any) will automatically become new roots
    # However, we can't add these children (new roots) to our answer automatically, as these children's children etc. also have to be checked for deletions

# MAIN IDEA:
    # While traversing a tree, at every node there are 2 options:
    # 1. delete the node -> we will delete it and then recurse the dfs into its children to process them
    # 2. don't delete the node -> check if we need to delete any of its children 
                                    # if yes, i.e. must delete child(ren)
                                    # recurse the dfs on its child(ren) to process them
                                    # set child(ren) to null

# TIME COMPLEXITY: O(n) + O(d)
    # n = no. of nodes
    # d = no. of nodes to delete
# SPACE COMPLEXITY: O(n) + O(d)
    # O(n) for the recursion call stack
    # O(d) for to_delete set

def delNodes(root, to_delete):
    to_delete = set(to_delete) # change to_delete array to set for quick lookups

    result = [] # this is our return value

    # this is our helper function
    def dfs(node, is_root): # is_root indicates if node is the root of a tree
        if not node: 
            return # stopping condition

        if node.val in to_delete: # if node needs to be deleted, recurse dfs to children
            dfs(node.left, True) # is_root=True bc child is now a root node since its parent is deleted
            dfs(node.right, True)
            # at this point, the current node would have been deleted
        
        else: # if current node doesn't need to be deleted, we check if child(ren) needs to be deleted
            if node.left:
                if node.left.val in to_delete: # if left child needs to be deleted,
                    dfs(node.left, True) # we need to first process this left child to be deleted
                        # is_root can be True/False, doesn't matter
                    node.left = None # remove left child by setting it to null
                else: # if we do not need to delete left child
                    dfs(node.left, False) # continue with dfs
                        # is_node = False bc that node will not be a root (as it's still connected to a parent)
            
            # do the same thing for the right child
            if node.right:
                if node.right.val in to_delete: # if right child needs to be deleted,
                    dfs(node.right, True) # we need to first process this right child to be deleted
                        # is_root can be True/False, doesn't matter
                    node.right = None # remove right child by setting it to null
                else: # if we do not need to delete right child
                    dfs(node.right, False) # continue with dfs
                        # is_node = False bc that node will not be a root (as it's still connected to a parent)
            
            if is_root: # if current node is root, and doesn't need to be deleted, we add it to return array
                result.append(node)

    dfs(root, True) # start dfs from the root node
    return result