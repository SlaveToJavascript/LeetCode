# https://leetcode.com/problems/house-robber/
# MEDIUM
# Tags: dplc, #198

# GIVEN:
    # an integer array, nums, representing the amount of money that can be robbed from each house

# TASK:
    # Maximize the amount of money that can be robbed without robbing any 2 adjacent houses

# EXAMPLE:
    # Input: nums = [1,2,3,1]
    # Output: 4
    # Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    # Total amount you can rob = 1 + 3 = 4.

    # Input: nums = [2,7,9,3,1]
    # Output: 12
    # Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    # Total amount you can rob = 2 + 9 + 1 = 12

###########################################################################################################

# ✅ ALGORITHM 1: ITERATIVE DP
# Create integer array, dp, with same length as nums
# For every house nums[i], dp[i] will be the max amount that can be robbed up to the house at nums[i]
# max amount at dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    # at dp[i], can either choose to rob only the previous house (at i-1) or to rob the current house + the house before the previous house (nums[i] + dp[i-2])
# return the last element in dp (which is the total maximum that can be robbed from all houses)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def rob(nums):
    if len(nums) == 1: return nums[0]
    dp = [0] * len(nums) # initiate dp of len(nums)
    dp[0], dp[1] = nums[0], max(nums[1], nums[0])
    # at the 0th house, max that can be robbed = nums[0]
    # at the 1st house, max that can be robbed = max between current house (i=1) and previous house (i=0)
    for i in range(2, len(nums)):
        dp[i] = max(nums[i]+dp[i-2], dp[i-1]) # fill up dp with the max amounts that can be robbed up to the ith house for the remaining houses
    return dp[-1] # last element of dp = max that can be robbed up till last house (i.e. all houses)

#==========================================================================================================

# ✅✅✅ ALGORITHM 2: ITERATIVE DP WITH CONSTANT SPACE (space-optimized)
# Instead of creating a dp array to keep track of the max amount that can be robbed reaching the ith house, we can simply iteratively calculate the max amount and return the max amount that can be robbed at the last house

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def rob(nums):
    rob1, rob2 = 0, 0 # rob1 is the max amount that can be robbed reaching the 2nd previous house before the current house, and rob2 is the max amount that can be robbed reaching the house before the current house

    for num in nums: # start calculating the max amounts robbed for each of the houses
        curr_rob = max(rob1 + num, rob2) # the max amount that can be robbed reaching the current house (i.e. num)
        
        # we move on to the next house, and the previous rob2 becomes the next rob1
        # the previous current becomes the next rob2
        rob1 = rob2
        rob2 = curr_rob
    
    return curr_rob # at this point curr_rob = max amount that can be robbed reaching the last house