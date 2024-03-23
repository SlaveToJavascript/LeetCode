# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# EASY
# Tags: linkedlistlc, twopointerslc, #21

# GIVEN:
    # the heads of two sorted linked lists, list1 and list2

# TASK:
    # merge the two lists into one sorted list and return it

# EXAMPLES:
    # Input: list1 = [1,2,4], list2 = [1,3,4]
    # Output: [1,1,2,3,4,4]

    # Input: list1 = [], list2 = []
    # Output: []

    # Input: list1 = [], list2 = [0]
    # Output: [0]

###########################################################################################################

# ✅ ALGORITHM: TWO POINTERS

# TIME COMPLEXITY: O(n1 + n2)
    #  n1 and n2 = lengths of list1 and list2 respectively
# SPACE COMPLEXITY: O(n1 + n2)
    # for the merged LL

def mergeTwoLists(list1, list2):
    curr1, curr2 = list1, list2 # pointers for current node in each list

    dummy = ListNode(0) # dummy node to chain our merged sorted LL to
    curr = dummy

    while curr1 and curr2:
        if curr1.val <= curr2.val:
            curr.next = curr1
            curr1 = curr1.next
        else:
            curr.next = curr2
            curr2 = curr2.next
        curr = curr.next
    
    curr.next = curr1 if curr1 else curr2 # append the remaining nodes of the non-empty list to the merged LL
    
    return dummy.next