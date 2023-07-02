# https://leetcode.com/problems/reverse-linked-list/description/
# EASY

# GIVEN:
    # head of a linked list, 

# TASK:
    # reverse the linked list and return head of the reversed list

# EXAMPLES:
    # Input: head = [1,2,3,4,5]
    # Output: [5,4,3,2,1]

    # Input: head = [1,2]
    # Output: [2,1]

    # Input: head = []
    # Output: []

###########################################################################################################

# ✅✅✅ ALGORITHM 1: ITERATIVE (TWO POINTERS)
# Maintain 2 pointers: prev and curr

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def reverseList(head):
    curr = head
    prev = None

    while curr:
        nx = curr.next
        curr.next = prev
        prev = curr
        curr = nx
    
    return prev # since curr is now None and prev is the start of the REVERSED linked list

#==========================================================================================================

# ✅ ALGORITHM 2: RECURSIVE
# Break down problem into subproblems: reverse last node, then 2 last nodes, then 3 last nodes, etc.

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def reverseList(head):
    if not head: return None

    new_head = head
    if head.next: # if there is still a subproblem (i.e. head.next is not null)
        new_head = reverseList(head.next)
        head.next.next = head # by now, head.next has been reversed. This is reversing the link between next node and head
    head.next = None # if head is the first node in list, we are setting its next pointer to null

    return new_head