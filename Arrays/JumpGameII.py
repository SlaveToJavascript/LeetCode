# https://leetcode.com/problems/jump-game-ii/description/
# MEDIUM
# dplc, #45

# GIVEN:
    # a positive integer array, nums

# TASK:
    # You are initially positioned at nums[0]
    # Each element nums[i] represents the maximum length of a jump you can take from index i
        # e.g. for nums = [2,3,1,1,4], we can jump 0/1/2 steps from nums[0] -> land on 3 or 1
    # Return the minimum number of jumps to reach the last element in nums
    # NOTE: it is definitely possible to jump to the last element in nums

# EXAMPLES:
    # Input: nums = [2,3,1,1,4]
    # Output: 2
    # Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

    # Input: nums = [2,3,0,1,4]
    # Output: 2
    # Explanation: 2 -> 3 (1 step), 3 -> 4 (3 steps) => 2 jumps in total

###########################################################################################################

# ✅ ALGORITHM 1: GREEDY
# MAIN IDEA: maintain l and r pointers to denote the indexes of the boundary where the current number can jump to
# There will be several boundaries within nums -> min. no. of jumps needed is equal to the no. of jumps needed to get from the first boundary to the last
# Once the last element of nums falls within this boundary, it means the last element of nums is reachable -> end the iteration

# e.g. for nums = [2,3,1,1,4],
# the boundaries are: [2],[3,1],[1,4]
    # [2] can jump to anywhere within [3,1] -> boundary is [3,1]
    # [3,1] can jump to anywhere within [1,4] -> boundary is [1,4]
# to jump from [2] -> [3,1] -> [1,4] takes 2 jumps

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def jump(nums):
    l = r = 0 # the 1st boundary will start and end at the first element
    jumps_count = 0 # this is the value we return

    while r < len(nums)-1: # while the last element in nums is not within current boundary
        furthest = 0 # this will be the furthest possible index any element in current boundary can jump to
        
        for i in range(l, r+1): # iterate within the boundary to get the ending index of the next boundary
            furthest = max(furthest, nums[i] + i) # nums[i] + i is the furthest index that nums[i] can jump to
        
        jumps_count += 1 # we make a jump to the next boundary
        
        l = r + 1 # the start of the next boundary is 1 element after the end of current boundary
        r = furthest # the end of the next boundary is the furthest index any element in current boundary can jump to

    return jumps_count # at this point, the last element in nums is within the boundary -> return jumps_count