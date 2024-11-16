# 369. Plus One Linked List
# https://leetcode.com/problems/plus-one-linked-list/
# MEDIUM
# Tags: linkedlistlc, #369

# GIVEN:
    # a non-negative integer represented as a linked list of digits

# TASK:
    # add one to the number and return the new linked list
    # NOTE: The digits are stored such that the most significant digit is at the head of the list

# EXAMPLES:
    # Input: head = [1,2,3]
    # Output: [1,2,4]

    # Input: head = [0]
    # Output: [1]

###########################################################################################################

# ✅ ALGORITHM: FIND RIGHTMOST NON-9 NODE
# for any 9's at the end of the linked list, we need to change it to 0 and add 1 to the integer before it
# for numbers like 999, we need to change all 9's to 0's and add an additional integer 1 to the start of the linked list
# STEPS:
    # 1. locate rightmost non-9 node
    # 2. add 1 to that rightmost non-9 node
    # 3. change all nodes after the rightmost non-9 node to 0 (all numbers, if any, after the rightmost non-9 node will be 9's)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def plusOne(head):
    dummy = ListNode(0) # initialize a dummy node for the additional 1 in case of numbers like 999 etc.
    dummy.next = head # chain up dummy node to head
    rightmost_non9 = dummy # initialize the rightmost non-9 node as dummy node

    curr = head
    while curr:
        if curr.val != 9:
            rightmost_non9 = curr # update rightmost non-9 node
        curr = curr.next
    
    rightmost_non9.val += 1 # add 1 to the rightmost non-9 node

    curr = rightmost_non9.next # start iterating from the node after the rightmost non-9 node, if any
    while curr:
        curr.val = 0 # change all nodes after the rightmost non-9 node to 0
        curr = curr.next
    
    return dummy if dummy.val else head # if dummy node is not needed, return the original head