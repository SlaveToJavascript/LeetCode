# 523. Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/description/
# MEDIUM
# Tags: hashmaplc, prefixlc, #523

# GIVEN:
    # an integer array, nums
    # an integer, k

# TASK:
    # return true if nums has a good subarray or false otherwise
    # good subarray:
        # length >= 2
        # sum of the elements of the subarray is a multiple of k
            # NOTE: 0 is always a multiple of k

# EXAMPLES:
    # Input: nums = [23,2,4,6,7], k = 6
    # Output: true
    # Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

    # Input: nums = [23,2,6,4,7], k = 6
    # Output: true
    # Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
    # 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

    # Input: nums = [23,2,6,4,7], k = 13
    # Output: false

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# Get every single subarray from nums and check if their sums % k == 0

# TIME COMPLEXITY: O(n^2)

#==========================================================================================================

# ✅ ALGORITHM 2: HASHMAP
    # https://youtu.be/OKcrLfR-8mE?t=390&si=w6UI6v2YeWzGZnpN
# Starting from nums[0], get the sum of each subarray from nums[0]...nums[i] and divide that by k
# Store the remainder of that into a hashmap with the value as the ending index of the subarray
# If we continue moving i forward and encounter another subarray with the same remainder, 
    # it means for the new elements in array (added after the first time that remainder appeared),
    # their sums is divisible by k

# e.g. for nums = [23,2,4,6,7], k = 6
# nums[0] = 23, 23 % 6 = 5 --> hashmap = {5: 0} (since the subarray ends at index 0)
# nums[1] = 2, (23+2) % 6 = 1 --> hashmap = {5: 0, 1: 1} (since the subarray ends at index 1)
# nums[2] = 4, (23+2+4) % 6 = 5 (5 again! 5 already exists as a key in the hashmap)
    # since 5 is already in hashmap with ending index 0 -> we can conclude nums[1] + nums[2] % 6 = 0
    # return True since 2-0 > 2 (minimum length of a good subarray)
# *** NOTE: why do we need the line "hm = {0: -1}"?
    # we are stating that a subarray starting from the 1st element of the array can be considered
    # without this line, we would miss subarrays that start from the beginning of the array

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def checkSubarraySum(nums, k):
    if len(nums) < 2:
        return False # since length of good subarray >= 2
    
    hm = {0: -1} # initialize hashmap with this since 0 is always a multiple of k
    
    total_sum = 0 # total sum of subarray until nums[i]
    for idx, num in enumerate(nums):
        total_sum += num # total sum of subarray until nums[idx]
        rem = total_sum % k
        if rem in hm: # that means we found a subarray that is divisible by k
            if idx-hm[rem] >= 2: # size of good subarray must be at least 2
                return True
        else: 
            hm[rem] = idx # add {remainder:closing_index} key-value pair to hm
    
    return False