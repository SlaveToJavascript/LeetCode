# 713. Subarray Product Less Than K
# https://leetcode.com/problems/subarray-product-less-than-k/description/
# MEDIUM
# Tags: slidingwindowlc, #713

# GIVEN:
    # an array of integers, nums
    # an integer, k

# TASK:
    # return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k

# EXAMPLES:
    # Input: nums = [10,5,2,6], k = 100
    # Output: 8
    # Explanation: The 8 subarrays that have product less than 100 are:
    # [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
    # Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

    # Input: nums = [1,2,3], k = 0
    # Output: 0

###########################################################################################################

# ✅ ALGORITHM: SLIDING WINDOW
# MAIN CONCEPT:
    # maintain a window of elements whose total product < k
        # the window continuously expands from the right, checks the total product, and shrinks from the left while product >= k
    # if a certain window has total product < k, all possible subarrays formed by selecting subsets of elements within the current window (from left to right) will also have a product strictly less than k
        # e.g. if the product of nums[i...j] inclusive is < k, then the product of nums[i+1...j] ... all the way to nums[j...j] inclusive is also < k -> we can count all of these valid subarrays towards the result
                # the no. of valid subarrays = j-i+1, which represents the no. of valid subarrays ending at j and starting at any element between i and j inclusive
                    # e.g. if array[l:r] = [3,4,5], and we include 6 in the window, we need to count all possible subarrays that end with 6
                    # These subarrays can be formed by starting at any element within the current window and extending to 6:
                # [6], [5,6], [4,5,6], [3,4,5,6]
                # hence, the total no. of valid arrays = r-l+1 = 3-0+1 = 4
                # as we can observe, adding 6 to the window created 4 new subarrays

# TIME COMPLEXITY: O(n)
    # O(n) for the for-loop
    # the while-loop terminates when the product < k, and this can happen max. n times in total (1 for each element) -> overall TC = O(2n)
# SPACE COMPLEXITY: O(1)

def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0 # since all elements are integers, we cannot get total product of any array to be STRICTLY LESS than 1 (must be at least = 1)
    
    result = 0 # return value
    product = 1 # total product of window (must be < k for it to be a valid window), initialized to 1
    
    l = 0 # boundaries of window denoted by l and r pointers (inclusive)
    for r in range(len(nums)):
        product *= nums[r] # expand window from right, and include rightmost element in window to total product

        while product >= k: # total product is not less than k -> need to shrink window
            product //= nums[l] # exclude leftmost element in window from total product
            l += 1 # shrink window by moving l pointer forward
        
        # when we reach this point, it means product of current window < k -> add no. of valid subarrays ending at r to the result
        result += r-l+1
    
    return result