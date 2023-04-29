# https://leetcode.com/problems/two-sum/

# BRUTE FORCE
    # 2 for-loops
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    # space required does not depend on the size of the input array, so only constant space is used
def twoSum(nums, target):
    for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if num + nums[j] == target:
                    return [i, j]

# DICTIONARY SEARCH
    # Time complexity: O(n)
    # Space complexity: O(n)
        # extra space required depends on the no. of items in dictionary, which stores exactly n elements
def twoSum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if num in d:
            return [d[num], i]
        else:
            d[target - num] = i