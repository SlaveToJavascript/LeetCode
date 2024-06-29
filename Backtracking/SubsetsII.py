# https://leetcode.com/problems/subsets-ii/
# MEDIUM
# Tags: backtracklc, #90

# GIVEN:
    # an integer array nums that may contain duplicates

# TASK:
    # return all possible subsets
    # NOTE: The solution set must not contain duplicate subsets
    # Return the solution in any order

# EXAMPLES:
    # Input: nums = [1,2,2]
    # Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

    # Input: nums = [0]
    # Output: [[],[0]]

###########################################################################################################

# ✅ ALGORITHM: BACKTRACKING
    # https://youtu.be/Vn2v6ajA7U0?si=UZKAp87qf2ZK5MIA&t=190
# at each element, we have 2 options: either include this element from the subset or exclude it
    # assume the 1st choice is to INCLUDE current element, 2nd choice is to EXCLUDE current element
    # for the array [1,2,2]， the decision tree looks like this:
        #                  [1,2,2]
        #                 /       \
        #             *[1]         []
        #             /   \       /  \
        #        [1,2]     [1]  [2]   []
        #        /\        /\    /  \   \  \
        # [1,2,2][1,2] [1,2][1] [2,2][2] [2][]
    # notice how [1,2] is repeated in the last row
    # think:
        # for *[1], since we're including a "2" in the left subset [1,2] in the tree, it means that for all subsets on the LEFT of *[1], there will be at least one "2" in the subset
            # therefore, for the right subset [1] of the node *[1] onwards, we SHOULD NOT BE adding any "2"s into the subsets at all (because this will result in duplicates with the left subtree of *[1])
            # this means that for the SECOND choice (which is to EXCLUDE current element), at the [1] subset on the right of *[1], we deliberately skip the 2nd "2" from being added to a subset because we know the left subtree of *[1] would already have [1,2]

# TIME COMPLEXITY: O(n * 2^n)
    # at each element, there are 2 choices: to include or to exclude the current element -> O(2^n)
        # -> we have O(2^n) subsets
    # max length of each subset = n 
# SPACE COMPLEXITY: O(n)
    # we use O(n) space to maintain comb, and are modifying comb in-place with backtracking

def subsetsWithDup(nums):
    result = []
    nums.sort() # sort nums to make it easier to prevent duplicates

    def backtrack(i, subset):
        if i == len(nums): # if current index has reached the end of nums array
            result.append(subset[:])
            return
        
        # all subsets that INCLUDE nums[i]
        subset.append(nums[i])
        backtrack(i+1, subset)
        subset.pop()

        # all subsets that EXCLUDE nums[i]
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1 # skip nums[i]
        backtrack(i+1, subset)
    
    backtrack(0, [])
        
    return result