# https://leetcode.com/problems/3sum-closest/description/
# MEDIUM
# Tags: twopointerslc, #16

# GIVEN:
    # an integer array, nums, of length n
    # an integer, target

# TASK:
    # find 3 integers in nums such that the sum is closest to target
    # TODO: Return the sum of the three integers
    # You may assume that each input would have exactly 1 solution

# EXAMPLES:
    # Input: nums = [-1,2,1,-4], target = 1
    # Output: 2
    # Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

    # Input: nums = [0,0,0], target = 1
    # Output: 0
    # Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

###########################################################################################################

# ✅ ALGORITHM: TWO POINTERS
# (Repetition of Two Sum Set II except with 1 pointer iterating whole array, and 2 other pointers iterating rest of array)
# Sort nums array
# use p1 to iterate through all elements in nums
    # p1 is a fixed target for current iteration, i.e. while p2 and p3 are shifting to get sum closest to target, p1 remains pointing to the same element
# initialize p2 to point to next element after p1
# initialize p3 to point to last element in nums
# keep checking if absolute difference between p1+p2+p3 sum vs target is the smallest absolute difference
    # if current absolute difference = 0, return p1+p2+p3 sum as this is the answer (you can't get a minimum absolute difference that is less than 0)
    # else, if current absolute difference is the smallest absolute difference so far, update min. absolute difference and update sum with min. absolute difference
    # if p1+p2+p3 sum is less than target, shift p2 to the right; if sum is more than target, shift p3 to the left
# return sum with min. absolute difference

# TIME COMPLEXITY: O(n^2)
    # O(n log n) for sorting nums array
    # O(n^2) for for-while nested loop
        # for-loop iterates each element of nums -> O(n)
        # at each element in nums, in the worst case, p2 and p3 iterate the whole of the remaining array to the right of p1 -> O(n) in the worst case
        # -> Overall TC = O(n^2)
# SPACE COMPLEXITY: O(n)
    # python sort() takes O(n) space

def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = 0 # i.e. sum with smallest absolute diff (i.e. return value)
    min_diff = float('inf') # min. absolute difference

    for p1 in range(len(nums)):
        p2 = p1 + 1 # p2 is initialized to the index after p1
        p3 = len(nums)-1 # p3 initialized to last element in nums

        while p2 < p3:
            curr_sum = nums[p1] + nums[p2] + nums[p3]
            abs_diff = abs(curr_sum-target) # absolute difference of sum - target
            if abs_diff == 0: # we found 3 numbers whose sums = target -> return sum (since this is the closest we can possibly get to target)
                return curr_sum
            
            if abs_diff < min_diff: # if current absolute difference is less than min. absolute difference,
                min_diff = abs_diff # update min. absolute difference
                closest_sum = curr_sum # update sum with min. absolute difference
            
            if curr_sum < target: # if sum is less than target, we want to increase sum
                p2 += 1 # shift p2 to the right to increase sum
            elif curr_sum > target: # if sum is greater than target, we want to decrease sum
                p3 -= 1 # shift p3 to the left to decrease sum
    
    return closest_sum # return sum with the min. absolute difference