# https://leetcode.com/problems/reverse-linked-list-ii/description/
# MEDIUM
# Tags: linkedlistlc, #92

# GIVEN:
    # the head of a singly linked list
    # 2 integers, left and right, where left <= right

# TASK:
    # reverse the nodes of the list from position left to position right, and return the reversed list

# EXAMPLES:
    # Input: head = [1,2,3,4,5], left = 2, right = 4
    # Output: [1,4,3,2,5]

    # Input: head = [5], left = 1, right = 1
    # Output: [5]

###########################################################################################################

# ✅ ALGORITHM: IN-PLACE REVERSAL

# TIME COMPLEXITY: O(n)
    # visit each node once
# SPACE COMPLEXITY: O(1)

def reverseBetween(head, left, right):
    if left == right: return head # if left = right, there are no reversals done

    dummy = ListNode(-1, head) # use dummy node in case the whole LL needs to be reversed
    curr = dummy
    before_left = dummy # the node before the node at "left" position
        # before_left will point to the head of the reversed LL in the resulting LL
    position = 0 # track which position we're at; dummy node not counted so position = 0

    while curr and position != left: # iterate LL until node at left position is found
        before_left = curr # set node before left position node to current
        curr = curr.next
        position += 1

    # when we reach this point, curr is the node at position left
    left_head = curr
    next = curr.next
    curr.next = None # initiate curr as the last node of the reversed LL
    prev = curr 
    curr = next 
    position += 1

    while curr and position != right: # iterate rest of the LL until node at right position is found
        # at the same time, we reverse this portion of the linked list as it is between left and right positions
        next = curr.next 
        curr.next = prev 
        prev = curr 
        curr = next 
        position += 1

    # when we reach this point, curr is the node at position right
    after_right = curr.next # after_right is the node after the node at position right
    curr.next = prev # reverse the last node in the original LL to point to its previous node

    before_left.next = curr # for the node before node at position left, set its next node to current node (curr node is the node at position right)
    left_head.next = after_right # for the node at position left (whose next node was pointing to None), set its next node to the node after the node at position right

    return dummy.next