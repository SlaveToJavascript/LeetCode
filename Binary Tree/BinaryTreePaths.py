# https://leetcode.com/problems/binary-tree-paths/description/
# EASY
# Tags: dfslc, binarytreelc, #257

# GIVEN:
    # a binary tree, root

# TASK:
    # return list of all root-to-leaf paths, e.g. ["1->2->5","1->3"]

# EXAMPLES:
    # Input: root = [1,2,3,null,5]
    # Output: ["1->2->5","1->3"]

    # Input: root = [1]
    # Output: ["1"]

###########################################################################################################

# ✅✅ ALGORITHM 1: RECURSIVE DFS
# Use recursive dfs function to populate array of string paths from root to leaves
# recursive dfs function:
    # if string is not empty string, add "->" to string
    # add current node's value to string
    # if current node is leaf node, add string to array of paths
    # else, recursively call dfs function on left and right children

# TIME COMPLEXITY: O(n), n = no. of nodes
# SPACE COMPLEXITY: O(n), n = no. of nodes

def binaryTreePaths(root):
    result = []

    def dfs(node, s):
        if not node: return
        if s: s += "->"
        s += str(node.val)
        if not node.left and not node.right: # if node is leaf node
            result.append(s) # add current path to result
        if node.left: dfs(node.left, s)
        if node.right: dfs(node.right, s)
    
    dfs(root, "")
    return result

#==========================================================================================================

# ✅ ALGORITHM 2: DFS (GET ALL PATHS THEN FORMAT STRINGS TO RETURN)
# Use DFS to get all paths from root to leaves and append them to array
# format each path into the required format and return

# TIME COMPLEXITY: O(n), n = no. of nodes
# SPACE COMPLEXITY: O(n), n = no. of nodes

def binaryTreePaths(root):
    paths = []

    def dfs(node, path):
        if not node: return
        path = path + [node.val]
        if not (node.left or node.right): # if node is leaf node
            return paths.append(path)
        dfs(node.left, path)
        dfs(node.right, path)
    
    dfs(root, [])

    return ['->'.join(map(str, path)) for path in paths]