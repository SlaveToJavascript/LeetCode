# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# MEDIUM

# GIVEN:
    # Sorted integer array, nums
    # integer target

# TASK:
    # Find two no.s such that they add up to target
    # Return [index1, index2] where 0 <= index1 < index2 < nums.length
    # NOTE: there is exactly one solution and you may not use the same no. twice
    # Your solution must use only constant extra space! (i.e. no hashmap, additional O(n) array, etc.)

# EXAMPLES:
    # Input: numbers = [2,7,11,15], target = 9
    # Output: [1,2]
    # Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

    # Input: numbers = [2,3,4], target = 6
    # Output: [1,3]
    # Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

    # Input: numbers = [-1,0], target = -1
    # Output: [1,2]
    # Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

###########################################################################################################

# ✅ ALGORITHM 1: TWO POINTERS
# Since nums array is sorted, we can use this to our advantage
    # by shifting left & right pointers based on whether their elements' sum are >, < or == target
# if nums[left] + nums[right] < target, shift left pointer to the right (to increase the sum)
# if nums[left] + nums[right] > target, shift right pointer to the left (to decrease the sum)
# else, return [left, right]

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]