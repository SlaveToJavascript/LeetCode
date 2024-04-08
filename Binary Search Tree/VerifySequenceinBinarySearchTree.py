# 255. Verify Preorder Sequence in Binary Search Tree
# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/
# MEDIUM
# Tags: bstlc, monotonicstacklc, #255

# GIVEN:
    # an array of unique integers, preorder

# TASK:
    # return true if it is the correct preorder traversal sequence of a binary search tree

# EXAMPLES:
    # Input: preorder = [5,2,1,3,6]
    # Output: true

    # Input: preorder = [5,2,6,1,3]
    # Output: false

###########################################################################################################

# ✅ ALGORITHM: DECREASING MONOTONIC STACK
# preorder = parent -> left -> right
    # 1st element is root
    # When we encounter a sequence of decreasing numbers, we continuously "walk" left, since they are the left children
        # e.g. preorder = [5, 2, 1, 3, 6]
            # 5 is root node
            # 2 < 5, therefore 2 is left child of 5
            # 1 < 2, therefore 1 is left child of 2
                #     5
                #    /
                #   2
                #  /
                # 1
    # if we encounter a larger element, we backtrack to find the largest value that is smaller than this larger element
        # 3 cannot possibly be the right child of 1 since 3 is greater than 2!
                #     5
                #    /
                #   2
                #  / \
                # 1   3
        # NOTE: We need to use a stack to emulate "moving" back up the tree, just like how recursion is implemented
# MAIN IDEA:
    # At any given moment, the node at the top of the stack is the current node we are at in the tree
    # For each node.val we visit, if the existing value at the top of the stack > num, we can just push this node.val onto the stack
    # If the value at the top of the stack < num, we need to backtrack up the tree by popping from the stack
        # After we backtrack (i.e. pop from) the stack to ensure monotonic order, we can push current node.val to the stack
        # the popped elements are the entire left subtree of the stack which are no longer needed
            # In a preorder traversal, a node's left subtree is visited completely before any node in the right subtree is visited. Because we are now in the right subtree, we can completely forget about the left subtree.
    # ❌ BUT if have discarded a left subtree from the stack, and then we encounter a no. smaller than the root of the left subtree that got discarded, we will incorrectly add this smaller no. as the left child of the right node, when in reality having this smaller no. means that the preorder array cannot form a valid BST!
        # -> RULE OBSERVED: When we pop from the stack (i.e. return from a node), every value we encounter from now on must be greater than node! Otherwise, it's an invalid BST
            # to resolve this issue, we implement a min_limit variable, where if any value encountered in preorder array is <= min_limit, return False as preorder cannot possibly be a valid BST
                # # If we encountered a node.val <= min_limit in the future, it would mean that this node.val belongs in the left subtree of the min_limit node, but since we already "returned" from the min_limit node, we have already visited all the nodes in the left subtree!

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
    # for stack

def verifyPreorder(preorder):
        min_limit = float('-inf') # since we need to find a num > min_limit, initialize min_limit to a small no.
        stack = []

        for num in preorder:
            while stack and stack[-1] < num: # keep backtracking up the tree to find the node which is the parent of the right child, num
                min_limit = stack.pop() # backtrack by popping nodes from the stack

            if num <= min_limit: # num belongs in the left subtree which has already been discarded -> preorder is an invalid BST
                return False
            
            stack.append(num) # if num < value at top of stack, add num to stack as it's the left child of node at top of stack
        
        return True