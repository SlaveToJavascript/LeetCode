# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# EASY
# Tags: dfslc, bfslc, #104

# GIVEN:
    # root of a binary tree, return its maximum depth 
    # maximum depth is the no. of nodes along the longest path from the root node down to the farthest leaf node

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS
# Depth of a binary tree = 1 + max(depth of left subtree + depth of right subtree)
    # 1 is for the root itself which takes 1 level
# if node is null, depth is 0 (there would be no depth)

# TIME COMPLEXITY = O(n)
    # n = no. of nodes
    # we are traversing the entire tree
# SPACE COMPLEXITY = O(h) or O(n) if it's not a balanced binary tree
    # h = height of tree

def maxDepth(root):
    if not root: return 0 # there would be no depth for a null node
    return 1 + max(maxDepth(root.left), maxDepth(root.right)) # 1 is for the root itself which takes 1 level

#==========================================================================================================

# ✅ ALGORITHM 2: BFS

def maxDepth(root):
    if not root: return 0
    queue = [root]
    depth = 0
    while queue:
        depth += 1
        for _ in range(len(queue)): # use an inner for loop to remove all queue elements then add children
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth

#==========================================================================================================

# ✅ ALGORITHM 3: ITERATIVE DFS
# maintain a stack of [node, depth] where nodes are stored with respective depths in the stack
    # e.g. [root, 0] and [root.left, 1] and [root.right, 1]
# update the max depth every time you pop a node from the array
# after stack is empty, return max_depth

def maxDepth(root):
    # we do not need "if not root: return 0" here since we will be checking if node is null later when popping from stack
    stack = [[root, 1]]
    max_depth = 0
    while stack:
        curr, depth = stack.pop()

        if curr:
            max_depth = max(depth, max_depth)

            stack.append([curr.left, depth+1])
            stack.append([curr.right, depth+1])
    
    return max_depth