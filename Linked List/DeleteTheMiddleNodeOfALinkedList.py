# Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# MEDIUM
# Tags: linkedlistlc, twopointerslc, leetcode75lc, lc75lc, #2095

# GIVEN:
    # head of a linked list

# TASK:
    # Delete the middle node, and return the head of the modified linked list
        # middle node = node at the (length//2)th index

# EXAMPLES:
    # Input: head = [1,3,4,7,1,2,6]
    # Output: [1,3,4,1,2,6]
    # Explanation:
    # The above figure represents the given linked list. The indices of the nodes are written below.
    # Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
    # We return the new list after removing this node. 

    # Input: head = [1,2,3,4]
    # Output: [1,2,4]
    # Explanation:
    # The above figure represents the given linked list.
    # For n = 4, node 2 with value 3 is the middle node, which is marked in red.

    # Input: head = [2,1]
    # Output: [2]
    # Explanation:
    # The above figure represents the given linked list.
    # For n = 2, node 1 with value 1 is the middle node, which is marked in red.
    # Node 0 with value 2 is the only node remaining after removing node 1.

###########################################################################################################

# ✅ ALGORITHM: TWO POINTERS
# use 2 pointers, fast and slow, both initialized to point at a dummy node
# for every 2 steps the fast pointer takes, the slow pointer takes 1 step
# the node that the slow pointer points to when the fast pointer has no more 2-step movements to make, is the node before the node that is to be deleted

def deleteMiddle(head):
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy # slow and fast pointers

    while fast.next and fast.next.next: # while there are 2-step movements for fast pointer to make,
        fast = fast.next.next # fast pointer takes 2 steps at a time
        slow = slow.next # slow pointer takes 1 step at a time
    
    slow.next = slow.next.next # remove the node after slow pointer node

    return dummy.next