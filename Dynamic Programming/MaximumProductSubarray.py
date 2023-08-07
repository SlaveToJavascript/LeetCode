# https://leetcode.com/problems/maximum-product-subarray/description/
# MEDIUM
# Tags: dplc, #152

# GIVEN:
    # Given an integer array nums

# TASK:
    # find the subarray with the largest product, and return this product

# EXAMPLES:
    # Input: nums = [2,3,-2,4]
    # Output: 6
    # Explanation: [2,3] has the largest product 6.

    # Input: nums = [-2,0,-1]
    # Output: 0
    # Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# Get every possible subarray and get maximum product

# TIME COMPLEXITY: O(n^2)

#==========================================================================================================

# ✅ ALGORITHM 2: TRACK MIN AND MAX OF SUBARRAY (DYNAMIC PROGRAMMING)
# Iterate nums, starting from 1st element
# For every new element (nums[i]) added to our running subarray, we find the maximum product and the minimum

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def maxProduct(nums):
    max_product = max(nums) # we initialize result to max(nums) instead of 0 because there might be only 1 element in the array, e.g. [-1], and the result should be -1

    current_min, current_max = 1, 1

    for n in nums:
        if n == 0: # if n = 0, we want to avoid it
            current_min, current_max = 1, 1 # so we reset current min and max to 1
            continue
        # if code reaches this point, it means n != 0
        
        tempMax = current_max # this is done for the "current_min = ..." line
        current_max = max(n * current_max, n * current_min, n)
        # EXPLANATION FOR ABOVE:
        # 1. if n and existing current max are both positive: curent_max = n * current_max
        # 2. if n and existing current min are both negative: current_max = n * current_min
            # because -ve * -ve = +ve
        # 3. n
            # e.g. for nums = [-1, 8], current_min and current_max = -1, but -1 * 8 = -8 for both current_min and current_max
        
        # do the same for current_min
        # however, we can't use the variable current_max here since it was reassigned above -> we have to use a temp variable to store the value of current_max before the reassignment
        current_min = min(n * tempMax, n * current_min, n)

        max_product = max(max_product, current_max) # we update result if current_max is greater than existing result
    
    return max_product