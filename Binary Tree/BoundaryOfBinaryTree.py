# 545. Boundary of Binary Tree
# https://leetcode.com/problems/boundary-of-binary-tree/
# MEDIUM
# Tags: binarytreelc, dfslc, premiumlc, #545

# The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.
# The left boundary is the set of nodes defined by the following:
    # The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
    # If a node in the left boundary and has a left child, then the left child is in the left boundary.
    # If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
    # The leftmost leaf is not in the left boundary.
# The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.
# The leaves are nodes that do not have any children. For this problem, the root is not a leaf.
# Given the root of a binary tree, return the values of its boundary.

# EXAMPLES:
    # Input: root = [1,null,2,3,4]
    # Output: [1,3,4,2]
    # Explanation:
    # - The left boundary is empty because the root does not have a left child.
    # - The right boundary follows the path starting from the root's right child 2 -> 4.
    #   4 is a leaf, so the right boundary is [2].
    # - The leaves from left to right are [3,4].
    # Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].

    # Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
    # Output: [1,2,4,7,8,9,10,6,3]
    # Explanation:
    # - The left boundary follows the path starting from the root's left child 2 -> 4.
    #   4 is a leaf, so the left boundary is [2].
    # - The right boundary follows the path starting from the root's right child 3 -> 6 -> 10.
    #   10 is a leaf, so the right boundary is [3,6], and in reverse order is [6,3].
    # - The leaves from left to right are [4,7,8,9,10].
    # Concatenating everything results in [1] + [2] + [4,7,8,9,10] + [6,3] = [1,2,4,7,8,9,10,6,3].

###########################################################################################################

# ✅ ALGORITHM: SPLIT INTO LEFT BOUNDARY + LEAVES + RIGHT BOUNDARY
# LEFT BOUNDARY:
    # keep traversing into the left child of the tree and keep adding the left nodes into the result array (as long as it's not a leaf node)
    # if at any point the left child does not exist, add the right child instead and continue the process
# LEAF NODES (BOTTOM BOUNDARY):
    # use recursive function addLeaves(node), which adds all leaf nodes descending from a certain node (in this case the root node) to the result array
    # If the current root node is a leaf node, it is added to result array
    # Otherwise, we make the recursive call using the left child of the current node as the new root. After this, we make the recursive call using the right child of the current node as the new root
# RIGHT BOUNDARY:
    # perform the same process as the left boundary, except this time we keep traversing into the RIGHT child of the tree and keep adding the RIGHT nodes into a stack (as long as it's not a leaf node)
    # add the nodes added to this stack to the result array in reverse order

# TIME COMPLEXITY: O(n)
    # adding left boundary nodes: takes O(h), where h = height of binary tree
    # adding leaf nodes: takes O(n), i.e. 1 complete traversal where each node is visited once
    # adding right boundary nodes: takes O(h), where h = height of binary tree
# SPACE COMPLEXITY: O(n)
    # for result and stack

def boundaryOfBinaryTree(root):
    result = []
    if not root:
        return result # edge case: if binary tree is null
    
    def is_leaf(node): # checks if node is a leaf node
        return not node.left and not node.right
    
    # adds all leaf nodes that descend from "node" to result array
    def add_leaves(node):
        if is_leaf(node):
            result.append(node.val)
        else:
            if node.left:
                add_leaves(node.left)
            if node.right:
                add_leaves(node.right)
    
    if not is_leaf(root): # if root is not leaf, add it to result array (if root is leaf, it'll be added to the array by the add_leaves() function)
        result.append(root.val)
    
    # LEFT BOUNDARY (excluding leaf nodes)
    curr = root.left
    while curr:
        if not is_leaf(curr): # if current node is not leaf, add it to result
            result.append(curr.val)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right
    
    # BOTTOM BOUNDARY (leaf nodes)
    add_leaves(root)

    # RIGHT BOUNDARY (excluding leaf nodes, in reverse order)
    stack = []
    curr = root.right
    while curr:
        if not is_leaf(curr):
            stack.append(curr.val)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    result.extend(reversed(stack)) # right boundary nodes should be added to result in reverse order
    
    return result