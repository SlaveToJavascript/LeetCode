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
    # dfs(root) returns an array of leaf values of the tree
    def dfs(node, leafs):
        if not node: 
            return []
        if not node.left and not node.right: # root is a leaf node
            leafs.append(node.val)
        if node.left: dfs(node.left, leafs)
        if node.right: dfs(node.right, leafs)
        return leafs
    
    return dfs(root1, []) == dfs(root2, [])