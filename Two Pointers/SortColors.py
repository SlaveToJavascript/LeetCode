# https://leetcode.com/problems/sort-colors/description/
# MEDIUM
# Tags: twopointerslc, #75

# GIVEN:
    # an array nums with n objects colored red, white, or blue

# TASK:
    # sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue
    # the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
    # NOTE: solve this problem without using the library's sort function

# EXAMPLES:
    # Input: nums = [2,0,2,1,1,0]
    # Output: [0,0,1,1,2,2]

    # Input: nums = [2,0,1]
    # Output: [0,1,2]

###########################################################################################################

# ✅ ALGORITHM: TWO POINTERS
# set 3 pointers, with variables zero, one, two
# zero, one will point to 0 initially; two points to last element in nums initially
# if one points to a 0:
    # if zero does not point to a zero:
        # swap values of zero and one
        # increment zero and one each by 1
    # else, if zero points to a zero:
        # just increment zero and one each by 1 (no point swapping)
# else if one points to a 1:
    # increment one by 1
# else, if one points to a 2:
    # if two does not point to a 2:
        # swap values of one and two
        # decrement two by 1
    # else, if two points to a 2:
        # just decrement two by 1 (no point swapping)
    # NOTE: when decrementing two, one remains unchanged since it has to analyze the swapped element to determine if further swapping is required with zero

# TIME COMPLEXITY: O(n)
    # we're traversing nums array of length = n once
# SPACE COMPLEXITY: O(1)

def sortColors(nums):
    # initialize the 3 pointers
    zero, one = 0, 0
    two = len(nums)-1

    while one <= two:
        if nums[one] == 0:
            if nums[zero] != 0:
                nums[one], nums[zero] = nums[zero], nums[one] # swap one and zero
            one += 1
            zero += 1
        
        elif nums[one] == 1:
            one += 1
        
        else: # if nums[one] == 2:
            if nums[two] != 2:
                nums[one], nums[two] = nums[two], nums[one] # swap one and two
            two -= 1 # one remains unchanged since it has to analyze the swapped element to determine if further swapping is required with zero