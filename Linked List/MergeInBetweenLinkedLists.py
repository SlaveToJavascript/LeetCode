# 1669. Merge In Between Linked Lists
# https://leetcode.com/problems/merge-in-between-linked-lists/description/
# MEDIUM
# Tags: linkedlistlc, #1669

# GIVEN:
    # 2 linked lists, list1 and list2
    # 2 integers, a and b

# TASK:
    # Remove list1's nodes from the ath node to the bth node, and put list2 in their place
    # Build the result list and return its head

# EXAMPLES:
    # Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
    # Output: [10,1,13,1000000,1000001,1000002,5]
    # Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

    # Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
    # Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
    # Explanation: The blue edges and nodes in the above figure indicate the result.

###########################################################################################################

# ✅ ALGORITHM 1A: LINKED LIST TWICE TRAVERSED (my solution – attempted 20/03/2024)

# TIME COMPLEXITY: O(n+m)
    # n and m = length of list1 and list2
# SPACE COMPLEXITY: O(1)

def mergeInBetween(list1, a, b, list2):
    curr1 = dummy = ListNode(0, list1)
    index = 0
    
    while curr1:
        curr1 = curr1.next
        index += 1
        if index == a:
            before_a = curr1 # before_a is the node before the a'th node (the node that splits from a'th node)
        elif index == a+2+(b-a): # a+2+(b-a): "+2" because a'th node from dummy is the node before a'th node, so +1 to get to a'th node, +1 again to get to node after b'th node
            after_b = curr1 # after_b is the node after the b'th node (the node that gets reattached to list2's tail)

    curr = before_a
    curr.next = list2 # attach list2's head to the node before the a'th node
    while curr and curr.next: # having "curr.next" in condition ensures that curr stops at tail of list2, instead of pointing at None
        curr = curr.next
    
    # now, curr points to tail of list2
    curr.next = after_b # attach tail of list node to node after the b'th node
    return dummy.next

#==========================================================================================================

# ✅ ALGORITHM 1B: LINKED LIST TWICE TRAVERSED (less verbose)

# TIME COMPLEXITY: O(n+m)
    # n and m = length of list1 and list2
# SPACE COMPLEXITY: O(1)

def mergeInBetween(list1, a, b, list2):
    curr = list1
    for _ in range(a-1): # -1 because we want the node before the a'th node
        curr = curr.next

    # now, curr points to the node before the a'th node
    l1 = curr
    for _ in range(b-a+2): # +2 because we want the node AFTER the b'th node (+1), and we want to include the b'th node itself (+1 again)
        curr = curr.next

    # now, curr points to the node after the b'th node
    l2 = curr
    l1.next = list2 # attach list2's head to the node before the a'th node
    curr = list2 # curr points to list2's head

    while curr.next: # having "curr.next" as condition ensures that curr stops at tail of list2, instead of pointing at None
        curr = curr.next # move curr to the tail (last node) of list2
    
    curr.next = l2 # attach tail of list2 to node after the b'th node
    return list1