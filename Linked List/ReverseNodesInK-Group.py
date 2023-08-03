# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
# HARD
# Tags: linkedlistlc, #25

# GIVEN:
    # head of a linked list, head
    # positive integer, k, which is less than or equal to the length of the linked list

# TASK:
    # reverse the nodes of the list k at a time from head, and return modified list

# EXAMPLES:
    # Input: head = [1,2,3,4,5], k = 2
    # Output: [2,1,4,3,5]

    # Input: head = [1,2,3,4,5], k = 3
    # Output: [3,2,1,4,5]

###########################################################################################################

# ✅ ALGORITHM 1
# Create helper function getKthNode(curr, k) that returns the kth node from curr
# Create dummy node at the start of head so that k jumps from dummy node will land on the kth node in original LL
    # e.g. dummy -> 1 -> 2, k = 2
    # 2 jumps from dummy -> 1 and 1 -> 2 gives us the kth (2nd) node in original LL (1 -> 2)
# Use variables groupPrev to keep track of the node before current group, and groupNext to keep track of the node after current group
# Reverse the current k-group starting from groupPrev.next and ending with kthNode

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def reverseKGroup(head, k):
    # getKthNode(curr, k) returns the kth node from curr
    # e.g. for 1 -> 2 -> 3 and k = 2, the 2nd node from node 1 is 3 => return node 3
    def getKthNode(curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
    dummy = ListNode(0, head) # dummy node at the head to eliminate edge cases
    groupPrev = dummy # groupPrev is the node before a k-group
        # e.g. x -> 1 -> 2; k =2 and we need to reverse nodes 1 and 2; x is the groupPrev here

    while True:
        kthNode = getKthNode(groupPrev, k) # we use groupPrev as curr since groupPrev is not part of our k-group
        if not kthNode: # if kthNode is null, it means we are dealing with the last group of our LL and this group is not even big enough for us to reverse it
            # e.g. dummy -> 1 -> 2 -> null and k = 3 -> kth node from dummy is null node as the remaining group size is 2 (i.e. [1 -> 2])
            break
        groupNext = kthNode.next # similar to groupPrev which is the node before our group, groupNext contains the node after our group

        # REVERSE THE K-GROUP
        prev, curr = groupNext, groupPrev.next # groupPrev.next will be the first node in our group to reverse; after reversing this group, we want the last node in the reversed group to point to groupNext, since it is the node after our group
        
        # Reverse current k-group
        while curr != groupNext: # while current is still within the k-group
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        temp = groupPrev.next # need to use a temp variable to store groupPrev.next since value of groupPrev.next will be replaced by kthNode in the next line
        groupPrev.next = kthNode # kth node was the last node in our unreversed group; now we want it to be the first node in our reversed group
        groupPrev = temp # update groupPrev; groupPrev is now the last node in our reversed group, which used to be the 1st node in the group before the reversal
    
    return dummy.next # or return curr

'''
[dummy, 1, 2, 3, 4, 5]
k = 2
groupPrev = dummy
groupNext = 3
After 1st reversal -> [dummy, 2, 1, 3, 4, 5]
'''