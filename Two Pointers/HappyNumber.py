# https://leetcode.com/problems/happy-number/description/
# EASY
# Tags: twopointerslc, #202

# GIVEN:
    # a number, n

# TASK:
    # return true if n is a happy number, false otherwise
    # A happy number is a number defined by the following:
        # Starting with any positive integer, replace the number by the sum of the squares of its digits.
        # Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
        # Those numbers for which this process ends in 1 are happy
        # Return true if n is a happy number, and false if not.

# EXAMPLES:
    # Input: n = 19
    # Output: true
    # Explanation:
    # 12 + 92 = 82
    # 82 + 22 = 68
    # 62 + 82 = 100
    # 12 + 02 + 02 = 1

    # Input: n = 2
    # Output: false

###########################################################################################################

# ✅ ALGORITHM 1: TWO POINTERS (FAST AND SLOW POINTER)
# Define helper function that takes in an integer and returns the sum of squares of its digits
# Initialize slow = n, fast = helper(n)
# while fast != 1 and slow != fast:
    # slow = helper(slow)
    # fast = helper(helper(fast))
    # NOTE: if the sum of squares of digits of n eventually = 1, fast would eventually be = 1
    # if there is an infinite cycle, fast would eventually be = slow
# return fast == 1

# TIME COMPLEXITY: O(log n), where n = input no.
    # worst case: non-happy no.
    # Since we are calculating the sum of all digits in a number, TC of this function = O(log n), because the no. of digits in the no. n = log_10 n
# SPACE COMPLEXITY: O(1)

def isHappy(n):
    def getNext(n): # takes in an integer and returns the sum of squares of its digits
        result = 0
        for num in str(n):
            res += int(num)**2
        return result
    
    # initialize fast and slow pointers
    slow = n
    fast = getNext(n)

    while fast != 1 and slow != fast:
        slow = getNext(slow)
        fast = getNext(getNext(fast))
    
    return fast == 1 # if fast = 1, it's a happy no.; else it means slow = fast -> unhappy no.