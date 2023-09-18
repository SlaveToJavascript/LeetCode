# https://leetcode.com/problems/add-two-numbers/description/
# MEDIUM
# Tags: linkedlistlc, #2

# GIVEN:
    # 2 linked lists, l1 and l2, representing 2 integers
    # digits in linked lists are stored in reverse order,
    # e.g. 2->4->3 represents integer 342

# TASK:
    # Add the 2 integers and return the sum as a linked list in reverse order
    # e.g. l1 = 2->4->3 (342), l2 = 5->6->4 (465); 342 + 465 = 807; return 7->0->8

# EXAMPLES:
    # Input: l1 = [2,4,3], l2 = [5,6,4]
    # Output: [7,0,8]
    # Explanation: 342 + 465 = 807

    # Input: l1 = [0], l2 = [0]
    # Output: [0]

    # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    # Output: [8,9,9,9,0,0,0,1]

###########################################################################################################

# ✅ ALGORITHM:
# Compare this question similar to doing elementary school calculations, i.e. summing up from the back
# e.g. for 3342 + 485 = 807, first 2+5=7, then 4+8=12 (2 carry over 1), then 3+4+1(carry-over)=8, then 3+0=3
# -> result = 3827
# while summing up each of these pairs, create a corresponding node for the value and chain them tgt

# TIME COMPLEXITY: O(max(m, n))
    # m = len(l1)
    # n = len(l2)
    # the algorithm iterates at most max(m, n)
# SPACE COMPLEXITY: O(1)
    # the length of the new list is at most max(m, n) + 1, but we don't count the answer as part of the space complexity

def addTwoNumbers(l1, l2):
    carry_over = 0
    dummy = ListNode(-1) # start of the new LL to be returned
    curr = dummy

    while l1 or l2 or carry_over:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        
        total = v1 + v2 + carry_over
        carry_over = 0 # reset carry_over after using it
        if total >= 10:
            carry_over = 1
            total %= 10
        
        node = ListNode(total) # create new node for the sum of current pair
        curr.next = node # chain the summed nodes together
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next