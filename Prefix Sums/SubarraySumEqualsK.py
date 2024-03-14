# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/description/
# MEDIUM
# Tags: prefixlc, hashmaplc, #560

# GIVEN:
    # an integer array, nums
    # an integer, goal

# TASK:
    # return the total number of subarrays whose sum equals to k
    # A subarray is a contiguous non-empty sequence of elements within an array

# EXAMPLES:
    # Input: nums = [1, 1, 1], k = 2
    # Output: 2

    # Input: nums = [1,2,3], k = 3
    # Output: 2

###########################################################################################################

# ✅ ALGORITHM: PREFIX SUMS
# prefix_sum = running sum of elements in array
# NOTE: formula: for any given prefix_sum, no. of valid subarrays summing to k = freq[k] + freq[prefix_sum - k]
# STEPS:
    # Create a hashmap of prefix_sums : frequencies
    # iterate nums array and add element to prefix_sum
    # if prefix_sum = k, add 1 to the result since this is a subarray whose sum = k
    # add freq[prefix_sum - k] to result for every prefix_sum
        # freq[prefix_sum - k] = no. of valid subarrays that do NOT start with 1st element of array, but ending with current element of the iteration
    # lastly, add prefix_sum to hashmap and increase frequency (hashmap value) by 1

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
    # for hashmap

from collections import defaultdict

def numSubarraysWithSumK(nums, k):
    prefix_sum = 0
    freq_hashmap = defaultdict(int)
    result = 0

    for num in nums:
        prefix_sum += num

        if prefix_sum == k:
            result += 1
        
        if prefix_sum - k in freq_hashmap:
            result += freq_hashmap[prefix_sum - k]

        freq_hashmap[prefix_sum] += 1
    
    return result