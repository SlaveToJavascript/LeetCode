# https://leetcode.com/problems/leaf-similar-trees/description/
# EASY

# GIVEN:
    # 2 binary trees, root1 and root2

# TASK:
    # return true if the 2 trees have the same leaf value sequence (from left to right of each tree)

# EXAMPLES:
    # Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
    # Output: true

    # Input: root1 = [1,2,3], root2 = [1,3,2]
    # Output: false

###########################################################################################################

# ✅ ALGORITHM 1: RECURSION

# TIME COMPLEXITY = O(v1 + v2)
    # v1 and v2 are the no.s of vertices in trees root1 and root2
# SPACE COMPLEXITY = O(v1 + v2)

def leafSimilar(root1, root2):
    # dfs(root) returns the leaf values of the tree
    def dfs(root):
        if not root.left and not root.right: # i.e. left and right are both null -> root is leaf node
            return [root.val]
        if root.left and root.right: # i.e. root has both left and right children
            return dfs(root.left) + dfs(root.right)
        return dfs(root.left) if root.left else dfs(root.right) # at this point, either root.left is null or root.right is null, but not both
    
    return dfs(root1) == dfs(root2)