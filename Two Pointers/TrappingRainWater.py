# https://leetcode.com/problems/trapping-rain-water/
# HARD
# Tags: twopointerslc, #42

# GIVEN:
    # positive integer array, height, where height[i] is the height of the wall at the uth position

# TASK:
    # find the total number of rainwater these walls can trap in between them

# EXAMPLES:
    # Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # Output: 6
    # Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

    # Input: height = [4,2,0,3,2,5]
    # Output: 9

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# MAIN IDEA: at any height[i], the amount of rainwater trapped = min(leftMax, rightMax) - height[i]
    # leftMax = maximum height of rainwater on the left of i
    # rightMax = maximum height of rainwater on the right of i

# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(1)

def trap(height):
    total_trapped = 0 # return value

    # leftMax and rightMax tracks the maximum height on the left and right of i respectively
    leftMax = 0 # leftMax is initialized to 0 for the 1st element
    rightMax = max(height) # rightMax initialized to the maximum element in height

    for i in range(len(height)):
        if i > 0: # if i is not the 1st element
            leftMax = max(height[:i]) # maximum height on the left of i
        if i < len(height)-1: # if i is not the last element
            rightMax = max(height[i+1:]) # maximum height on the right of i

        trapped = min(rightMax, leftMax) - height[i] # rainwater trapped at current height[i]
        total_trapped += trapped if trapped > 0 else 0 # if current trapped <= 0, no rainwater is trapped; else, update total rainwater tracked
    
    return total_trapped

#==========================================================================================================

# ✅ ALGORITHM 2: TWO POINTERS
# MAIN IDEA: at any height[i], the amount of rainwater trapped = min(leftMax, rightMax) - height[i]
# 2 pointers l and r, at the start and end of height array respectively
# we use leftMax = height[l], rightMax = height[r]
    # we don't actually need to find the real max heights on the left and right of i, since we only need the MINIMUM of the 2
    # therefore we don't care how big the bigger value is, since we only care about the minimum
# while l < r:
    # shift the pointer which has the lower height
        # this is because by incrementing only the pointer with the min height each time, we don't have to compute max height on the left and right for every height[i]
    # calculate the trapped water in the new position where the pointer shifted to
        # e.g. for l += 1 :
        # pointer shifts before we compute the rainwater trapped in the l+1th position, since height at previous value of l before shifting (which was the minimum value between the 2 pointers) was the wall, and we have to calculate water trapped at position l+1
        # also, the lst and last walls are boundaries -> no water can be trapped in those positions
    # update the leftMax value if the value at l+1 is greater than existing leftMax
    # add trapped water at current position to total trapped water
# return total trapped water

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def trap(height):
    l, r = 0, len(height)-1 # l and r initialized to 1st and last element of height respectively
    leftMax, rightMax = height[l], height[r]
    total_trapped_water = 0 # this is our return value

    while l < r: # this is our looping condition since l and r are slowly moving towards each other
        if height[l] < height[r]: # we find out which pointer has the smaller height, and shift that pointer
            l += 1 # we are calculating water trapped at l+1 since l is the wall
            trapped_water = leftMax - height[l] # this follows the formula "amount of water trapped at height[i] = min(leftMax, rightMax) - height[l]"; we know min(leftMax, rightMax) is leftMax here, and height[l] is the position whose rainwater we are trying to compute
            leftMax = max(leftMax, height[l]) # since pointer is shifted, we update leftMax if height at new position is greater than existing leftMax
        else: # if leftMax = rightMax, doesn't matter which one we move
            r -= 1
            trapped_water = rightMax - height[r]
            rightMax = max(rightMax, height[r])
        
        total_trapped_water += trapped_water if trapped_water > 0 else 0 # if trapped_water is positive, add trapped water at position after shifting to total trapped water; else, no water is trapped (add 0)
    return total_trapped_water