# https://leetcode.com/problems/jump-game/description/
# MEDIUM
# Tags: dplc, greedylc, #55

# GIVEN:
    # a positive integer array, nums

# TASK:
    # You are initially positioned at the array's first element
    # each element in the array represents the maximum no. of jumps you can take from that element
    # Return true if you can reach the last index, or false otherwise

# EXAMPLES:
    # Input: nums = [2,3,1,1,4]
    # Output: true
    # Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

    # Input: nums = [3,2,1,0,4]
    # Output: false
    # Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

###########################################################################################################

# ✅ ALGORITHM 1: GREEDY (my solution - not optimized)
# Initiate current index to 0
# While current index is before the last element,
    # get the array of possible positions to jump to
        # e.g. if nums = [2,3,1,1,4], and current index is 0 (i.e. we are at 2), the array of possible positions to jump to is [3,1] since we can jump once (land on 3) or jump twice (land on 1)
    # for each element in this array, calculate the sum of itself + the no. of jumps it takes to get to itself
        # e.g. continuing from above example, we take 1 jump to land on 3 and 2 jumps to land on 1 -> the array changes from [3,1] to [3+1,1+2] = [4,3]
    # if this array is empty, we are stuck at a place before the last element but there are no more jumps to take -> return False
    # get the maximum value from the above array, and find the index of this maximum value in the above array + 1 -> that would be the no. of jumps to take
    # increase current index with the no. of jumps
# return True, because at this point, current index would be at last element or past it

# TIME COMPLEXITY: O(n^2) worst case
    # the while loop takes O(n) time
    # the for loop within the while loop takes O(n) time in the worst case (when the jumps array's length = nums array length)
# SPACE COMPLEXITY: O(n^2) worst case
    # for every while loop iteration, we are creating a new array whose length = nums array's length in the worst case

def canJump(nums):
    idx = 0 # this is the current index we are at in the nums array

    while idx < len(nums)-1: # while idx is before the last element in nums array
        # get the array of next possible positions to jump to (between 1 jump to idx+nums[idx] no. of jumps)
        jumps = nums[idx+1 : idx+nums[idx]+1]

        for i in range(len(jumps)):
            jumps[i] += i+1 # if it takes x jumps to land on jumps[i], then jumps[i] = x+jumps[i]
            # this is to get the maximum possible next jump factoring in the no. of jumps needed to get there
        
        if not jumps: return False # if there are no more places to jump to, it means we are stuck within the nums array and cannot reach the end

        jumps_to_take = jumps.index(max(jumps)) + 1 # max no. of jumps to take is the index of the max element in jumps array (+1 is because indexing is 0-based)
        idx += jumps_to_take # update current index after taking these no. of jumps
    
    return True # at this point, current index is equal to or greater than last index of nums

#==========================================================================================================

# ✅ ALGORITHM 2: OPTIMIZED GREEDY FROM BACK OF ARRAY
# Instead of starting from the first element of the array, we start from the end and make sure the element(s) in front of it can reach it
# e.g. if nums = [2,3,1,2,4], we set our goal to 4, then check if the element before it (2) can reach 4 -> since 2 can reach 4 (since it can take 1 step), we move our goal to 2 -> we check if 1 can reach 2 (yes it can) -> ... -> if goal becomes at index 0, that means we managed to reach goal from the 1st element of the array

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def canJump(nums):
    goal = len(nums)-1 # goal initialized to the index of the last element in nums
    
    for i in range(goal-1, -1, -1): # we start from element before goal and iterate from back to front
        if i + nums[i] >= goal: # i is the index of the origin of our jump, and nums[i] is the max no. of steps we can take
            goal = i # we shift the goal forward, since i is able to access goal
    
    return goal == 0 # goal needs to be 0 since we start jumping from 0

#==========================================================================================================

# ✅✅ ALGORITHM 3: OPTIMIZED GREEDY FROM FRONT OF ARRAY
# When iterating nums array, we keep track of only the max no. of jumps we can take at each element

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def canJump(nums):
    max_jumps = nums[0] # we initialize max possible no. of jumps to the 1st element

    for i in range(1, len(nums)):
        if max_jumps == 0: return False # there are no jumps we can take
        max_jumps -= 1 # we are taking 1 jump here, so max_jumps reduces by 1
        max_jumps = max(max_jumps, nums[i]) # max possible no. of jumps we can take is either the existing max_jumps value or nums[i], whichever is greater
    
    return True # if no False is returned and the for-loop finishes iterating, it means we reached the last element