# 2958. Length of Longest Subarray With at Most K Frequency
# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
# MEDIUM
# Tags: slidingwindowlc, #2958

# GIVEN:
    # an integer array, nums
    # an integer, k

# TASK:
    # return the length of the longest subarray whose frequency of each element is at most k

# EXAMPLES:
    # Input: nums = [1,2,3,1,2,3,1,2], k = 2
    # Output: 6
    # Explanation: The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
    # It can be shown that there are no good subarrays with length more than 6.

    # Input: nums = [1,2,1,2,1,2,1,2], k = 1
    # Output: 2
    # Explanation: The longest possible good subarray is [1,2] since the values 1 and 2 occur at most once in this subarray. Note that the subarray [2,1] is also good.
    # It can be shown that there are no good subarrays with length more than 2.

    # Input: nums = [5,5,5,5,5,5,5], k = 4
    # Output: 4
    # Explanation: The longest possible good subarray is [5,5,5,5] since the value 5 occurs 4 times in this subarray.
    # It can be shown that there are no good subarrays with length more than 4.

###########################################################################################################

# ✅ ALGORITHM: SLIDING WINDOW
# keep a window starting at index l and ending at index r. Both l and r start from 0
# create a hashmap that tracks the frequency of each element in the window
# at every nums[r], add 1 to the frequency of nums[r] in the hashmap and check if this frequency > k
    # if yes, keep shrinking window from the left until the frequency of nums[l] in the hashmap is = k
        # we achieve this by decrementing the frequency of each nums[l] encountered within the window by 1, then shifting l pointer forward
# as long as frequency of nums[r] <= k, update max window length

# TIME COMPLEXITY: O(n)
    # O(n) for the for-loop
    # the while-loop terminates when the frequency of nums[r] > k, and this can happen max. n times in total (1 for each element) -> overall TC = O(2n)
# SPACE COMPLEXITY: O(n)
    # for hashmap

from collections import defaultdict

def maxSubarrayLength(nums, k):
    freq_hashmap = defaultdict(int) # hashmap of each num : frequency in nums array
    max_len = 0 # max. length of a valid window
    
    l = 0 # left boundary of window
    for r in range(len(nums)):
        freq_hashmap[nums[r]] += 1 # increment frequency of nums[r] by 1 in hashmap
        
        while freq_hashmap[nums[r]] > k:
            # shrink window from left until frequency of nums[l] = k
            freq_hashmap[nums[l]] -= 1
            l += 1
        
        max_len = max(max_len, r-l+1) # update max_len with length of window (if necessary)
    
    return max_len