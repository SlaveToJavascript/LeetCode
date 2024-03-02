# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/
# MEDIUM
# Tags: twopointerslc, #1679

# GIVEN:
    # an integer array, nums
    # an integer, k

# TASK:
    # pick two numbers from the array whose sum = k and remove them from the array
    # Return the maximum number of operations you can perform on the array

# EXAMPLES:
    # Input: nums = [1,2,3,4], k = 5
    # Output: 2
    # Explanation: Starting with nums = [1,2,3,4]:
    # - Remove numbers 1 and 4, then nums = [2,3]
    # - Remove numbers 2 and 3, then nums = []
    # There are no more pairs that sum up to 5, hence a total of 2 operations.

    # Input: nums = [3,1,3,4,3], k = 6
    # Output: 1
    # Explanation: Starting with nums = [3,1,3,4,3]:
    # - Remove the first two 3's, then nums = [1,4,3]
    # There are no more pairs that sum up to 6, hence a total of 1 operation.

###########################################################################################################

# ✅ ALGORITHM 1: TWO POINTERS
# sort nums array
# initiate left pointer at the start of nums array; initiate right pointer at the end of nums array
# check if the 2 nums add up to k
    # IF YES: increment result counter by 1, shift both pointers by 1
    # IF NO:
        # if sum < k, shift left pointer to the right (since nums array is sorted, this increases the sum)
        # if sum > k, shift right pointer to the left (since nums array is sorted, this decreases the sum)
# return result counter

# TIME COMPLEXITY: O(n log n)
    # for sorting
# SPACE COMPLEXITY: O(n)
    # sorting takes O(n) space

def maxOperations(nums, k):
    nums.sort()
    result = 0
    l, r = 0, len(nums)-1
    while l < r:
        if nums[l] + nums[r] == k:
            result += 1
            l += 1
            r -= 1
        elif nums[l] + nums[r] < k:
            l += 1
        else:
            r -= 1
    
    return result

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: HASHMAP with O(n) time complexity
# create hashmap with the no. of occurrences of each num in nums
# for each num in nums, check if k-num (target) exists in hashmap

from collections import Counter

def maxOperations(nums, k):
    hm = Counter(nums)
    result = 0
    for num in nums:
        target = k-num
        if hm[target] > 0 and hm[num] > 0: # if both num and target exists in hm,
            if num == target and hm[num] < 2:  # if num == target, ensure there are at least 2 occurrences
                continue # if < 2 occurrences, this is not a pair and cannot be removed -> skip to next num
            result += 1
            hm[target] -= 1
            hm[num] -= 1 # remove current pair of num and target
    return result