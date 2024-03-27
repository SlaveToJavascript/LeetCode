# 2863. Maximum Length of Semi-Decreasing Subarrays
# https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/description/
# MEDIUM
# Tags: monotonicstacklc, monotoniclc, stacklc, #2863

# GIVEN:
    # an integer array, nums

# TASK:
    # Return the length of the longest semi-decreasing subarray of nums, and 0 if there are no such subarrays
        # A non-empty array is semi-decreasing if its first element is strictly greater than its last element

# EXAMPLES:
    # Input: nums = [7,6,5,4,3,2,1,6,10,11]
    # Output: 8
    # Explanation: Take the subarray [7,6,5,4,3,2,1,6].
    # The first element is 7 and the last one is 6 so the condition is met.
    # Hence, the answer would be the length of the subarray or 8.
    # It can be shown that there aren't any subarrays with the given condition with a length greater than 8.

    # Input: nums = [57,55,50,60,61,58,63,59,64,60,63]
    # Output: 6
    # Explanation: Take the subarray [61,58,63,59,64,60].
    # The first element is 61 and the last one is 60 so the condition is met.
    # Hence, the answer would be the length of the subarray or 6.
    # It can be shown that there aren't any subarrays with the given condition with a length greater than 6.

###########################################################################################################

# ✅ ALGORITHM: INCREASING MONOTONIC STACK
# MAIN IDEA:
    # Consider a valid subarray beginning at index l, ending at r
        # if l < r and nums[l] > nums[r], this subarray is a valid semi-decreasing subarray
    # to make the above subarray to be the longest possible one, we make sure that:
        # 1. there is no smaller index l' where nums[l'] >= nums[l]
            # i.e. all no.s before the subarray are smaller than the no. at index l
        # 2. there is no larger index r' where nums[r'] <= nums[r]
            # i.e. all no.s after the subarray are larger than the no. at index r

def maxSubarrayLength(nums):
    stack = []

    for r in range(len(nums)-1, -1, -1):
        if not stack or nums[r] < nums[stack[-1]]: # if we get a smaller element than the element at the last index in stack, we append it to stack -> stack becomes a decreasing array
            stack.append(r) # NOTE: stack will contain all possible ending indexes of valid subarrays
        # the above code works since we want to get the smallest possible ending index r such that all elements after r are LARGER -> when we iterate from back to front and encounter a SMALLER element than the last element in stack, we append it to stack, because this smaller element is a potential ending index for a valid subarray, and all elements on its right are larger than it!
        
    result = 0 # return value (max len of valid subarray)
    starting_num = float('-inf') # cannot be 0 as that wouldn't work if all elements in nums are -ve

    # look for a possible starting index, l
    for l in range(len(nums)):
        while stack and stack[-1] <= l: # since ending index r must be > starting index l, if last index in stack is <= l, it can't possibly be the ending index for a subarray starting at index l
            stack.pop() # therefore we elimunate the last index from stack since it's invalid
    
        # since we want to get largest possible starting value, every possible starting value (nums[l]) must be greater than all elements that come before it in nums array
        if nums[l] > starting_num: # starting_num is the previous possible starting value; we only consider nums[l] if it's greater than starting_num, since we shouldn't have any larger values than nums[l] existing on the left of nums[l] in the nums array
            starting_num = nums[l] # since nums[l] > starting_num, update starting_num with nums[l]

            while stack and nums[stack[-1]] < starting_num: # while the last element in stack (i.e. a possible ending index) is smaller than the starting_num (i.e. while starting_num and nums[stack[-1]] are the start and end of a valid subarray),
                result = max(result, stack[-1] - l + 1) # update result with the length of the current subarray that starts with starting_num and ends with nums[stack[-1]]
                stack.pop() # pop the current ending index stack[-1] to explore longer valid subarrays
    
    return result