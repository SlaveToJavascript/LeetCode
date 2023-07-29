# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# MEDIUM
# Tags: twopointerslc, #19

# GIVEN:
    # head of a linked list

# TASK:
    # remove the nth node from the right

# EXAMPLES:
    # Input: head = [1,2,3,4,5], n = 2
    # Output: [1,2,3,5]

    # Input: head = [1], n = 1
    # Output: []

    # Input: head = [1,2], n = 1
    # Output: [1]

###########################################################################################################

# ✅ ALGORITHM 1: TWO POINTERS
# 1st, create a dummy node in front of head
    # so that if length of LL = 1, i.e. head = [1], we can still iterate from dummy -> 1
# create Right pointer starting from dummy
# Right pointer moves n steps to the right
# Left pointer starts from dummy node
# while Right pointer is not at the last node, continue shifting L and R pointers forward
    # Stop at R = last node
    # When R @ last node, L would be pointing to the node before node to be deleted
# L.next = L.next.next

# TIME COMPLEXITY: O(n)
    # O(n) for iterating LL with n nodes
# SPACE COMPLEXITY: O(1)
    # we use constant space to store two pointers

def removeNthFromEnd(head, n):
    dummy = ListNode(-1)
    dummy.next = head
    right = dummy
    for _ in range(n):
        right = right.next # shift R pointer to the right by n spaces
    left = dummy
    while right.next: # R pointer iterates LL until it is at the last node
        right = right.next
        left = left.next
    left.next = left.next.next
    return dummy.next