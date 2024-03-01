# https://leetcode.com/problems/maximum-odd-binary-number/
# EASY
# Tags: bitlc, binarylc, bitmanipulationlc, quicksortlc, #2864

# GIVEN:
    # binary string s that contains at least one '1'

# TASK:
    # rearrange the bits such that the resulting binary number is the max. odd binary number that can be created from this combi

# EXAMPLES:
    # Input: s = "010"
    # Output: "001"
    # Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".

    # Input: s = "0101"
    # Output: "1001"
    # Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".

###########################################################################################################

# ✅ ALGORITHM 1: ADD ALL 1's TO THE FRONT
# FIRSTLY, to make odd number, the last bit must be 1
    # bc 2 to the power of any number is always even, except 2^1 = 1
    # when the last bit is 1, 1 × 2^1 = 1, so the number is odd
# SECONDLY, to make the GREATEST POSSIBLE binary number, the remaining 1's must all be in the front
# STEPS:
    # 1. add all the 1's in string s to the front of resulting string, but leave one 1 for the last bit in resulting string
    # 2. add all the 0's in string s behind the 1's in resulting string
    # 3. add the last one remaining 1 in string s to the end of resulting string

# TIME COMPLEXITY: O(n)
    # n = len(s)
# SPACE COMPLEXITY: O(n)

def maximumOddBinaryNumber(s):
    ones_count = s.count("1") # no. of 1's in string s
    return (ones_count-1) * "1" + (len(s)-ones_count) * "0" + "1"

#==========================================================================================================

# ✅✅ ALGORITHM 2: QUICK SORT / PARTITIONING (https://www.youtube.com/watch?v=EUKLOAv4-IQ&t=276s)
# existing sorting algorithms are NOT suitable as they are O(n log n)
# 2 pointers, left_pointer and right_pointer, iterating from left to right
    # left_pointer stays at the same index until there is a swap to be done, then it moves right by 1
    # right_pointer keeps moving right and compares itself with left_pointer to see if need to swap
### if right_pointer is 1:
    # swap them
    # left_pointer += 1
    # right_pointer += 1
### else:
    # right_pointer += 1

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def maximumOddBinaryNumber(s):
    left_pointer = 0
    s = list(s)

    for right_pointer in range(len(s)):
        if s[right_pointer] == "1":
            s[right_pointer], s[left_pointer] = s[left_pointer], s[right_pointer] # swap
            left_pointer += 1
        # in either case, right_pointer will += 1

    s[right_pointer], s[left_pointer-1] = s[left_pointer-1], s[right_pointer]
    return ''.join(s)