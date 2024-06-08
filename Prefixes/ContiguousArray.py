# 525. Contiguous Array
# https://leetcode.com/problems/contiguous-array/description/
# MEDIUM
# Tags: prefixlc, hashmaplc, #525

# GIVEN:
    # a binary array, nums

# TASK:
    # return the maximum length of a contiguous subarray with an equal number of 0's and 1's

# EXAMPLES:
    # Input: nums = [0,1]
    # Output: 2
    # Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

    # Input: nums = [0,1,0]
    # Output: 2
    # Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# NOTE: sliding window is not feasible for this because:
    # for the example [1,1,1,0,0,0]:
        # when our window = [1,1,1,0,0], we still have achieved 0 valid contiguous subarrays (since no. of 1's and 0's are not the same)
        # BUT there are already 2 valid subarrays in [1,1,1,0,0], which are [1,0] and [1,1,0,0]
        # how do we know when we need to move left pointer forward to shrink the window from the left?

###########################################################################################################

# ✅ ALGORITHM: PREFIX SUMS
    # https://www.youtube.com/watch?v=agB1LyObUNE
# main idea: since our goal is to equalize no. of 1's and 0's,
    # create a hashmap, diff_index
    # it stores the 1st index at which every unique balance value of 0's and 1's is encountered, where i is every index in nums
        # NOTE: balance value = diff(no. of 1's up until nums[i] - no. of 0's up until nums[i])
        # i.e. for any index i in nums, diff_index = { diff(no. of 1's up until nums[i] - no. of 0's up until nums[i]) : i }
            # i should be the smallest index where this diff value occurs -> i.e. it shouldn't be replaced once it's in the hashmap
                # by always referring back to the 1st occurrence of a balance value when the same balance value is encountered again, you ensure you are considering the longest possible valid subarray with an equal number of 1's and 0's
                    # this is bc any subarray (with balance value = x) starting AFTER the 1st occurrence of balance value x is definitely shorter than the subarray that starts at the 1st occurrence
    # if ones==zeros (at index i), this is definitely the largest subarray up until index i, since this subarray starts from the beginning of nums
    # else, if ones != zeros, check diff_index hashmap to get the index of the previous occurrence of ones-zeros, and update max length if necessary

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
    # for hashmap

def findMaxLength(nums):
    zeros, ones = 0, 0 # zeros = no. of 0's ; ones = no. of 1's
    max_length = 0 # return value, i.e. max. length of a contiguous subarray with an equal number of 0's and 1's
    diff_index = {} # balance value : index
        # balance value = diff between no. of 1's - no. of 0's
    
    for i, num in enumerate(nums):
        # update zeros and ones
        if num == 0:
            zeros += 1
        else: # if num = 1,
            ones += 1
        
        if ones-zeros not in diff_index:
            diff_index[ones-zeros] = i # if a new balance value is encountered, add it to hashmap with current index
        
        if ones == zeros: # this is what we're looking for (same no. of 0's and 1's)
            max_length = ones + zeros # result can be ones+zeros bc this is definitely the longest subarray we've seen at this point bc it starts at the beginning of the array
        elif ones-zeros in diff_index: # technically, we can replace this with "else", since we already added ones-zeros to diff_index in the above code ("if ones-zeros not in diff_index:")
            max_length = max(max_length, i - diff_index[ones-zeros])
            # if ones-zeros in index, we can find the last index that it occurred at and subtract it from i -> we get size of window
                # i.e. i - last index where ones-zeros occurred at = size of window
    
    return max_length