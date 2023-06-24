# https://leetcode.com/problems/odd-even-linked-list/description/

# GIVEN:
    # head of linked list, 

# TASK:
    # group all nodes with odd indexes together, followed by nodes with even indexes
    # the first node is odd, and the second node is even, and so on
    # solve the problem in O(1) extra space complexity and O(n) time complexity

# EXAMPLES:
    # Input: head = [1,2,3,4,5]
    # Output: [1,3,5,2,4]

    # Input: head = [2,1,3,5,6,4,7]
    # Output: [2,3,6,7,1,5,4]

###########################################################################################################

# ALGORITHM: 
# return None if head is None
# Assign 1st node as head of odd list, assign 2nd node as head of even list
# while even head is not null and even head's next node is not null:
    # assign odd node's next pointer to even node's next node, then move odd to odd.next node
    # assign even node's next pointer to new odd node's next node, then move even to even.next node
    # (stopping condition is even != null and even.next != null bc either even or even.next would be the last element in linked list)
# chain odd list to even list and return it

def oddEvenList(head):
    if head == None: return head
    curr_odd = head
    curr_even = even_head = head.next # we initiate an extra var, even_head, to chain odd and even lists at the last step
    while curr_even and curr_even.next: # this is the stopping condition bc either even or even.next would be the last element in linked list
        curr_odd.next = curr_even.next # point odd node's next pointer to even node's next pointer
        curr_odd = curr_odd.next # move odd pointer to new odd node
        curr_even.next = curr_odd.next
        curr_even = curr_even.next
    curr_odd.next = even_head # chain tail of odd list (curr_odd) to head of even list
    return head