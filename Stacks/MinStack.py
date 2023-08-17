# https://leetcode.com/problems/min-stack/description/
# MEDIUM
# Tags: stacklc, #155

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time
# Implement the MinStack class:
    # MinStack() initializes the stack object.
    # push(int val) pushes the element val onto the stack.
    # pop() removes the element on the top of the stack.
    # top() gets the top element of the stack.
    # getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function

# EXAMPLES:
    # Input
    # ["MinStack","push","push","push","getMin","pop","top","getMin"]
    # [[],[-2],[0],[-3],[],[],[],[]]

    # Output
    # [null,null,null,null,-3,null,0,-2]

    # Explanation
    # MinStack minStack = new MinStack();
    # minStack.push(-2);
    # minStack.push(0);
    # minStack.push(-3);
    # minStack.getMin(); // return -3
    # minStack.pop();
    # minStack.top();    // return 0
    # minStack.getMin(); // return -2

###########################################################################################################

# ✅ ALGORITHM: TWO STACKS
# Since we need to be able to pop from top of the stack but also be able to retrive the min element in stack both in O(1) time, we should maintain 2 stacks: 1 regular stack and another min stack
    # the min stack will track the min value in the stack up till that index
    # e.g.
        # stack   min_stack
        #  -3        -3
        #   0        -2
        #  -2        -2
    # when only -2 is in stack, the minimum in the stack is -2
    # when 0 is added to stack, the minimum in stack is still -2
    # when -3 is added to stack, then minimum in stack is -3 => update min_stack
# NOTE: simply using a min_stack_value variable is insufficient as we might be popping from stack -> what if the element popped is the minimum of the current stack? We need to find the next minimum of the stack after popped element is removed
# When we pop from stack, we also pop from min_stack -> top of the min_stack will still be the minimum of the stack after popping

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        min_val = val
        if self.min_stack:
            min_val = min(val, self.min_stack[-1]) # set min_val to the minimum between val and current minimum in the stack
        self.min_stack.append(min_val) # now, top of min_stack will always be minimum of current stack

    def pop(self):
        self.stack.pop()
        self.min_stack.pop() # When we pop from stack, we also pop from min_stack -> top of the min_stack will still be the minimum of the stack after popping

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]