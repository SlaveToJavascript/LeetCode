# https://leetcode.com/problems/merge-k-sorted-lists/description/
# HARD
# Tags: mergesortlc, linkedlistlc, heaplc, minheaplc, #23

# GIVEN:
    # an array of k linked-lists, lists, where each linked-list is sorted in ascending order

# TASK:
    # Merge all the linked-lists into one sorted linked-list and return it

# EXAMPLES:
    # Input: lists = [[1,4,5],[1,3,4],[2,6]]
    # Output: [1,1,2,3,4,4,5,6]
    # Explanation: The linked-lists are:
    # [
    # 1->4->5,
    # 1->3->4,
    # 2->6
    # ]
    # merging them into one sorted list:
    # 1->1->2->3->4->4->5->6

    # Input: lists = []
    # Output: []

    # Input: lists = [[]]
    # Output: []

###########################################################################################################

# ✅ ALGORITHM 1: MERGE SORT
# Split lists array into 2 halves, and pass each half through the same function recursively
# At each recursion, if length of either half of array = 0, return null node for that half
    # else if length of either half of array = 1, return the 1 LL in that half
# pass the return value (i.e. the returned LL or null) for each half into merge()
# merge(l1, l2) merges 2 sorted LLs and returns the sorted combined LL
# The resulting LL returned from merge() function is the final merged sorted LL

# TIME COMPLEXITY: O(n log k)
    # k = no. of linked lists
    # n = no. of nodes in each linked list
    # merge(l1, l2) takes O(n1 + n2) time ≈ O(n)
    # mergeKLists(lists) splits the lists array (with k linked lists) recursively and calls merge() for each half -> total no. of halving operations ≈ log k
    # Since merge() is called for each half, total TC = O(n) * O(log k)
# SPACE COMPLEXITY: O(log k) for the recursion stack

def mergeKLists(lists):
    def merge(l1, l2): # merge 2 sorted lists
        curr1, curr2 = l1, l2 # pointers for current node in each LL
        
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

        if curr1: # if only l1's nodes are left
            curr.next = curr1
        
        if curr2: # if only l2's nodes are left
            curr.next = curr2
        
        return dummy.next
    
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    
    # split array of LLs into half
    mid = len(lists) // 2
    left = lists[:mid]
    right = lists[mid:]

    return merge(mergeKLists(left), mergeKLists(right))

#==========================================================================================================

# ✅ ALGORITHM 2: MIN HEAP
# Create a min-heap and push the val of 1st node (i.e. head node) of each LL into the min-heap together with its index i
    # any minHeap[j] = (lists[i].val, i), i.e. the value of the current node of any lists[i] and the index of the LL within lists array
# Create dummy node to build the merged LL
# Merge lists using min-heap:
# While heap is not empty,
    # pop the smallest node val from heap, and get the index i of that LL (with the smallest node val) within lists array
    # attach the popped node (at lists[i]) to the merged LL (headed by the dummy node)
    # shift merged LL pointer to its next node
    # shift lists[i] pointer to its next node
    # if this next node of lists[i] is not null, push it to heap

# TIME COMPLEXITY: O(N log k)
    # k = no. of linked lists
    # N = total no. of nodes in all linked lists combined
# SPACE COMPLEXITY: O(N) for the resulting linked list which has N nodes

from heapq import *

def mergeKLists(lists):
    heap = [] # min-heap

    # push the val of 1st node (i.e. head node) of each LL into min-heap together with its index i
    for i in range(len(lists)):
        if lists[i]: # if head node in linked list at index i is valid
            heappush(heap, (lists[i].val, i))
    
    dummy = ListNode(0) # this is the head node of merged LL to return
    curr = dummy # pointer for the current node of merged LL

    while heap: # while heap is not empty,
        min_val, i = heappop(heap) # pop node with smallest val from heap
        curr.next = lists[i] # point merged LL's next node to the node that was popped
        curr = curr.next # move pointer of current node of merged LL forward
        lists[i] = lists[i].next # move pointer of popped node's LL forward
        if lists[i]: # if the next node in popped node's LL is valid,
            heappush(heap, (lists[i].val, i)) # push it to heap
    
    return dummy.next # return the merged LL