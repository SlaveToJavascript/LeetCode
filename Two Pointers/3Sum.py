# https://leetcode.com/problems/3sum/description/
# MEDIUM

# GIVEN:
    # integer array, nums

# TASK:
    # return all the triplets [nums[i], nums[j], nums[k]],
    # such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0
    # solution set must not contain duplicate triplets

###########################################################################################################

# ALGORITHM: TWO POINTER
# Repetition of Two Sum Set II except with 1 pointer iterating whole array, 
# and Two Pointers iterating rest of array

def threeSum(nums):
    nums.sort()
    result = []
    for p1 in range(len(nums)-2): # end iteration at index len(nums)-3 so last 2 positions are for 2nd and 2rd pointers
        p2 = p1+1
        p3 = len(nums)-1
        target = -(nums[p1]) # required sum of p2 and p3 = 0-nums[p1]

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