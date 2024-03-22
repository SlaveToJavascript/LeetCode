# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
# MEDIUM
# Tags: binarytreelc, dfslc, leetcode75lc, lc75lc,  #236

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).

# EXAMPLES:
    # Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    # Output: 3
    # Explanation: The LCA of nodes 5 and 1 is 3.

    # Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    # Output: 5
    # Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

    # Input: root = [1,2], p = 1, q = 2
    # Output: 1

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS
    # https://www.youtube.com/watch?v=WO1tfq2sbsI
# 2 situations:
    # 1. p and q are in different subtrees of root -> LCA is the parent of the node (p/q) that is closest to the root
    # 2. p is a child of q or vice versa -> LCA is the node (p/q) that is closest to the root
# STEPS:
# 1. lowestCommonAncestor() function takes in 3 parameters: the root of a binary tree (root) and two nodes of the binary tree (p and q)
# 2. Base cases: If root is null, return null
    # If root is p or q, return root (this means that we have found one of the nodes we are looking for)
# 3. recursively call the lowestCommonAncestor() function on the left and right subtrees of the root
    # We store the results of these recursive calls in variables left and right, respectively
# 4. if both left and right are not null, it means that we have found both p and q in different subtrees of the current root -> therefore the current root is the lowest common ancestor, so we return the current root
# 5. if left is null and right is not null, it means we found both p and q in the right subtree -> return right (right is the node p or q that is closest to the root node)
# 6. vice versa, if right is null and left is not null, it means we found both p and q in the left subtree -> return left (left is the node p or q that is closest to the root node)

# TIME COMPLEXITY: O(N) -> we visit every node in the tree
# SPACE COMPLEXITY: O(N) -> we store the entire tree in memory

def lowestCommonAncestor(root, p, q):
    if not root: 
        return
    if root == p or root == q: # if root is either p or q, then root is the LCA for this subtree which contains p or q
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right: # if both left and right are not null, it means that we have found both p and q in different subtrees of the current root
        return root # therefore the current root is the lowest common ancestor, so we return the current root
    
    return left or right # if only one out of left and right is not null, it means both p and q are found in the same (left/right) subtree -> return the non-null subtree

#==========================================================================================================

# ✅ ALGORITHM 2: ITERATIVE DFS
# To find the lowest common ancestor, we need to find where is p and q
# We also need to track their ancestors
    # to do this, we use a parent hashmap where the key is a child node and the value is its parent node
# After we found both p and q, we create a set of p's ancestors (using parent hashmap)
# Then we travel through q's ancestors (stored in parent), and the first ancestor of q that appears in p's ancestor set is our answer

def lowestCommonAncestor(root, p, q):
    parent = { root: None } # the root node doesn't have any parent
    stack = [root]

    while p not in parent or q not in parent: # while p and q are both not in parent hashmap,
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    # at this point, both p and q are in parent hashmap
    
    p_ancestors = set()

    while p != None:
        p_ancestors.add(p)
        p = parent[p] # using parent hashmap, add p and all of p's ancestors to the set
    
    while q not in p_ancestors:
        q = parent[q] # use q to store all of q's ancestors and check if these ancestors are in p_ancestors
    
    return q # here, q is the lowest common ancestor of both q and p