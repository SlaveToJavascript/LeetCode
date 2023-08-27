# https://leetcode.com/problems/sort-list/description/
# MEDIUM
# Tags: divideconquerlc, mergesortlc, linkedlistlc, #128

# GIVEN:
    # the head of a linked list

# TASK:
    # return the list after sorting it in ascending order

# EXAMPLES:
    # Input: head = [4,2,1,3]
    # Output: [1,2,3,4]

    # Input: head = [-1,5,3,4,0]
    # Output: [-1,0,3,4,5]

    # Input: head = []
    # Output: []

###########################################################################################################

# ✅ ALGORITHM 1: ADD ALL NODES TO ARRAY AND SORT ARRAY BY NODE VAL
# Iterate through the entire LL, and add each node to an array
# Sort the array with custom key lambda x : x.val, in descending order (largest to smallest value)
# Iterate through the sorted array and chain the nodes up together

# TIME COMPLEXITY: O(n log n) 
    # for sorting the array
# SPACE COMPLEXITY: O(n)
    # for the array

def sortList(head):
    nodes = []
    curr = head
    while curr:
        nodes.append(curr) # iterate entire LL and add each node to array
        curr = curr.next
    
    nodes = sorted(nodes, key=lambda x: x.val, reverse=True) # sort array by decreasing node.val
    
    prev = None
    for node in nodes:
        node.next = prev # chain up the nodes in the sorted array
        prev = node
    
    return prev

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: MERGE SORT
# Use fast-slow pointer approach to get the middle node in a LL and divide LL into 2 using middle node as pivot
# For the sorting of left and right LLs part: create a dummy node and whichever is the smaller node, chain that node to the dummy LL

# TIME COMPLEXITY: O(n log n)
    # sortList() takes O(log n) time (keep dividing no. of nodes by 2)
    # merging takes O(log n) time
    # taking 2 sorted LLs and merging them together takes O(n)
    # Overall TC = O(n) * O(log n)
# SPACE COMPLEXITY: O(log n)
    # for the recursion stack in sortList()

def sortList(head):
    if not head or not head.next: # if head.next is null, there's only 1 node in LL -> no sorting needed
        return head
    
    # split list into 2 halves
    left = head
    middle = getMiddleNode(head) # 2
    right = middle.next # 1
    middle.next = None # 2 -> null

    return merge(sortList(left), sortList(right))

def getMiddleNode(head):
    # use fast-slow pointer algorithm to get and return middle node of LL
    fast = head
    slow = ListNode(0, head) # slow starts from 1 step behind so that we can use the middle.next node as the start of the right LL in sortList() above

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    return slow

def merge(left_list, right_list):
    dummy = ListNode(0)
    curr = dummy

    while left_list and right_list:
        if left_list.val <= right_list.val:
            curr.next = left_list
            left_list = left_list.next
        else:
            curr.next = right_list
            right_list = right_list.next
        curr = curr.next
    
    if left_list: # if left_list is longer than right_list, there are still nodes in left_list remaining
        curr.next = left_list # add the remaining nodes to curr LL
    
    if right_list: # if right_list is longer than left_list, there are still nodes in right_list remaining
        curr.next = right_list # add the remaining nodes to curr LL
    
    return dummy.next