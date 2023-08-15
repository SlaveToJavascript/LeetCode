# https://leetcode.com/problems/partition-list/description/
# MEDIUM
# Tags: linkedlistlc, #86

# GIVEN:
    # the head of a linked list
    # a value x

# TASK:
    # partition the linked list such that all nodes less than x come before nodes greater than or equal to x
    # preserve the original relative order of the nodes in each of the two partitions

# EXAMPLES:
    # Input: head = [1,4,3,2,5,2], x = 3
    # Output: [1,2,2,4,3,5]

    # Input: head = [2,1], x = 2
    # Output: [1,2]

###########################################################################################################

# ✅ ALGORITHM: TWO LINKED LISTS – BIGGER AND SMALLER
# MAIN IDEA: maintain 2 linked lists starting with dummy nodes: 1 is for nodes smaller than x and 1 is for nodes greater than/equals to x
# Iterate through original linked list; when node val < x, smaller linked list's next pointer points to current node; when node val >= x, bigger linked list's next pointer points to current node
# After finish iterating through original linked list, connect the 2 linked lists together and return the smaller linked list

# TIME COMPLEXITY: O(n)
    # iterate through original linked list once
# SPACE COMPLEXITY: O(1)

def partition(head, x):
    curr = head # curr pointer will iterate through original LL

    # smaller linked list that will take nodes smaller than x in the original LL
    smaller_dummy = ListNode(0)
    curr_smaller = smaller_dummy # curr_smaller pointer will move along the smaller LL's nodes

    # bigger linked list that will take nodes greater than/equals to x in the original LL
    bigger_dummy = ListNode(0)
    curr_bigger = bigger_dummy # curr_bigger pointer will move along the bigger LL'nodes

    while curr: # iterate original LL
        if curr.val < x:
            curr_smaller.next = curr # add curr node to smaller LL
            curr_smaller = curr_smaller.next # move curr_smaller pointer forward
        else:
            curr_bigger.next = curr # add curr node to bigger LL
            curr_bigger = curr_bigger.next # move curr_bigger pointer forward
        curr = curr.next # move curr pointer forward
    
    curr_bigger.next = None # end bigger LL with None
    curr_smaller.next = bigger_dummy.next # connect tail of smaller LL to bigger LL
    return smaller_dummy.next # return combined LL that starts with smaller LL