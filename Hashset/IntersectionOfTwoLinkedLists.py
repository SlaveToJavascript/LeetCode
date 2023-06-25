# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect
# If the two linked lists have no intersection at all, return None

###########################################################################################################

# ✅ ALGORITHM 1: HASH SET
# Iterate 1st linked list and add all nodes to a hash set
# Iterate 2nd linked list, checking whether any nodes are in hash set
    # If node is in hash set, return node
    # else, go to next node in 2nd linked list
# return None (no intersection)

# TIME COMPLEXITY = O(m+n) where m is no. of nodes in list1, n is no. of nodes in list2
# SPACE COMPLEXITY = O(m) where m is no. of nodes in list1

def getIntersectionNode(self, headA, headB):
    hs = set()

    currA = headA
    while currA:
        hs.add(currA)
        currA = currA.next

    currB = headB
    while currB:
        if currB in hs:
            return currB
        else:
            currB = currB.next

    return None

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: Least complicated solution
# Start from heads of linked list 1 and 2 and iterate both simultaneously
# If reach the end of a linked list, continue from the head of the other linked list
    # i.e. if reach end of list1, go to head2 and iterate again;
    # if reach end of list2, go to head1 and iterate again
# Basically, make the two pointers pass the same distance in total, then they will certainly meet
# The meeting is either on a node or at the end (null)

# TIME COMPLEXITY = O(m+n) where m is no. of nodes in list1, n is no. of nodes in list2

def getIntersectionNode(headA, headB):
    currA, currB = headA, headB

    while currA != currB:
        currA = currA.next if currA else headB
        currB = currB.next if currB else headA
        
    return currA