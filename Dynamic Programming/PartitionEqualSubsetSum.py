# https://www.youtube.com/watch?v=IsvocB5BJhw
# MEDIUM
# Tags: dplc, 0/1 Knapsack, 01knapsack, #416

# GIVEN:
    # an integer array, nums

# TASK:
    # return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal
    # return false otherwise

# EXAMPLES:
    # Input: nums = [1,5,11,5]
    # Output: true
    # Explanation: The array can be partitioned as [1, 5, 5] and [11].

    # Input: nums = [1,2,3,5]
    # Output: false
    # Explanation: The array cannot be partitioned into equal sum subsets.

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# For each element in nums, we can either include it in the first subset or the second subset
# So for each element in nums, we have 2 choices

# TIME COMPLEXITY: O(2^n) 👎

#==========================================================================================================

# ✅ ALGORITHM 2: DYNAMIC PROGRAMMING
# let target be the sum of nums / 2
    # i.e. each resulting subset should have a sum of target
# if you're able to find a subset in nums that has a sum of target, then the 2nd subset which contains the remaining elements is definitely = target as well
# MAIN IDEA: just find 1 subset where sum(subset) = target!

# TIME COMPLEXITY: O(len(nums) * sum(nums)/2) = O(n^2)

def canPartition(nums):
    if sum(nums) % 2 != 0: return False # if sum(nums) is odd, it's impossible to find 2 subsets with equal sums

    target = sum(nums) / 2 # this is the target sum of each subset of our result

    dp = [False] * (target+1)
    # dp[i] = True means there is a subset in nums where sum(subset) = i
    # dp[i] = False means there is no subset in nums where sum(subset) = i
    dp[0] = True # sum of empty subset from nums = 0

    for num in nums:
        for i in range(len(dp)-1, num-1, -1):
            # iterate backwards from target to num
                # NOTE: if we iterate from 0 to target, then we will be overwriting dp[i] before we use it
                # NOTE: we have to end at num, otherwise it will check for a negative sum
            # if dp[i-num] is True, then there is a subset in nums where sum(subset) = i-num
            # so if we add num to that subset, then sum(subset) = i
            # so dp[i] = True
            dp[i] = dp[i] or dp[i-num]
    
    return dp[target] # since we want to know if there is a subset in nums where sum(subset) = target