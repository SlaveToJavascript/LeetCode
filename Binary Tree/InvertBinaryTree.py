# https://leetcode.com/problems/invert-binary-tree/description/
# EASY
# Tags: dfslc, bfslc, binarytreelc, #226

# GIVEN:
    # the root of a binary tree, invert the tree, and return its root

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS
# After the inversion:
    # root.left = root.right

    # root.left.left = root.right.right
    # root.left.right = root.right.left

    # root.right.left = root.left.right
    # root.right.right = root.left.left
# Summary: change every node's left subtree into its right subtree and right subtree into left subtree

# TIME COMPLEXITY: O(n)
    # Since each node in the tree is visited only once
# SPACE COMPLEXITY: O(n)
    # Because of recursion, O(h) function calls will be placed on the stack in the worst case
    # since h ∈ O(n), space complexity is O(n)

def invertTree(root):
    if not root: 
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root

#==========================================================================================================

# ✅ ALGORITHM 2: ITERATION (BFS)
# Idea: need to swap left and right children of all nodes in the tree
# create a queue (with root node) to store nodes whose left and right child have not been swapped yet
# while queue is not empty, pop the next node from the queue, swap its children, and add the children to the queue
    # Null nodes are not added to queue
# Eventually, queue will be empty and all children swapped
# return the original root.

# TIME COMPLEXITY: O(n)
    # Since each node in the tree is visited / added to the queue only once
# SPACE COMPLEXITY: O(n)
    # since in the worst case, the queue will contain all nodes in one level of the binary tree
    # For a full binary tree, the leaf level has n/2 = O(n) leaves

def invertTree(root):
    if not root: 
        return None

    queue = [root]
    
    while queue:
        curr = queue.pop(0)

        curr.left, curr.right = curr.right, curr.left

        if curr.left: 
            queue.append(curr.left)
        if curr.right: 
            queue.append(curr.right)

    return root