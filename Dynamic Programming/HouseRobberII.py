# https://leetcode.com/problems/house-robber-ii/
# MEDIUM
# Tags: dplc, #213

# GIVEN:
    # an integer array, nums, representing the amount of money that can be robbed from each house

# TASK:
    # Maximize the amount of money that can be robbed without robbing any 2 adjacent houses
    # NOTE: All houses at this place are arranged in a circle
        # the first house is the neighbor of the last one

# EXAMPLES:
    # Input: nums = [2,3,2]
    # Output: 3
    # Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

    # Input: nums = [1,2,3,1]
    # Output: 4
    # Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    # Total amount you can rob = 1 + 3 = 4.

    # Input: nums = [1,2,3]
    # Output: 3

###########################################################################################################

# ✅ ALGORITHM 1: ITERATIVE DP
# Since we cannot rob both the 1st and last house (as they are adjacent), the max amount that can be robbed = max(max amount that can be robbed from all houses except 1st house, max amount that can be robbed from all houses except last house, amount at 1st house)
    # the "amount at 1st house" is included for the edge case where there is only 1 house
# We run the function from House Robber twice, 1 time for each of the above situations (i.e. without first house, without last house)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def rob(nums):
    def max_robbed(amounts):
        rob1, rob2 = 0, 0

        for amount in amounts:
            curr_robbed = max(rob1 + amount, rob2)

            rob1 = rob2
            rob2 = curr_robbed
        
        return curr_robbed
    
    return max(max_robbed(nums[1:]), max_robbed(nums[:-1]), nums[0])