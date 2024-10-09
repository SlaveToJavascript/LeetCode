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

# *** NOTE: this question is VERY similar to CountNumberOfNiceSubarrays.py

###########################################################################################################

# ✅ ALGORITHM: PREFIX SUMS
    # https://youtu.be/fFVZt-6sgyo?si=dPf2TPMiG6riFeR6&t=304
# prefix_sum = running sum of elements in array
# THINK: if a subarray starting from the 1st element of nums has a sum of k+x, can we chop off a "x" element (or a few elements summing up to x) from the beginning of the subarray to make it a k-sum subarray?
# FORMULA: 
    # for any prefix_sum, no. of valid subarrays summing to k = freq_of_(prefix_sum-k)_in_hashmap + 1 (if prefix_sum = k)
# STEPS:
    # Create a hashmap of prefix_sums : frequencies_of_appearance
    # iterate nums array and get prefix_sum up till and including current element
    # if prefix_sum = k, add 1 to the result (since this is a subarray whose sum = k)
    # add hashmap[prefix_sum-k] to result (if the key exists in hashmap)
        # hashmap[prefix_sum-k] = no. of valid subarrays that do NOT start with 1st element of array, but ends with current element of the iteration
    # lastly, add prefix_sum to hashmap (as key) and increase frequency (hashmap value) by 1

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
        
        result += freq_hashmap[prefix_sum - k]

        freq_hashmap[prefix_sum] += 1
    
    return result