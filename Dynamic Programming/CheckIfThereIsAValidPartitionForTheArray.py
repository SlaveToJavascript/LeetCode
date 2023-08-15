# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/description/
# MEDIUM
# Tags: dplc, #2369

# GIVEN:
    # integer array, nums

# TASK:
    # partition the array into one or more contiguous subarrays
    # We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:
        # The subarray consists of exactly 2 equal elements
            # e.g. [2,2]
        # The subarray consists of exactly 3 equal elements
            # e.g. [4,4,4]
        # The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1
            # e.g [3,4,5]
    # TODO: Return true if the array has at least one valid partition. Otherwise, return false

# EXAMPLES:
    # Input: nums = [4,4,4,5,6]
    # Output: true
    # Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
    # This partition is valid, so we return true.

    # Input: nums = [1,1,1,2]
    # Output: false
    # Explanation: There is no valid partition for this array.

###########################################################################################################

# ✅ ALGORITHM: DYNAMIC PROGRAMMING (TOP DOWN + MEMOIZATION) (not space optimized)
# Define helper function isValidPartition(i) which returns True if nums[0:i] (inclusive) is a valid subarray which satisfies 1 of the 3 conditions
# This function recursively checks for the last 2 / last 3 elements (if they satisfy any 1 of the 3 conditions) then reduces the problem area to nums[0:i-2] or nums[0:i-3] (inclusive)
# Cache the result to a dp hashmap, where key = i and value = True if nums[0:i] is a valid partition, False otherwise
    # initate dp hashmap to {-1: True} since an empty array always has a valid partition
        # if i = -1, it means it's an empty array

# TIME COMPLEXITY: O(n)
    # isValidPartition(i) recursively calls itself to determine the existence of a valid partition for the current subarray nums[0:i] (inclusive)
    # Due to memoization, we only calculate each value of i once
# SPACE COMPLEXITY: O(n)
    # The recursive solution uses the call stack to keep track of the current function being processed
    # The maximum depth of the call stack equals n/2 as the index is decremented by at least 2 at each call, resulting in a space complexity of O(n)
    # The dp hashmap stores at most n pairs, which also takes O(n) space

def validPartition(nums):
    dp = {-1: True} # since an empty array always has a valid partition

    def isValidPartition(i): # returns True if nums[0:i] is a valid partition
        if i in dp:
            return dp[i] # if i is already in dp (has been calculated before), we can simply return it
        result = False # return value; initialize to False

        # Check if the subarray satisfies one of the 3 conditions below:
        # 1) subarray consists of exactly 2 equal elements, e.g. [4,4]
        if i-2 >= -1 and nums[i-1] == nums[i]:
            result = result or isValidPartition(i-2)
                # NOTE: we cannot directly return result here, since if this condition is not satisfied, we still have to check for the other conditions
                # NOTE: we have to use "result or ..." because if any 1 of the conditions is True, then we'll return True, even if for another condition, isValidPartition() returns False
                    # "result = result or ..." returns True as long as 1 of the conditions is True
        
        # 2) subarray consists of exactly 3 equal elements, e.g. [4,4,4]
        if i-3 >= -1 and nums[i-2] == nums[i-1] == nums[i]:
            result = result or isValidPartition(i-3)

        # 3) subarray consists of exactly 3 consecutive increasing elements, e.g. [3,4,5]
        if i-3 >= -1 and nums[i-1] - nums[i-2] == 1 and nums[i] - nums[i-1] == 1:
            result = result or isValidPartition(i-3)
    
    return isValidPartition(len(nums)-1)

#==========================================================================================================

# ✅ ALGORITHM 2: ITERATIVE DYNAMIC PROGRAMMING (BOTTOM UP) (not space optimized)
# Create dp array of size len(nums), where dp[i] is True if nums[i:] is a valid subarray that satisfies 1 of 3 conditions
# Fill up dp array from the end:
# 1) if dp[i] = dp[i+1], 1st condition (subarray consists of exactly 2 equal elements) is satisfied, so we check if dp[i+2] is a valid subarray
    # if dp[i+2] is False, dp[i] = False
# 2) if dp[i] = dp[i+1] = dp[i+2], 2nd condition (subarray consists of exactly 3 equal elements) is satisfied, so we check if dp[i+3] is a valid subarray
    # if dp[i+3] is False, dp[i] = False
# 3) if dp[i]+2 = dp[i+1]+1 = dp[i+2], 3rd condition (subarray consists of exactly 3 consecutive increasing elements) is satisfied, so we check if dp[i+3] is a valid subarray
    # if dp[i+3] is False, dp[i] = False
# NOTE: if any 1 of the above conditions is satisfied and the 2nd check (dp[i+2] or dp[i+3]) is also True, then dp[i] will be set to True
# return dp[0]

# TIME COMPLEXITY: O(n)
    # We iterate through the entire array once
# SPACE COMPLEXITY: O(n)
    # We create a dp array of size n

def validPartition(nums):
    dp = [False] * len(nums) + [True] # initialize last element to True since an empty array always has a valid partition

    for i in range(len(nums)-1, -1, -1): # iterate nums from the back

        # 1st condition (subarray consists of exactly 2 equal elements) is satisfied
        if len(nums)-i >= 2 and nums[i] == nums[i+1]:
            dp[i] |= dp[i+2] # check if dp[i+2] is a valid subarray

        # 2nd condition (subarray consists of exactly 3 equal elements) is satisfied
        if len(nums)-i >= 3 and nums[i] == nums[i+1] == nums[i+2]:
            dp[i] |= dp[i+3] # check if dp[i+3] is a valid subarray

        # 3rd condition (subarray consists of exactly 3 consecutive increasing elements) is satisfied
        if len(nums)-i >= 3 and nums[i]+2 == nums[i+1]+1 == nums[i+2]:
            dp[i] |= dp[i+3] # check if dp[i+3] is a valid subarray
        
    return dp[0]

#==========================================================================================================

# ✅ ALGORITHM 3: ITERATIVE DYNAMIC PROGRAMMING (BOTTOM UP) (space optimized)
# Same as above, but we only need the dp to be of length 3 since, when we fill up dp, each time we only need the 3 closest True/False values

# TIME COMPLEXITY: O(n)
    # We iterate through the entire array once
# SPACE COMPLEXITY: O(1)

def validPartition(nums):
    two = nums[-1] == nums[-2] # check if the last 2 elements are equal; if yes, 1st condition is satisfied for the 2nd last element in nums

    if len(nums) == 2: # edge case: if nums has 2 elements
        return two
    
    three = (nums[-1] == nums[-2] == nums[-3]) or (nums[-3] + 2 == nums[-2] + 1 == nums[-1]) # check if 2nd and 3rd conditions are satsfied for the 3rd last element in nums
    dp = [three, two, False] # dp[-1] is False as we cannot partition an array of size 1

    for i in range(len(nums)-4, -1, -1): # start iterating from behind, starting from i = len(nums)-4, since the True/False conditions for the last 3 elements have already been filled up
        curr = (nums[i] == nums[i+1]) and dp[1] # if 1st condition satisfied, check if dp[1] is True
        
        curr = curr or (
                        (nums[i] == nums[i+1] == nums[i+2] or nums[i+2] == nums[i+1] + 1 == nums[i] + 2)
                        and dp[2]
        ) # if 2nd or 3rd condition satisfied, check if dp[2] is True
        
        dp = [curr, dp[0], dp[1]] # shift the values in dp for the next iteration of for-loop
    
    return dp[0]