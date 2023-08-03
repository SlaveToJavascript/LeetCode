# https://leetcode.com/problems/linked-list-cycle/description/
# EASY
# Tags: setlc, #141

# Given the head of a linked list, determine if the linked list has a loop in it
# Return True if loop exists, False otherwise

###########################################################################################################

# ✅ ALGORITHM:
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