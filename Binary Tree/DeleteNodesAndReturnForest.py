# https://leetcode.com/problems/delete-nodes-and-return-forest/description/
# MEDIUM
# Tags: dfslc, postorderlc, #1110

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
# When we delete a node, we also have to deal with its children
    # Recursively, we try to delete smaller and smaller trees
# When we delete a node, its children (if any) will automatically become new roots
    # However, we can't add these children (new roots) to our answer automatically, as these children's children etc. also have to be checked for deletions

# While traversing a tree, at every node there are 2 options:
# 1. delete the node -> we will delete it and then recurse the dfs into its children
# 2. don't delete the node -> check if we need to delete any of its children 
                                # if yes, i.e. must delete child(ren) -> set child(ren) to null
                                # recurse the dfs on its child(ren)

# TIME COMPLEXITY: O(n)
    # DFS visits each node once
# SPACE COMPLEXITY: O(n)

def delNodes(root, to_delete):
    to_delete = set(to_delete) # change to_delete array to set for quick lookups

    remaining_roots = [] # this is our return value

    # this is our helper function
    def dfs(node, to_delete, is_root): # is_root indicates if node is the root of a tree
        if not node: return # stopping condition

        if node.val in to_delete: # if node needs to be deleted, recurse dfs to children
            dfs(node.left, to_delete, True) # is_root=True bc child is now a root node since its parent is deleted
            dfs(node.right, to_delete, True)
            # at this point, the current node would have been deleted
        else: # if current node doesn't need to be deleted, we check if child(ren) needs to be deleted
            if node.left:
                if node.left.val in to_delete: # if left child needs to be deleted,
                    dfs(node.left, to_delete, True)
                    node.left = None # remove left child by setting it to null
                else: # if we do not need to delete left child
                    dfs(node.left, to_delete, False) # we continue with our dfs
            # now do the same thing for the right child
            if node.right:
                if node.right.val in to_delete: # if right child needs to be deleted,
                    dfs(node.right, to_delete, True)
                    node.right = None # remove right child by setting it to null
                else: # if we do not need to delete right child
                    dfs(node.right, to_delete, False) # we continue with our dfs
            
            if is_root: # if current node is root, and doesn't need to be deleted, we add it to return arr
                remaining_roots.append(node)

    dfs(root, to_delete, True) # start dfs from the root node
    return remaining_roots