# https://leetcode.com/problems/combination-sum-ii/
# MEDIUM
# Tags: backtracklc, #40

# GIVEN:
    # an array of integers, candidates
    # a target integer, target

# TASK:
    # find all unique combinations in candidates where the candidate numbers sum to target
    # Each number in candidates may only be used once in the combination
    # NOTE: The solution set must not contain duplicate combinations

# EXAMPLES:
    # Input: candidates = [10,1,2,7,6,1,5], target = 8
    # Output: 
    # [
    # [1,1,6],
    # [1,2,5],
    # [1,7],
    # [2,6]
    # ]

    # Input: candidates = [2,5,2,1,2], target = 5
    # Output: 
    # [
    # [1,2,2],
    # [5]
    # ]

###########################################################################################################

# ✅ ALGORITHM: BACKTRACKING
# NOTE: to prevent duplicate combinations:
    # sort the candidates array
    # if we choose to include 1, we can include all 1's from the rest of the array
    # if we choose to skip 1, we cannot include any more 1's in our combination
    # The idea behind this is that, if in one decision path we include 1's while in the other decision path we don't include any 1's, then the combinations from these 2 different decision paths will always be different

# TIME COMPLEXITY: O(k * 2^n)
    # k = average length of each combination, n = length of candidates array
    # at each element, you have 2 choices to choose from: include or not include this element
    # ea
# SPACE COMPLEXITY: 

def combinationSum2(candidates, target):
    candidates.sort() # this makes it easier for us to prevent duplicates
    result = []

    def backtrack(start, comb, total):
        # if we found the desired sum, add it to the results array
        if total == target:
            result.append(comb[:])
            return

        # if we went over the target sum or start index is out of bounds, end recursion
        if total > target or start >= len(candidates):
            return
        
        # we need to track the prev no. because:
            # in candidates array, if the next no. is the same as the current no., we should skip the next no.
            # e.g. if current no. in candidates is 1 and next no. is also 1, we shouldn't include any 1's in the next combination. However, we can include multiple 1's in the previous combination, as long as there are also multiple 1's in candidates
            # this, together with the sorting, makes it possible for us to prevent duplicates
        prev_candidate = -1
        for i in range(start, len(candidates)): # i only iterates from index start to end
            if candidates[i] == prev_candidate:
                continue # skip current candidate at i if it's == previous candidate
            
            comb.append(candidates[i])
            backtrack(i+1, comb, total + candidates[i])
            comb.pop()

            prev_candidate = candidates[i]
        
    backtrack(0, [], 0)
    return result

# 1, [1], 1