# 1265. Print Immutable Linked List in Reverse
# https://leetcode.com/problems/print-immutable-linked-list-in-reverse/
# MEDIUM
# Tags: linkedlistlc, #1265

# You are given an immutable linked list, print out all values of each node in reverse with the help of the following interface:
    # ImmutableListNode: An interface of immutable linked list, you are given the head of the list.
# You need to use the following functions to access the linked list (you can't access the ImmutableListNode directly):
    # ImmutableListNode.printValue(): Print value of the current node.
    # ImmutableListNode.getNext(): Return the next node.
# The input is only given to initialize the linked list internally. You must solve this problem without modifying the linked list. In other words, you must operate the linked list using only the mentioned APIs.

# EXAMPLES:
    # Input: head = [1,2,3,4]
    # Output: [4,3,2,1]

    # Input: head = [0,-4,-1,3,-5]
    # Output: [-5,3,-1,-4,0]

    # Input: head = [-2,0,6,4,4,-6]
    # Output: [-6,4,4,6,0,-2]

###########################################################################################################

# ✅ ALGORITHM: RECURSION
# recursively go to the end of the linked list
# print the value of the node at the end of the linked list
# then go back to the previous node and print its value
# continue this process until the head of the linked list is reached

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def printLinkedListInReverse(head):
    if head: # if head is not None
        printLinkedListInReverse(head.getNext())
        head.printValue()
