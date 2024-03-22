# https://leetcode.com/problems/validate-binary-tree-nodes/
# MEDIUM
# Tags: binarytreelc, #1361

# GIVEN:
    # n binary tree nodes numbered from 0 to n-1 where node i has two children leftChild[i] and rightChild[i]
    # If node i has no left child then leftChild[i] will equal -1, similarly for the right child

# TASK:
    # return true if and only if all the given nodes form exactly one valid binary tree

# EXAMPLES:
    # Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
        #     0  
        #    / \ 
        #   1   2
        #  / 
        # 3 
    # Output: true

    # Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
        #   0
        #  / \
        # 1   2
        #  \ /
        #   3
    # Output: false

    # Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
        # 0 <-> 1
    # Output: false

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE DFS
# Requirements for a binary tree:
    # 1) Exactly 1 root node
    # 2) No cycles
    # 3) All nodes reachable from root
    # 4) Each node has at most 2 children

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def validateBinaryTreeNodes(n, leftChild, rightChild):
    child_nodes = set(leftChild + rightChild) # these are child nodes (i.e. they have parent nodes)
    child_nodes.discard(-1) # NOTE: discard(x) removes all instances of x and doesn't raise and error if x doesn't exist, unlike remove()!
    if len(child_nodes) == n:
        return False # this means that every node is a child node, so there's no root node
    
    # FIND ROOT NODE
    root = -1 # we don't know what's the root node, so initialize root node to -1 first
    for i in range(n):
        if i not in child_nodes: # if i is not a child node, then i is a root node
            root = i
            break
    
    visited = set()
    def dfs(i):
        if i == -1:
            return True # this means i is a LEAF NODE -> return True as path is valid up till this point
        if i in visited:
            return False # i is visited before -> there is a cycle! ❌
        
        visited.add(i)
        return dfs(leftChild[i]) and dfs(rightChild[i]) # recursively checks the left and right children of i for further exploration
    
    return dfs(root) and len(visited) == n