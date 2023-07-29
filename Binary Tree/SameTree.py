# https://leetcode.com/problems/same-tree/description/
# EASY
# Tags: dfslc, bfslc, #100

# GIVEN:
    # the roots of 2 binary trees, p and q, return True if they are the same tree
    # binary trees are same if they are structurally identical, and nodes have the same value

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS
# Criteria for same binary trees:
    # 1) p's root val = q's root val
    # 2) p's left subtree = q's left subtree
    # 3) p's right subtree = q's right subtree

# TIME COMPLEXITY: O(n)
    # since each node is visited once
# SPACE COMPLEXITY: O(n)
    # in the worst case of completely unbalanced tree, to keep a recursion stack

def isSameTree(p, q):
    if not p and not q: # both p and q are null
        return True
    if not p or not q: # either p is null or q is null, but not both
        return False
    
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

#==========================================================================================================

# ✅ ALGORITHM 2: ITERATIVE BFS
# Start from the root of both trees
# at each iteration, pop current node out of queue
# Perform checks:
    # p and q are both not null
    # p.val == q.val
# if checks are ok, enqueue p's and q's child nodes into queue
# else, return False

# TIME COMPLEXITY: O(n)
    # since each node is visited once
# SPACE COMPLEXITY: O(n)
    # this is worst case, where tree is a perfect fully balanced binary tree
        # since BFS will have to store at least an entire level of the tree in the queue, and the last level has O(n) nodes

def isSameTree(p, q):
    def check(p, q):
        if not p and not q: # if both are None
            return True
        if not q or not p: # either p is null or q is null, but not both
            return False
        if p.val != q.val:
            return False
        return True
    
    stack = [[p, q]]
    while stack:
        p, q = stack.pop()

        if not check(p, q):
            return False
        
        if p and q:
            stack.append([p.left, q.left])
            stack.append([p.right, q.right])
    
    return True