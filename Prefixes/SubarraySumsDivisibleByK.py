# 974. Subarray Sums Divisible by K
# https://leetcode.com/problems/subarray-sums-divisible-by-k
# MEDIUM
# Tags: prefixlc, hashmaplc, #974

# GIVEN:
    # an integer array, nums
    # an integer k

# TASK:
    # return the number of non-empty subarrays that have a sum divisible by k
        # A subarray is a contiguous part of an array

# EXAMPLES:
    # Input: nums = [4,5,0,-2,-3,1], k = 5
    # Output: 7
    # Explanation: There are 7 subarrays with a sum divisible by k = 5:
    # [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

    # Input: nums = [5], k = 9
    # Output: 0

###########################################################################################################

# ✅ ALGORITHM: PREFIX SUMS & COUNTING
    # https://www.youtube.com/watch?v=10wbS3uk2F8&t=280s
# PRINCIPLE: if num1 % k = x and num2 % k = x (i.e. if 2 no.s divided by k gets the same remainder), the difference between nums1 and nums2 is a multiple of k
# use a prefix_sum variable which is the running sum of each element of nums array as we iterate the array
# use a hashmap where key = remainder, value = no. of times this remainder has been encountered
# when iterating nums, at each element, check if prefix_sum % k is in hashmap (i.e. if the remainder of prefix_sum/k has already been encountered before)
    # at an index i, if prefix_sum % k = remainder exists in hashmap, it means there are subarrays ending at index i that are divisible by k; the count of such subarrays = no. of times this remainder has been encountered before (WHY??? because when 2 elements have the same remainder after dividing by k, e.g. [nums1, ..., nums2] where nums1 and nums2 have the same % k value, it means nums2 - nums1 = a multiple of k -> [element_after_nums1, ..., nums2] is a valid array
        # add the remainder's hashmap value to result
        # increment the remainder's hashmap value by 1
    # if remainder doesn't exist in hashmap, add it to hashmap with a value of 1
# NOTE: make sure to add { 0 : 1 } to the hashmap first so that valid subarrays beginning from the 1st element can also be counted
    # e.g. if the subarray sum is k, and we don't have { 0 : 1 } in the hashmap (and k % k = 0), then this valid subarray cannot be counted into result

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(k)
    # the remainder of a division is always between 0 and k-1 -> worst case: there are k different remainders

def subarraysDivByK(nums, k):
    result = 0 # return value (i.e. no. of valid subarrays in nums)
    hashmap = { 0 : 1 } # remainder : frequency of encountering this remainder
        # add { 0 : 1 } to the hashmap first so that valid subarrays beginning from the 1st element can also be counted
    prefix_sum = 0 # running sum of elements in nums array as we iterate array

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k
        if remainder in hashmap: # this remainder has been encountered before -> there are valid subarrays ending at the current num
            result += hashmap[remainder]
            hashmap[remainder] += 1
        else:
            hashmap[remainder] = 1
    
    return result