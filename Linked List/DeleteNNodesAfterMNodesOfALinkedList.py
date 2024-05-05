# 1474. Delete N Nodes After M Nodes of a Linked List
# https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/
# MEDIUM
# Tags: linkedlistlc, premiumlc, #1474

# GIVEN:
    # the head of a linked list
    # two integers, m and n

# TASK:
    # Traverse the linked list and remove some nodes in the following way:
        # 1. Start with the head as the current node.
        # 2. Keep the first m nodes starting with the current node.
        # 3. Remove the next n nodes
        # 4. Keep repeating steps 2 and 3 until you reach the end of the list.
    # Return the head of the modified list after removing the mentioned nodes.

# EXAMPLES:
    # Input: head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
    # Output: [1,2,6,7,11,12]
    # Explanation: Keep the first (m = 2) nodes starting from the head of the linked List  (1 ->2) show in black nodes.
    # Delete the next (n = 3) nodes (3 -> 4 -> 5) show in read nodes.
    # Continue with the same procedure until reaching the tail of the Linked List.
    # Head of the linked list after removing nodes is returned.

    # Input: head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3
    # Output: [1,5,9]
    # Explanation: Head of linked list after removing nodes is returned.

###########################################################################################################

# ✅ ALGORITHM: DOUBLE WHILE-LOOPS
# when counting the m nodes to be kept, keep track of a "tail" node before the curr = curr.next line in every iteration so that "tail" points to the last node to be joined with the remaining chain after the next n nodes are removed
# iterate through the next n nodes
# finally, chain the remaining chain with the tail node

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def deleteNodes(head, m, n):
    curr = head
    tail = None

    while curr:
        m_count, n_count = 0, 0

        while curr and m_count < m:
            tail = curr # keep track of tail node before curr = curr.next line, so that tail points to the last node to be joined with the remaining chain after the next n nodes are removed
            curr = curr.next
            m_count += 1

        while curr and n_count < n:
            curr = curr.next
            n_count += 1

        tail.next = curr # chain the remaining chain with the tail node

    return head