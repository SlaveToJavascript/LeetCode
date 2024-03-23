# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/description/
# EASY
# Tags: linkedlistlc, twopointerslc, #876

# GIVEN:
    # head of a singly linked list

# TASK:
    # return the middle node of the linked list
    # If there are two middle nodes, return the second middle node

# EXAMPLES:
    # Input: head = [1,2,3,4,5]
    # Output: [3,4,5]
    # Explanation: The middle node of the list is node 3.

    # Input: head = [1,2,3,4,5,6]
    # Output: [4,5,6]
    # Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

###########################################################################################################

# ✅ ALGORITHM: TWO POINTERS / FAST AND SLOW POINTERS
# use 2 pointers, fast and slow, where fast moves 2 steps at a time and slow travels 1 step at a time
# both pointers should start from a dummy node
# by the time fast pointer reaches the last node, slow pointer would be pointing to the middle node (for odd-lengthed LL)
    # for even-lengthed LL, slow pointer would be pointing to the 1st middle node
# return the middle node

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def middleNode(head):
    fast = slow = head # initiate both pointers to point at dummy node
    
    while fast and fast.next:
        fast = fast.next.next # fast pointer moves 2 steps at a time
        slow = slow.next # slow pointer moves 1 step at a time
    
    return slow