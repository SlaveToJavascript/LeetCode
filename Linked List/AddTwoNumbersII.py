# https://leetcode.com/problems/add-two-numbers-ii/description/
# MEDIUM

# GIVEN:
    # 2 non-empty linked lists representing 2 non-negative integers

# TASK:
    # Add the two numbers and return the digits of the sum as a linked list

# EXAMPLES:
    # Input: l1 = [7,2,4,3], l2 = [5,6,4]
    # Output: [7,8,0,7]
    # Explanation: 7243 + 564 = 7807

    # Input: l1 = [2,4,3], l2 = [5,6,4]
    # Output: [8,0,7]

    # Input: l1 = [0], l2 = [0]
    # Output: [0]

###########################################################################################################

# ✅ ALGORITHM 1: STACKS
# push all elements of l1 and l2 into 2 stacks
# while stacks are not empty:
    # pop elements from both stacks and add them together
    # if the sum of both elements are 2 digits (i.e. >= 10), keep track of the carry-over 1
    # chain up the new nodes with val = sum of the 2 elements (or last digit of the sum if sum >= 10)
# if there is still a carry-over of 1, create a new node with value = 1 and append to the LL chain

# TIME COMPLEXITY: O(m+n), where m and n are the lengths of l1 and l2
    # Iterating over both the lists and pushing all the values in the respective stacks take O(m+n) time
    # We iterate until both the stacks are empty -> O(max(m, n))
# SPACE COMPLEXITY: O(m+n)
    # The s1 stack takes O(m) space and the s2 stack takes O(n) space

def addTwoNumbers(l1, l2):
    stack1, stack2 = [], []
    # add digits in l1 into stack1 and l2 into stack2
    while l1:
        stack1.append(l1.val)
        l1 = l1.next
    while l2:
        stack2.append(l2.val)
        l2 = l2.next

    carry = 0 # carry-over initialized to 0
    tail = None # tail node initialized to None
    while stack1 or stack2: # while stack1 or stack2 is not empty
        total = carry # add carry-over to the total sum
        if stack1: total += stack1.pop() # if stack1 not empty, add top element of stack1 to sum
        if stack2: total += stack2.pop() # if stack2 not empty, add top element of stack2 to sum
        carry = 1 if total > 9 else 0 # if total > 9 (i.e. 2 digits), carry-over = 1, else = 0
        total %= 10 # if total >= 10, total = 2nd digit of sum, else total = sum
        tail = ListNode(total, tail) # create new node with val = total, chained to tail
        
    if carry: tail = ListNode(carry, tail) # if there is still a carry-over, chain new node with carry-over value to resulting node from previously
    return tail