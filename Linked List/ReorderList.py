# 143. Reorder List
# https://leetcode.com/problems/reorder-list/description/
# MEDIUM
# Tags: linkedlistlc, twopointerslc, #143

# GIVEN:
    # the head of a singly linked-list
        # The list can be represented as: 
            # L0 → L1 → … → Ln - 1 → Ln

# TASK:
    # Reorder the list to be on the following form: 
        # L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    # NOTE: You may not modify the values in the list's nodes. Only nodes themselves may be changed

# EXAMPLES:
    # Input: head = [1,2,3,4]
    # Output: [1,4,2,3]

    # Input: head = [1,2,3,4,5]
    # Output: [1,5,2,4,3]

###########################################################################################################

# ✅ ALGORITHM: FAST SLOW POINTERS + REVERSE LINKED LIST + MERGE TWO LINKED LISTS
# NOTE: this question is the combination of 3 questions:
    # (1) MiddleOfTheLinkedList.py
    # (2) ReverseLinkedList.py
    # (3) MergeTwoSortedLists.py
# STEPS:
    # 1. Get middle node of LL using fast and slow pointers
        # if there are 2 middle nodes, return 2nd middle node
    # 2. Reverse 2nd part of LL
    # 3. Merge the 2 lists alternately

# TIME COMPLEXITY: O(n)
    # step 1 (find the middle node): O(n)
    # step 2 (reverse the 2nd half of the LL): O(n/2) = O(n)
    # step 3 (merge the 2 lists): O(n)
# SPACE COMPLEXITY: O(1)

def reorderList(head):
    # 1. Get middle node of LL using fast and slow pointers
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # slow is now pointing to the middle node of LL

    # 2. Reverse 2nd part of LL
    prev, curr = None, slow
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    # 3. Merge the 2 lists alternately
    first, second = head, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next