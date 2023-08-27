# https://leetcode.com/problems/rotate-list/
# MEDIUM
# Tags: linkedlistlc, twopointerslc, #61

# GIVEN:
    # head of a linked list

# TASK:
    # rotate the list to the right by k places

# EXAMPLES:
    # Input: head = [1,2,3,4,5], k = 2
    # Output: [4,5,1,2,3]

    # Input: head = [0,1,2], k = 4
    # Output: [2,0,1]

###########################################################################################################

# ✅ ALGORITHM: TWO POINTERS
# Nett no. of rotations = k % len(LL)
# k rotations means we take the last k nodes and move them to the front of the LL

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def rotateRight(head, k):
    if not head: 
        return head
    
    tail = head # tail pointer points to tail of LL
    n = 1 # length of LL

    while tail.next: # iterate the whole LL to get tail tail to point to last node of LL + get length of LL at the same time
        tail = tail.next
        n += 1

    if n == 1 or k == 0: # if length of LL = 1 or no rotations need to be made,
        return head
    
    curr = head
    for _ in range(n-k-1): # we move curr pointer to the node before the node that is to be shifted to the front of LL
        curr = curr.next
    
    # at this point, node points to pivot (e.g. LL = [1,2,3,4,5], k = 2 -> curr points to 3)
    new_head = curr.next # this is the head of the new LL after k rotations
    curr.next = None # curr (node 3) is now the last node of the new LL after k rotations
    tail.next = head # chain the last k nodes of the original LL to the original head

    return new_head