# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
# MEDIUM
# Tags: linkedlistlc, twopointerslc, #82

# GIVEN:
    # the head of a sorted linked list

# TASK: 
    # delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list
    # Return the linked list sorted as well

# EXAMPLES:
    # Input: head = [1,2,3,3,4,4,5]
    # Output: [1,2,5]

    # Input: head = [1,1,1,2,3]
    # Output: [2,3]

###########################################################################################################

# ✅ ALGORITHM: TWO POINTERS
# have a prev and curr pointer -> curr pointer checks if the current node and next node have the same values, while prev pointer points to the node before the curr pointer
# if curr node's val = curr's next node's val, a while loop will run until a node with a different value is encountered -> prev's next pointer will point to that node with the different value

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def deleteDuplicates(head):
    dummy = ListNode("x", head) # dummy node is needed in case 1st node in LL is a repeated node that has to be deleted
    curr = head
    prev = dummy
    repeated_val = 0 # when nodes with repeating values are encountered, repeated_val tracks the val of these nodes

    while curr:
        if curr.next and curr.next.val == curr.val: # if curr's next node's val is the same as curr's val,
            repeated_val = curr.val # track the val of the nodes with repeated vals
            curr = curr.next # go to the next node
            
            while curr and curr.val == repeated_val: # while loop runs until a node with a different value is reached
                curr = curr.next

            # at this point, curr is a node with a different val from repeated_val
            prev.next = curr # prev's next pointer will point to that node with the different value
        
        else:
            prev = curr # keep updating prev node as the tail of the LL to be returned
            curr = curr.next
    
    return dummy.next