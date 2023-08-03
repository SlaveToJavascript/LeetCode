# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
# MEDIUM
# Tags: stacklc, twopointerslc, linkedlistlc, #2130

# GIVEN:
    # head, the head of a linked list with even length

# TASK:
    # return the maximum twin sum of the linked list
    # twin sum = sums of the values of 1st and last node, 2nd and 2nd last node, 3rd and 3rd last node, etc.

# EXAMPLES:
    # Input: head = [5,4,2,1]
    # Output: 6
    # Explanation:
    # Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
    # There are no other nodes with twins in the linked list.
    # Thus, the maximum twin sum of the linked list is 6. 

    # Input: head = [4,2,2,3]
    # Output: 7
    # Explanation:
    # The nodes with twins present in this linked list are:
    # - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
    # - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
    # Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 

    # Input: head = [1,100000]
    # Output: 100001
    # Explanation:
    # There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

###########################################################################################################

# ✅✅✅ ALGORITHM 1: LIST OF VALUES
# Traverse through the linked list and store the values in a list
# then get the twin sums using 2 pointers and obtain the maximum

# TIME COMPLEXITY: O(n)
    # Iterating the linked list and pushing all the node values in arrays takes O(n) time
    # iterate over the first half of the linked list to find the max twin sum, which also takes O(n) time
# SPACE COMPLEXITY: O(n)
    # the values array takes O(n) space as we push n elements into it

def getMaximumTwinSum(head):
    curr = head
    vals = [] # list to collect values of linked lists in sequence
    while curr:
        vals.append(curr.val)
        curr = curr.next
    
    # two pointers approach to match each node with its tune and get the max sum
    l, r = 0, len(vals)-1 # left and right pointers
    max_sum = 0
    while l<r:
        max_sum = max(max_sum, vals[l] + vals[r])
        l += 1
        r -= 1
    
    return max_sum

#==========================================================================================================

# ✅ ALGORITHM 2: STACK
# use a stack to get the values of the second half of the nodes in reverse order
    # iterate over the linked list, pushing all of the node values into the stack
# To compute twin sums, iterate from beginning to end of linked list
# then get the values of the nodes from the end using the stack
# get the 1st half nodes using LL next pointers and pop from top of  stack to get the 2nd half nodes

# TIME COMPLEXITY: O(n)
    # Iterating over linked list and pushing all node values into stack takes O(n) time
    # iterating over 1st half of the linked list to find the max twin sum also takes O(n) time
# SPACE COMPLEXITY: O(n)
    # the stack takes O(n) space as we push n elements into it

def getMaximumTwinSum(head):
    current = head
    stack = []
    max_sum = 0

    # iterate LL and push all node vals into stack
    while current:
        stack.append(current.val)
        current = current.next

    # iterate over 1st half of LL while popping from end of stack to find max twin sum
    current = head
    size = len(stack)
    count = 1
    max_sum = 0
    while count <= size/2:
        max_sum = max(max_sum, current.val + stack.pop())
        current = current.next
        count = count + 1

    return max_sum

#==========================================================================================================

# ✅ ALGORITHM 3: TWO POINTERS TO REVERSE 2ND HALF IN PLACE
# Flip the 2nd half of the LL so the last elem points to the 2nd last elem, which points to 3rd last elem, and so on
# to reverse 2nd half of LL, first obtain the list's middle node using slow and fast pointers
    # fast pointer moves at 2x faster speed than slow pointer so that when fast reaches the end, slow would point to the middle node
# then we reverse the 2nd half of LL
    # first do nextNode = slow.next so we can still reach the next node after modifying slow.next
    # Then set slow.next = prev
    # To set up the variables for next iteration, we set prev = slow and slow = nextNode
        # We continue doing so until slow is not null
# Once we've reversed the 2nd half of the list, prev will point to the 1st elem of this reversed list
# So we use head to iterate over the original list because the first half is unaffected, and prev to iterate over the reversed list
# We add the corresponding node values, update the maximum twin sum with the current twin if possible, and then proceed to the next node in both lists

# TIME COMPLEXITY: O(n)
    # takes O(n) time to iterate over LL to find middle node and then reverse the 2nd half of LL
# SPACE COMPLEXITY: O(1)
    # since we're only reversing LL in-place and iterating, constant space is needed

def pairSum(head):
    slow, fast = head, head
    maximumSum = 0

    # Get middle node of the linked list using slow pointer
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Reverse second half of the linked list, which starts from slow
    curr, prev = slow, None
    while curr:       
        curr.next, prev, curr = prev, curr, curr.next
    
    # get twin sums by iterating 1st half and 2nd half at the same time
    start = head
    while prev:
        maximumSum = max(maximumSum, start.val + prev.val)
        prev = prev.next
        start = start.next

    return maximumSum