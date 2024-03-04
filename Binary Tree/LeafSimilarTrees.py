# 872. Leaf-Similar Trees
# https://leetcode.com/problems/leaf-similar-trees/description/
# EASY
# Tags: dfslc, leetcode75lc, lc75lc, binarytreelc, #872

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

# ✅ ALGORITHM 1: RECURSIVE DFS

# TIME COMPLEXITY = O(n1 + n2)
    # n1 and n2 are the no.s of nodes in trees root1 and root2 respectively
# SPACE COMPLEXITY = O(h1 + h2)
    # h1 and h2 are the heights trees root1 and root2 respectively

def leafSimilar(root1, root2):
    # dfs(root) returns an array of leaf values of the tree
    def dfs(node, leafs):
        if not node:
            return []
        if not node.left and not node.right: # node is a leaf node
            leafs.append(node.val)
        if node.left: dfs(node.left, leafs)
        if node.right: dfs(node.right, leafs)
        return leafs
    
    return dfs(root1, []) == dfs(root2, [])