# 930. Binary Subarrays With Sum
# https://leetcode.com/problems/binary-subarrays-with-sum/description/
# MEDIUM
# Tags: hashmaplc, slidingwindowlc, prefixlc, #930

# GIVEN:
    # a binary array, nums
    # an integer, goal

# TASK:
    # return the number of non-empty subarrays with sum = goal
    # A subarray is a contiguous part of the array

# EXAMPLES:
    # Input: nums = [1,0,1,0,1], goal = 2
    # Output: 4
    # Explanation: The 4 subarrays are bolded and underlined below:
    # [1,0,1,0,1]
    # [1,0,1,0,1]
    # [1,0,1,0,1]
    # [1,0,1,0,1]

    # Input: nums = [0,0,0,0,0], goal = 0
    # Output: 15

###########################################################################################################

# ✅✅✅ ALGORITHM 1: PREFIX SUMS
# prefix_sum = running sum of elements in array
# NOTE: formula: for any given prefix_sum, no. of valid subarrays summing to goal = freq[goal] + freq[prefix_sum - goal]
# STEPS:
    # Create a hashmap of prefix_sums : frequencies
    # iterate nums array and add element to prefix_sum
    # if prefix_sum = goal, add 1 to the result since this is a subarray whose sum = 0
    # add freq[prefix_sum - goal] to result for every prefix_sum
        # freq[prefix_sum - goal] = no. of valid subarrays that do NOT start with 1st element of array, but ending with current element of the iteration
    # lastly, add prefix_sum to hashmap and increase frequency (hashmap value) by 1

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

from collections import defaultdict

def numSubarraysWithSum(nums, goal):
    prefix_sum = 0
    freq_hashmap = defaultdict(int)
    result = 0

    for num in nums:
        prefix_sum += num

        if prefix_sum == goal:
            result += 1
        
        if prefix_sum - goal in freq_hashmap:
            result += freq_hashmap[prefix_sum - goal]

        freq_hashmap[prefix_sum] += 1
    
    return result

#==========================================================================================================

# ✅ ALGORITHM 2: SLIDING WINDOW with O(1) space
# NOTE: leading 0's in a window don't affect the sum, but they increase the no. of valid subarrays
# track the no. of 0's at the l pointer of the current window
    # each continuous sequence of 0's at the start of the window can be additionally added to the total no. of valid subarrays
    # ********** i.e. result += 1 + no. of prefix 0's
# remaining logic: iterate through array using l and r pointers, indicating start and end of current window
# if sum of current window > goal, adjust window by shifting l pointer until sum <= goal
# also need to update prefix 0's count accordingly with the current window
    # if l pointer is 0, prefix zeros count +1
    # else, if l pointer is 1, reset prefix zero count to 0
# e.g. nums = [0,0,1,1], goal = 2
    # we count [1,1] as a valid window -> result +1
    # for every leading 0, a new combination can be formed, e.g. [0,1,1] and [0,0,1,1] -> result +2
    # -> result = 1 + 2 = 3

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1) ✅

def numSubarraysWithSum(nums, goal):
    l = 0 # left pointer, i.e. start of window
    prefix_sum = 0 # running sum of array elements
    prefix_zeros = 0 # no. of leading 0's in current window
    result = 0 # return value, i.e. no. of valid subarrays summing to goal

    for r in range(len(nums)): # r is the right pointer, i.e. end of window
        prefix_sum += nums[r]

        while l < r and (prefix_sum > goal or nums[l] == 0): # shrink window from left if prefix sum > goal OR 1st element of window is 0
            if nums[l] == 1:
                prefix_zeros = 0 # if 1st element of window is 1, reset prefix_zeros to 0
            else: # if 1st element of window is 0,
                prefix_zeros += 1
            
            prefix_sum -= nums[l] # this shrinks the window from the left and reduces the window sum by the 1st element of window
            l += 1 # shifts left pointer by 1
        
        if prefix_sum == goal: # when we found a valid subarray,
            result += 1 + prefix_zeros # the formula to get the no. of valid subarrays: 1 + no. of leading 0's in current window
    
    return result