# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/
# EASY
# Tags: setlc, loop, linkedlistlc, twopointerslc, #141

# Given the head of a linked list, determine if the linked list has a loop in it
# Return True if loop exists, False otherwise

###########################################################################################################

# ✅ ALGORITHM: HASH SET
# Iterate linked list and check if each node exists in a hash set.
# If the node is in hash set, it means a loop exists --> return True
# If the node is not in hash set, add node to hash set
# Return false

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def hasCycle(head):
    hs = set()
    curr = head
    while curr:
        if curr in hs:
            return True
        else:
            hs.add(curr)
        curr = curr.next
    return False

#==========================================================================================================

# ✅✅✅ ALGORITHM: FAST AND SLOW POINTERS, O(1) space
# use 2 pointers, fast and slow
    # fast pointer moves 2 steps at a time, slow pointer moves 1 step at a time
# if there is a loop, fast and slow pointers will eventually meet
# if there is no loop, fast pointer will reach the end of the linked list

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def hasCycle(head):
    fast = slow = head
    
    while fast and fast.next:
        fast = fast.next.next # fast pointer moves 2 steps at a time
        slow = slow.next # slow pointer moves 1 step at a time
        if fast == slow:
            return True
    
    return False