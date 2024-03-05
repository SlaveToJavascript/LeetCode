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

# ✅ ALGORITHM: RECURSIVE DFS
    # https://www.youtube.com/watch?v=Nr8dbnL0_cM
# recursively visit each node ; if node is leaf node, add node value to array of leaf values
# check if leaf values arrays of both trees are the same

# TIME COMPLEXITY = O(n1 + n2)
    # n1 and n2 are the no.s of nodes in trees root1 and root2 respectively
# SPACE COMPLEXITY = O(h1 + h2)
    # h1 and h2 are the heights trees root1 and root2 respectively

def leafSimilar(root1, root2):
    # dfs(root) returns an array of leaf values of the tree
    def getLeaves(node, leaves):
        if not node:
            return []
        if not node.left and not node.right: # node is a leaf node
            leaves.append(node.val)
        if node.left: getLeaves(node.left, leaves)
        if node.right: getLeaves(node.right, leaves)
        return leaves
    
    return getLeaves(root1, []) == getLeaves(root2, [])