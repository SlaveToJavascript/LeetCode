# 2485. Find the Pivot Integer
# https://leetcode.com/problems/find-the-pivot-integer/description/
# EASY
# Tags: twopointerslc, prefixlc, #2485

# GIVEN:
    # a positive integer n

# TASK:
    # find the pivot integer x such that the sum of all elements between and including 1 and x = sum of all elements between x and n
    # Return the pivot integer x
    # If no such integer exists, return -1
    # It is guaranteed that there will be at most one pivot index for the given input

# EXAMPLES:
    # Input: n = 8
    # Output: 6
    # Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

    # Input: n = 1
    # Output: 1
    # Explanation: 1 is the pivot integer since: 1 = 1.

    # Input: n = 4
    # Output: -1
    # Explanation: It can be proved that no such integer exist.

###########################################################################################################

# ✅ ALGORITHM: BRUTE FORCE with time complexity = O(n^2)
# Iterate from 1 to n, calculating left and right sums that are both inclusive of the iterated no.
# return i if left sum = right sum

# TIME COMPLEXITY: O(n^2) 👎
# SPACE COMPLEXITY: O(1)

def pivotInteger(n):
    left_sum = 0
    for i in range(1, n+1):
        left_sum += i
        if left_sum == sum(range(i, n+1)):
            return i
    
    return -1

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: MATH
# Since the pivot is duplicated in left sum and right sum, left_sum + right_sum = total_sum + pivot
    # -> right_sum = total_sum + pivot - left_sum
    # if left_sum = total_sum + pivot - left_sum, then pivot is the answer

# TIME COMPLEXITY: O(n) 👍
# SPACE COMPLEXITY: O(1)

def pivotInteger(n):
    total_sum = sum(range(n+1))
    left_sum = 0
    for i in range(1, n+1):
        left_sum += i
        if left_sum == total_sum + i - left_sum:
            return i
    return -1

#==========================================================================================================

# ✅ ALGORITHM 3: TWO POINTERS (not recommended)

# TIME COMPLEXITY: O(n) 👍
# SPACE COMPLEXITY: O(1)

def pivotInteger(n):
    left_value = 1
    right_value = n
    sum_left = left_value
    sum_right = right_value

    if n == 1:
        return n

    # Iterate until the pointers meet
    while left_value < right_value:
        # Adjust sums and pointers based on comparison
        if sum_left < sum_right:
            sum_left += left_value + 1
            left_value += 1
        else:
            sum_right += right_value - 1
            right_value -= 1

        # Check for pivot condition
        if sum_left == sum_right and left_value + 1 == right_value - 1:
            return left_value + 1

    return -1  # Return -1 if no pivot is found