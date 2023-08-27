# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description
# MEDIUM
# Tags: bstlc, inorderlc, dfslc, stacklc, #230

# GIVEN:
    # the root of a binary search tree
    # an integer k

# TASK:
    # return the kth smallest value (1-indexed) of all the values of the nodes in the tree

# EXAMPLES:
    # Input: root = [3,1,4,null,2], k = 1
    # Output: 1

    # Input: root = [5,3,6,2,4,null,null,1], k = 3
    # Output: 3

###########################################################################################################

# ✅ ALGORITHM 1: RECURSIVE DFS INORDER TRAVERSAL
# We perform an inorder traversal of the tree, appending each node's value to a list
# Once we have the list of all the values, we return the kth smallest value
# Since we are performing an inorder traversal in a BST, the values will be in ascending order

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def kthSmallest(root, k):
    def inorder(node):
        if not node: return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    return inorder(root)[k-1] # k is 1-indexed, so return element at index k-1

#==========================================================================================================

# ✅ ALGORITHM 2: ITERATIVE DFS INORDER TRAVERSAL WITH STACK
# While trying to get to leftmost node, push each node encountered along the way into a stack
# once we encountered a null value while trying to get to the left child, we pop from the stack
    # popping from stack = visited -> if this is the kth node visited, can just return the node
# if the node popped is not the kth node popped, go to the right child of the node we just popped and push it to stack
# repeat until we have popped k nodes from the stack

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def kthSmallest(root, k):
    stack = []
    n = 0 # when n = k, return the popped node
    curr = root

    while curr or stack:
        while curr: # while curr is not null,
            stack.append(curr) # add current node to stack
            curr = curr.left # we are trying to reach the leftmost node until the leftmost node is null

        # at this point, curr is null, so we start popping from stack
        # the top elements in stack are the left elements, followed by parent
        
        curr = stack.pop() # popping an element means we processed it
        n += 1
        if n == k: return curr.val # if we popped k elements, return curr
        curr = curr.right # if curr is not kth element, we start pushing right nodes into stack