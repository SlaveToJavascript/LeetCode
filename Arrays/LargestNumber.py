# 179. Largest Number
# https://leetcode.com/problems/largest-number/
# MEDIUM
# Tags: arraylc, greedylc, sortlc, #179

# GIVEN:
    # a list of non-negative integers, nums

# TASK:
    # arrange them such that they form the largest number and return it
    # Since the result may be very large, so you need to return a string instead of an integer

# EXAMPLES:
    # Input: nums = [10,2]
    # Output: "210"

    # Input: nums = [3,30,34,5,9]
    # Output: "9534330"

###########################################################################################################

# ✅ ALGORITHM 1: USE CUSTOM SORTING KEY
# cmp_to_key (from functools) is a function that allows sort() or sorted() functions to use a custom sorting key
    # define a custom comparator function and use that as the key for sort() or sorted()
    # SYNTAX (ASCENDING SORT) FOR cmp(a,b):
        # if a < b: return -1 (a should come before b in the resulting sorted list)
        # if a > b: return 1 (a should come after b in the resulting sorted list)
        # is a = b: return 0
    # for DESCENZING SORT, just reverse the return values (1 and -1)
# STEPS:
    # 1. Convert all numbers in nums to strings
    # 2. Define comparator function which sorts the string integers in descending order based on the concatenation of the two strings
        # e.g. if a = "3" and b = "30", then a + b = "330" > b + a = "303" --> a should come before b
    # 3. Sort the string integers array using the custom comparator function and return the result as a string

# TIME COMPLEXITY: O(n log n)
    # for sort function
# SPACE COMPLEXITY: O(n)
    # sort function uses O(n) space

from functools import cmp_to_key

def largestNumber(nums):
    if max(nums) == 0:
        return "0" # handling edge case where all numbers in nums are 0
    
    nums = list(map(str, nums))

    def compare(a, b):
        if a + b > b + a:
            return -1
        if a + b < b + a:
            return 1
        return 0
    
    nums.sort(key = cmp_to_key(compare))
    return "".join(nums)

#==========================================================================================================

# ✅ ALGORITHM 2: USE BUILT-IN SORT FUNCTION WITH LAMBDA FUNCTION
# to handle cases where numbers have different lengths (e.g., 3 vs. 30), we want to see which combination (e.g., 3 + 30 = '330' vs. 30 + 3 = '303') forms a larger number
    # to achieve this, we can use multiplication to replicate the string enough times to make a meaningful comparison
    # e.g. '3' * 10 = '3333333333' and '30' * 10 = '30303030303030303030' -> When sorted, '3' will come before '30' because '3333333333' > '30303030303030303030'
# therefore, we can sort the string integers array using a lambda function that replicates the strings enough times to make a meaningful comparison (e.g. string * 10)

# TIME COMPLEXITY: O(n log n)
    # for sort function
# SPACE COMPLEXITY: O(n)
    # sort function uses O(n) space

def largestNumber(nums):
    num_strings = [str(num) for num in nums]
    num_strings.sort(key=lambda a: a * 10, reverse=True) # ! most important step

    if num_strings[0] == "0": # if largest no. is 0
        return "0"

    return "".join(num_strings)