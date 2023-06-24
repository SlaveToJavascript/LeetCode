# https://leetcode.com/problems/delete-node-in-a-linked-list/description/

# GIVEN:
    # node, a node to be deleted from the linked list
    # the head of this linked list is not given

# TASK:
    # "delete" the node from the linked list and connect the node before this node to the node after this node
    # definition of "delete":
        # value of the node to be deleted should not exist in the linked list
        # no. of nodes in linked list should decrease by 1
        # all nodes before node to be deleted should be in the same order
        # all nodes after node to be deleted should be in the same order

# EXAMPLES:
    # Input: head = [4,5,1,9], node = 5
    # Output: [4,1,9]
    # Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

    # Input: head = [4,5,1,9], node = 1
    # Output: [4,5,9]
    # Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

###########################################################################################################

# ALGORITHM: MODIFY NODE TO BE DELETED, THEN DELETE THE NODE AFTER NODE TO BE DELETED INSTEAD
# i.e. copy over the value of the node after the node to be deleted, then delete that node (that was copied from) instead

def deleteNode(node):
    node.val = node.next.val # change value of node to be deleted to value of the next node
    node.next = node.next.next # change next pointer of node to be deleted (after changing) to the 2nd node after it