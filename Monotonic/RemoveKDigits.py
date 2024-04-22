# https://leetcode.com/problems/remove-k-digits/description/
# MEDIUM
# Tags: monotoniclc, monotonicstacklc, stacklc, 

# GIVEN:
    # string, num, representing a non-negative integer
    # an integer, k

# TASK:
    # return the smallest possible integer after removing k digits from num

# EXAMPLES:
    # Input: num = "1432219", k = 3
    # Output: "1219"
    # Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

    # Input: num = "10200", k = 1
    # Output: "200"
    # Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

    # Input: num = "10", k = 2
    # Output: "0"
    # Explanation: Remove all the digits from the number and it is left with nothing which is 0.

###########################################################################################################

# ✅ ALGORITHM: INCREASING MONOTONIC STACK
# Greedy rules to achieve the smallest possible number (in order of priority):
    # 1) Prioritize removing the largest digits first
    # 2) Prioritize removing the digits in front first
        # e.g. s = "9119", k = 1 -> which 9 to remove?
            # remove the 1st 9 -> 119
            # remove the 2nd 9 -> 911
            # therefore we should prioritize digits on the left
# Create an increasing monotonic stack
    # while iterating through num, if the no. at top of stack > current digit, we pop the greater no. from stack
        # this reduces the number of large digits at the front of the resulting string
# We can only pop k times
# After the iterating and popping, if remaining k is still > 0, we remove the last remaining k digits from the end of the string
    # e.g. if num = "12345", there will not be any numbers popped at first because original num is already increasing
    # this means all the larger no.s are at the back -> we remove k digits from the back

# TIME COMPLEXITY: O(n)
    # n = len(num)
    # worst case: we iterate through the entire string and pop all the digits
# SPACE COMPLEXITY: O(n)
    # worst case: we push all the digits into the stack

def removeKdigits(num, k):
    stack = []

    for i in num: # iterate num string
        while stack and int(stack[-1]) > int(i) and k > 0: # while num @ top of stack > current num,
            stack.pop()
            k -= 1
        stack.append(i)
    
    while stack and k > 0: # if k > 0 after the above while loop
        stack.pop() # remove the last k digits from num
        k -= 1
    
    result = ''.join(stack)

    return str(int(result)) if result else "0" # edge case: if result is empty string, return "0" instead