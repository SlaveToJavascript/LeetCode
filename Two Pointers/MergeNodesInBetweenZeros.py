# 2181. Merge Nodes in Between Zeros
# https://leetcode.com/problems/merge-nodes-in-between-zeros/
# MEDIUM
# Tags: linkedlistlc, twopointerslc, #2181

# GIVEN:
    # head of a linked list, which contains a series of integers separated by 0's
    # The beginning and end of the linked list will have Node.val == 0

# TASK:
    # For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
    # Return the head of the modified linked list.

# EXAMPLES:
    # Input: head = [0,3,1,0,4,5,2,0]
    # Output: [4,11]
    # Explanation: 
    # The above figure represents the given linked list. The modified list contains
    # - The sum of the nodes marked in green: 3 + 1 = 4.
    # - The sum of the nodes marked in red: 4 + 5 + 2 = 11.

    # Input: head = [0,1,0,3,0,2,2,0]
    # Output: [1,3,4]
    # Explanation: 
    # The above figure represents the given linked list. The modified list contains
    # - The sum of the nodes marked in green: 1 = 1.
    # - The sum of the nodes marked in red: 3 = 3.
    # - The sum of the nodes marked in yellow: 2 + 2 = 4.

###########################################################################################################

# ✅ ALGORITHM 1: CREATE A NEW LINKED LIST OF MERGED NODES
# iterate through the linked list, and sum up node values of nodes where node.val != 0
# create a 2nd linked list which is to be eventually returned; every time we reach a node with value = 0, we create a new node and attach the new node to the 2nd linked list
# return the 2nd linked list

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
    # for the 2nd linked list

def mergeNodes(head):
    dummy = dummy_curr = ListNode(0) # dummy is the 2nd linked list (which is to be returned)
    curr = head.next

    while curr:
        curr_sum = 0
        while curr.val != 0: # keep iterating until the next 0-value node is found
            curr_sum += curr.val
            curr = curr.next
        
        # at this point, curr would be pointing to the "closing" 0-value node

        dummy_curr.next = ListNode(curr_sum) # create a new node for the 2nd linked list (which is to be returned) with value = the sum of the merged nodes
        dummy_curr = dummy_curr.next
        curr = curr.next # curr moves to the next node after the "closing" 0-value node
    
    return dummy.next

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: TWO POINTERS
# iterate through the linked list, and sum up node values of nodes where node.val != 0
# once we reach a node with value = 0 (i.e. the "closing" 0-value node), modify the value of the node after the "opening" 0-value node to become the summed up value of the nodes in between
# then link this node to the node after the "closing" 0-value node

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
    # no extra space is needed as we modify the linked list in-place

def mergeNodes(head):
    curr1 = curr2 = head.next # start iterating the linked list from its 2nd node (a non-0-value node)

    while curr1:
        curr_sum = 0
        while curr2.val != 0: # keep iterating until the next 0-value node is found
            curr_sum += curr2.val
            curr2 = curr2.next
        
        curr1.val = curr_sum # modify the value of the node after the "opening" 0-value node to become the summed up value of the nodes in between
        curr1.next = curr2.next # link the node after the "opening" 0-value node to the node after the "closing" 0-value node
        curr1 = curr2 = curr2.next # start the next iteration with the node after the "closing" 0-value node
    
    return head.next

#==========================================================================================================

# ✅ ALGORITHM 3: RECURSION
# Store the first non-zero value, given by head->next, in head.
# If head is null, return head.
# Initialize a dummy node temp with head.
# Initialize sum with 0.
# Iterate through the list until the value of temp is not 0:
# Increment sum with the value of temp.
# Set temp as temp->next.
# Store the updated sum in the value of head.
# Store head->next as the solution of the sub-problem starting at temp, given by mergeNodes(temp).
# Return head.

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
    # for the recursion call stack

def mergeNodes(head):
    head = head.next # we start from the 1st non-zero node after the "opening" 0-value node
    if not head:
        return 

    temp = head # temp variable is used for traversing non-zero nodes to sum up their values and merge them
    merged_sum = 0
    while temp.val != 0:
        merged_sum += temp.val
        temp = temp.next
    head.val = merged_sum # modify value of 1st non-zero node after the "opening" zero-node to become merged_sum

    head.next = mergeNodes(temp) # set merged node's next node to be the next 0-value node
    return head