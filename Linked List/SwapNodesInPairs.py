# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
# MEDIUM
# Tags: linkedlistlc, #24

# GIVEN:
    # a linked list

# TASK:
    # swap every two adjacent nodes and return its head
    # You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# EXAMPLES:
    # Input: head = [1,2,3,4]
    # Output: [2,1,4,3]

    # Input: head = []
    # Output: []

    # Input: head = [1]
    # Output: [1]

###########################################################################################################

# ✅✅✅ ALGORITHM 1: ITERATIVE
# at each node (curr):
    # 1. save curr's next node's next node in a variable
    # 2. set prev node's "next" as curr's next node
    # 3. set curr's next node's "next" as curr
    # 4. set curr's "next" as curr's next node's next node (which was saved in a variable in step 1)
    # 5. update prev = curr and curr = curr's next node's next node (which was saved in a variable in step 1)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def swapPairs(head):
    dummy = ListNode(0, head)
    prev = dummy
    curr = head

    while curr and curr.next:
        next_pair = curr.next.next # next_pair is set to the node after the current pair that is swapped

        prev.next = curr.next # Link the previous node to the second node of the pair
        curr.next.next = curr # Perform the swap

        # Move to the next pair
        curr.next = next_pair
        prev = curr # Move prev to the end of the current pair
        curr = next_pair # Move curr to the beginning of the next pair
    
    return dummy.next

#==========================================================================================================

# ✅ ALGORITHM 2: RECURSION
# Start the recursion with head node of the original linked list.
# Every recursion call is responsible for swapping a pair of nodes. Let's represent the two nodes to be swapped by firstNode and secondNode.
# Next recursion is made by calling the function with head of the next pair of nodes. This call would swap the next two nodes and make further recursive calls if there are nodes left in the linked list.
# Once we get the pointer to the remaining swapped list from the recursion call, we can swap the firstNode and secondNode i.e. the nodes in the current recursive call and then return the pointer to the secondNode since it will be the new head after swapping.
# Once all the pairs are swapped in the backtracking step, we would eventually be returning the pointer to the head of the now swapped list. This head will essentially be the second node in the original linked list.

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
    # recursive call stack

def swapPairs(head):
    if not head or not head.next: # If the list has no node or has only one node left
        return head

    # Nodes to be swapped
    first_node = head
    second_node = head.next

    # Swapping
    first_node.next = swapPairs(second_node.next)
    second_node.next = first_node

    # Now the head is the second node
    return second_node