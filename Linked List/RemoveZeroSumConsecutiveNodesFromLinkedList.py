# 1171. Remove Zero Sum Consecutive Nodes from Linked List
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
# MEDIUM
# Tags: linkedlistlc, hashmaplc, prefixlc, #1171

# GIVEN:
    # head of a linked list

# TASK:
    # repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences
    # return the head of the final linked list
        # You may return any such answer

# EXAMPLES:
    # Input: head = [1,2,-3,3,1]
    # Output: [3,1]
    # Note: The answer [1,2,1] would also be accepted.

    # Input: head = [1,2,3,-3,4]
    # Output: [1,2,4]

    # Input: head = [1,2,3,-3,-2]
    # Output: [1]

###########################################################################################################

# ✅ ALGORITHM: PREFIX SUMS HASHMAP
# if you keep a hashmap of the running (prefix) sum at each node mapped to the respective current node, and then encounter a prefix sum at a later node that is already in the hashmap, it means the nodes between those 2 respective nodes (specifically, from the node after the 1st node up to and including the 2nd node) add up to 0
    # we need to remove the nodes after the 1st node up to and including the 2nd node
# so we can do a 2nd traversal through the LL to set the 1st node's .next pointer to the 2nd node's next node -> this removes the nodes in between

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def removeZeroSumSublists(head):
    dummy = ListNode(0, head) # use dummy node to simplify edge cases, e.g. when 1st node in LL forms a zero-sum sequence
    prefix_sum = 0 # running sum of all nodes
    prefixes = { 0 : dummy } # key : value = prefix_sum : node

    # FIRST TRAVERSAL: traverse LL and add respective prefix sum : node mappings to hashmap
    curr = head
    while curr:
        prefix_sum += curr.val # add current node's value to running sum
        prefixes[prefix_sum] = curr # add current sum and current node to prefixes hashmap
        curr = curr.next
    
    # SECOND TRAVERSAL: uses prefixes hashmap to identify nodes that form a zero-sum sequence and remove them
    curr = dummy # reinitialize curr pointer to start of LL
    prefix_sum = 0 # reset prefix sum to 0
    while curr:
        prefix_sum += curr.val # add current node's value to running sum
        curr.next = prefixes[prefix_sum].next
            # remove the nodes AFTER the 1st node up to and including the 2nd node
            # can achieve this by setting the 1st node's .next pointer to the 2nd node's next node
        curr = curr.next
    
    return dummy.next