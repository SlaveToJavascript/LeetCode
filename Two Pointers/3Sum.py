# https://leetcode.com/problems/3sum/description/
# MEDIUM
# Tags: twopointerslc, #15

# GIVEN:
    # integer array, nums

# TASK:
    # return all the triplets [nums[i], nums[j], nums[k]],
    # such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0
    # solution set must not contain duplicate triplets

###########################################################################################################

# ✅ ALGORITHM: TWO POINTERS
# Repetition of Two Sum Set II except with 1 pointer iterating whole array, 
# and Two Pointers iterating rest of array

# TIME COMPLEXITY: O(n^2)
    # O(n log n) for sorting nums array
    # O(n^2) for for-while nested loop
# SPACE COMPLEXITY: O(n)
    # Python sort function requires O(n) space

def threeSum(nums):
    nums.sort()
    result = []

    # initialize the 3 pointers
    for p1 in range(len(nums)-2): # end iteration at index len(nums)-3 so last 2 positions are for 2nd and 3rd pointers
        p2 = p1+1
        p3 = len(nums)-1
        target = -(nums[p1]) # required sum of p2 and p3 = 0-nums[p1]

        # Traverse the list to find the triplet whose sum equals 0
        while p2 < p3:
            if nums[p2] + nums[p3] < target:
                p2 += 1
            elif nums[p2] + nums[p3] > target:
                p3 -= 1
            else: # nums[p2] + nums[p3] == target
                output = [nums[p1], nums[p2], nums[p3]]
                if output not in result:
                    result.append(output)
                p2 += 1
                p3 -= 1
    
    return result