# https://leetcode.com/problems/longest-consecutive-sequence/description/
# MEDIUM

# GIVEN:
    # unsorted array of integers, nums

# TASK:
    # return the length of the longest consecutive elements sequence
    # NOTE: algo must be in O(n) time max

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# Starting from each num in the nums array
# try to build a consecutive sequence and check if it is the longest
# do this by checking if num + 1 is present or not
    # if present, then check if num + 2 is present or not and so on

# TIME COMPLEXITY = O(n^3)
    # outer for loop runs n times
    # inner while loop can run up to n times for the worst case
        # i.e. if the entire array forms consecutive sequence
    # and finding curr_num + 1 in nums has complexity 0(n)
# SPACE COMPLEXITY = O(1)

def longestConsecutive(nums):
    max_len = 0
    for num in nums:
        curr_num = num
        curr_len = 1
        while curr_num + 1 in nums:
            curr_num += 1
            curr_len += 1
        max_len = max(max_len, curr_len)
    return max_len

#==========================================================================================================

# ❌ ALGORITHM 2: OPTIMIZED BRUTE FORCE + HASHSET
# check if curr_num + 1 is present in the array in O(n) time
# We can optimize this lookup to O(1) using a HashSet
# This solution is the exact same as above, except that a hashset (num_set) is used instead of array nums

# TIME COMPLEXITY = O(n^2)
    # We reduced the lookup to O(1) and everything else remains the same
# SPACE COMPLEXITY = O(1)

def longestConsecutive(nums):
    max_len = 0
    num_set = set(nums)
    for num in nums:
        curr_num = num
        curr_len = 1
        while curr_num + 1 in num_set:
            curr_num += 1
            curr_len += 1
        max_len = max(max_len, curr_len)
    return max_len

#==========================================================================================================

# ✅ ALGORITHM 3: SUPER OPTIMIZED BRUTE FORCE + HASHSET
# In the above 2 solutions, we are still performing redundant operations
    # because we are still checking for consecutive sequences of numbers that are not start of sequence
    # e.g. if current num = 2 and 1 exists in the array, we are still getting the sequence from 2, when the sequence supposedly start at 1. This is unnecessary.
# avoid this by checking if num - 1 exists in the array. Only if it does (i.e. current num is the true start of the sequence, then we check for consecutive numbers)

# TIME COMPLEXITY = O(n)
    # TC is not O(n^2) since while loop only executes when num is the start of a sequence
    # and will run up to n times for the worst case
        # e.g. nums = [3, 5, 1, 2, 7, 6]
        # while loop will only execute when num = 1 or 5, which will run till 3 and 7 respectively
# SPACE COMPLEXITY = O(1)

def longestConsecutive(nums):
    max_len = 0
    num_set = set(nums)
    for num in nums:
        if num - 1 not in num_set: # this is the line that optimizes solution
        # it stops curr_num from looking for consecutive numbers if curr_num is not start of sequence
            curr_num = num
            curr_len = 1
            while curr_num + 1 in num_set:
                curr_num += 1
                curr_len += 1
            max_len = max(max_len, curr_len)
    return max_len