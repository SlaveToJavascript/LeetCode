# 1248. Count Number of Nice Subarrays
# https://leetcode.com/problems/count-number-of-nice-subarrays/
# MEDIUM
# Tags: prefixlc, hashmaplc, twopointerslc, threepointerslc, slidingwindowlc, #1248

# GIVEN:
    # an array of integers, nums
    # an integer, k

# TASK:
    # Return the number of nice sub-arrays
        # A continuous subarray is called nice if there are k odd numbers on it

# EXAMPLES:
    # Input: nums = [1,1,2,1,1], k = 3
    # Output: 2
    # Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

    # Input: nums = [2,4,6], k = 1
    # Output: 0
    # Explanation: There are no odd numbers in the array.

    # Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
    # Output: 16

# *** NOTE: this question is VERY similar to SubarraySumEqualsK.py

###########################################################################################################

# ✅ ALGORITHM 1: PREFIX SUMS
# odd_count = no. of odd elements in current subarray
# THINK: if a subarray starting from the 1st element of nums has an odd_count of k+x, can we chop off x elements(s) from the beginning of the subarray to make its odd_count = k?
# FORMULA: 
    # for any subarray, no. of valid subarrays summing to k = freq_of_(odd_count-k)_in_hashmap + 1 (if odd_count = k)
# STEPS:
    # Create a hashmap of odd_count : frequencies_of_appearance
    # iterate nums array and get odd_count of current subarray
    # if odd_count = k, add 1 to the result since this is a subarray whose odd_count = k
    # add hashmap[odd_count-k] to result (if the key exists in hashmap)
        # hashmap[odd_count - k] = no. of valid subarrays that do NOT start with 1st element of array, but ends with current element of the iteration
    # lastly, add odd_count to hashmap (as key) and increase frequency (hashmap value) by 1

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
    # for hashmap

from collections import defaultdict

def numberOfSubarrays(nums, k):
    hashmap = defaultdict(int)
    odd_count = 0 # count of odd no.s in subarray
    result = 0

    for num in nums:
        if num % 2 != 0: # if num is odd
            odd_count += 1
        
        if odd_count == k:
            result += 1
        
        if odd_count-k in hashmap:
            result += hashmap[odd_count-k]
        
        hashmap[odd_count] += 1

    return result

#==========================================================================================================

# ✅✅ ALGORITHM 2: THREE POINTERS + SLIDING WINDOW
# first use the sliding window algorithm (2 pointers) to get the longest subarray with at most k odd no.s, then use a 3rd pointer, middle, to move from left pointer up till and including the rightmost element within this subarray where odd_count = k
# since the shortest valid subarray within the current subarray is nums[m...r] and the longest valid subarray is nums[l...r], that means each subarray starting from nums[l...m] and ending at nums[r] is a valid subarray -> there are m-l+1 valid subarrays!!!
    # e.g. nums = [2,2,2,1,2,1]
        #          l     m   r  (these are where the pointers should be)
        # no. of valid subarrays ending at nums[r] = m-l+1 = 3-0+1 = 4 ✅

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def numberOfSubarrays(nums, k):
        result = 0
        odd_count = 0

        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 != 0: # odd
                odd_count += 1
            
            # sliding window algorithm:
            while odd_count > k:
                if nums[l] % 2 != 0:
                    odd_count -= 1
                l += 1
            
            # here, odd_count <= k

            m = l # m is the 3rd pointer (middle)
            if odd_count == k:
                # check if there is a smaller valid subarray that ends at r
                while nums[m] % 2 == 0: # even
                    m += 1
                
                # m is between l and r
                result += m-l+1
        
        return result