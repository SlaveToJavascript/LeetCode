# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/
# MEDIUM
# Tags: kadanelc, #53

# GIVEN:
    # Given an integer array nums

# TASK:
    # find the subarray with the largest sum, and return its sum

# EXAMPLES:
    # Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    # Output: 6
    # Explanation: The subarray [4,-1,2,1] has the largest sum 6.

    # Input: nums = [1]
    # Output: 1
    # Explanation: The subarray [1] has the largest sum 1.

    # Input: nums = [5,4,-1,7,8]
    # Output: 23
    # Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# 1 for loop to represent starting index
# 1 for loop to represent ending index
# 1 for loop to iterate from start to end

# TIME COMPLEXITY: O(n^3)

# Code:
# for start in range(len(array)):
#     for end in range(start, len(array)):
#         for i in range(i, j):
#             # compute sum here

#============================================================================================================

# ❌ ALGORITHM 2: SAVE THE SUMS OF PREVIOUS SUBARRAYS
# save the sum of each subarray
# then when shifting the end forward, simply add the next number to the sum of previous subarray

# TIME COMPLEXITY: O(n^2)

# Code:
# for start in range(len(array)):
#     for end in range(start, len(array)):
#         currentSum += array[end]

#============================================================================================================

# ✅ ALGORITHM 3: REMOVE NEGATIVE PREFIX / SLIDING WINDOW
# Iterate through nums and add each number to curr_sum
# If prefix sum is -ve, we would exclude this negative prefix sum out from our calculation (curr_sum)
    # because a negative prefix will only reduce our current sum, it cannot contribute positively to current sum so we might as well exclude it
    # therefore, if curr_sum is negative, reset curr_sum to 0 so we only continue with the remaining elements in nums
    # else, if curr_sum is positive, we continue adding current num to curr_sum
    # every time we add a num to curr_sum, we update max_sum with curr_sum

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def maxSubarray(nums):
    max_sum = nums[0] # start finding max subarray sum from 1st element
        # we cannot initiate max_sum = 0 as it will incorrectly return 0 for the edge case where all numbers in nums are -ve
    curr_sum = 0 # current running sum of subarray

    for num in nums:
        if curr_sum < 0: # if current sum until the element before num is -ve, 
            curr_sum = 0 # remove previous elements from current sum and reset curr_sum to 0
        
        curr_sum += num # add current element to current sum
        max_sum = max(max_sum, curr_sum) # update max sum encountered so far
    
    return max_sum

#============================================================================================================

# ✅ ALGORITHM 4: KADANE'S ALGORITHM
# Maintain 2 maximums: current maximum and global maximum
# Iterate nums array; for each element i, current_max is updated to max(element i, sum up to and INCLUDING element i)
# every time after curr_max is updated, we also update global_max to be the max of existing global_max value vs curr_max value
# after iterating through entire list, return final global_max value

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def maxSubarray(nums):
    currMax, globalMax = float('-inf'), float('-inf') # initiate globalMax and currMax
    
    for num in nums: # for each no. in nums,
        currMax = max(num, currMax + num) # get the max between current no. sum of no.s from 1st to current no.
        globalMax = max(globalMax, currMax) # update global max after every currMax update

    return globalMax