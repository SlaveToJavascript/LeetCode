# https://leetcode.com/problems/split-linked-list-in-parts/description/
# MEDIUM
# Tags: linkedlistlc, #725

# GIVEN:
    # the head of a singly linked list
    # an integer k

# TASK:
    # split the linked list into k consecutive linked list parts

# EXAMPLES:
    # Input: head = [1,2,3], k = 5
    # Output: [[1],[2],[3],[],[]]
    # Explanation:
    # The first element output[0] has output[0].val = 1, output[0].next = null.
    # The last element output[4] is null, but its string representation as a ListNode is [].

    # Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
    # Output: [[1,2,3,4],[5,6,7],[8,9,10]]
    # Explanation:
    # The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

###########################################################################################################

# ✅ ALGORITHM: 

# TIME COMPLEXITY: O(max(n,k))
    # n = length of LL
    # k might be greater than n, therefore TC might be O(k) if k > n
# SPACE COMPLEXITY: O(k)

def splitListToParts(head, k):
    # get length of LL
    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next
    
    sub_len = length // k # the min. length of each split part
    extra = length % k # the remainder after splitting LL into k equal parts of sub_len each
    result = [] # return value
    curr = head
    
    for _ in range(k):
        result.append(curr) # even if curr is null, we can still add it to result array

        for _ in range(sub_len - 1): # -1 because we need n-1 moves to get to the nth node
                                        # e.g. 1->2->3: we need 2 moves to get from node 1 to node 3
            curr = curr.next
        if extra:
            curr = curr.next # include 1 additional node if there are extra nodes
            extra -= 1 # decrease the no. of extra nodes by 1

        if curr:
            next = curr.next
            curr.next = None # curr should be last node of current split part -> set its next node to null
            curr = next # curr now points to the head of the next split part
    
    return result