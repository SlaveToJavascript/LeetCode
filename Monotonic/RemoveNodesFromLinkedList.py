# 2487. Remove Nodes From Linked List
# https://leetcode.com/problems/remove-nodes-from-linked-list/
# MEDIUM
# Tags: linkedlistlc, monotonicstacklc, monotoniclc, stacklc, #2487

# GIVEN:
    # the head of a linked list

# TASK:
    # Remove every node which has a node with a greater value anywhere to the right side of it
    # Return the head of the modified linked list

# EXAMPLES:
    # Input: head = [5,2,13,3,8]
    # Output: [13,8]
    # Explanation: The nodes that should be removed are 5, 2 and 3.
    # - Node 13 is to the right of node 5.
    # - Node 13 is to the right of node 2.
    # - Node 8 is to the right of node 3.

    # Input: head = [1,1,1,1]
    # Output: [1,1,1,1]
    # Explanation: Every node has value 1, so no nodes are removed.

###########################################################################################################

# ✅ ALGORITHM: MONOTONIC STACK
# the resulting LL to be returned should be a decreasing LL since we need to remove all no.s on the left that are less than any no.s on the right
# hence we can use a monotonic stack to store nodes with decreasing values
# iterate through LL, and if any node has val > node at top of stack, keep popping from stack until current node.val < node at top of stack
# chain up the nodes in stack and return it

# TIME COMPLEXITY: O(n)
    # n = no. of nodes
# SPACE COMPLEXITY: O(n)
    # for stack

def removeNodes(head):
    stack = []
    curr = head
    while curr:
        while stack and stack[-1].val < curr.val: # while current val < val at top of stack, keep popping from stack
            stack.pop()
        stack.append(curr) # append current node to stack
        curr = curr.next
    
    # chain up the resulting nodes in stack
    prev = None
    for node in stack:
        if prev:
            prev.next = node
        prev = node
    prev.next = None # last node in resulting LL points to None
    return stack[0]