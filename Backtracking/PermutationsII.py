# https://leetcode.com/problems/permutations-ii/
# MEDIUM
# Tags: backtracklc, #47

# GIVEN:
    # an array, nums, that might contain duplicates

# TASK:
    # return all possible unique permutations in any order

# EXAMPLES:
    # Input: nums = [1,1,2]
    # Output:
    # [[1,1,2],
    #  [1,2,1],
    #  [2,1,1]]

    # Input: nums = [1,2,3]
    # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

###########################################################################################################

# ✅ ALGORITHM: BACKTRACKING
# to avoid generating any duplicate permutations, at each step rather than viewing each number as a candidate, we consider each unique number as the true candidate
# e.g. at the very beginning, given the input of [1, 1, 2], we have only two true candidates (1 and 2) instead of three (1, 1, 2)
# MAIN IDEA: to find out all the unique numbers at each stage, we create a Counter() hashmap with each unique number as key and its frequency in nums as the value
# TODO: define a function called backtrack(comb, counter) which generates all permutations, starting from the current combination (comb) and the remaining numbers (in hashmap)

# TIME COMPLEXITY: O(n * n!)
    # n! to generate n! different permutations
    # For each of the n! combinations, we need O(n) time to copy each combination into result array
# SPACE COMPLEXITY: O(n)
    # The extra space here is for comb and the recursion call stack
    # The depth of the call stack is equal to the length of comb, which is limited to n

from collections import Counter

def permuteUnique(nums):
    result = []

    def backtrack(comb, hashmap):
        if len(comb) == len(nums):
            result.append(comb[:])
            return
        
        for num in hashmap:
            if hashmap[num] > 0:
                comb.append(num)
                hashmap[num] -= 1 # decrement the frequency of num in hashmap after adding it to a combination

                backtrack(comb, hashmap)

                comb.pop() # revert the choice for the next exploration
                hashmap[num] += 1
    
    backtrack([], Counter(nums))
    return result