# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
# HARD
# Tags: binarysearchlc, #315

# GIVEN:
    # an integer array, nums

# TASK:
    # return an integer array, counts, where counts[i] is the number of smaller elements to the right of nums[i]

# EXAMPLES:
    # Input: nums = [5,2,6,1]
    # Output: [2,1,1,0]
    # Explanation:
    # To the right of 5 there are 2 smaller elements (2 and 1).
    # To the right of 2 there is only 1 smaller element (1).
    # To the right of 6 there is 1 smaller element (1).
    # To the right of 1 there is 0 smaller element.

    # Input: nums = [-1]
    # Output: [0]

    # Input: nums = [-1,-1]
    # Output: [0,0]

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE (TLE)
# Iterate through nums array
# for each element in nums array, sum up the no. of elements on its right that are greater that current nums element
# Return the counts array

# TIME COMPLEXITY: O(n^2) 👎
# SPACE COMPLEXITY: O(n)

def countSmaller(nums):
    result = []
    for i in range(len(nums)):
        count = sum(num < nums[i] for num in nums[i+1:])
        result.append(count)
    return result

#==========================================================================================================

# ✅ ALGORITHM 2: BINARY SEARCH
# MAIN IDEA: maintain an additional sorted array for nums, so for each num in nums, we can do binary search on the sorted nums array to find this num in sorted nums array -> the no. of elements before this num in sorted nums array is the no. of elements on the right of num in the original nums array that are smaller than num
# bisect_left() will always insert an element into the lowest possible index of an array while maintaining sorted order
    # i.e. if num to be inserted is a duplicate element that already exists in sorted_nums, then bisect_left() would return the leftmost index where num can be inserted, which is in front of the duplicate num in sorted_nums
# NOTE: bisect_left() is a binary search operation, so its TC is O(log n)

# TIME COMPLEXITY: O(n log n) on average
    # O(n) for iterating nums array
    # for each iteration of nums array, bisect_left() performs binary search to find index to be inserted to -> O(log n)
    # TC = O(n) * O(log n) on average
    # NOTE: even though del nums[i] is O(n) TC in the worst case, on average it is O(1)
# SPACE COMPLEXITY: O(n)
    # for sorted_nums array

from bisect import bisect_left

def countSmaller(nums):
    sorted_nums = sorted(nums)
    result = []

    for num in nums:
        i = bisect_left(sorted_nums, num) # i is the index where current num should be inserted (into the sorted nums array)
        result.append(i) # if num should be inserted at the ith index of the sorted array, then there are i elements on the left of i
        del sorted_nums[i] # delete num from sorted_nums array so that it doesn't get counted again
    
    return result