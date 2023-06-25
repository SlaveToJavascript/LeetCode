# https://leetcode.com/problems/container-with-most-water/description/

# GIVEN:
    # integer array height of length n containing the heights of n walls

# TASK:
    # Find two lines that together with the horizontal axis form a container,
    # such that the container contains the most water

# RETURN:
    # the maximum amount of water a container can store (height x width)

# EXAMPLES:
    # Input: height = [1,8,6,2,5,4,8,3,7]
    # Output: 49
    # Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
    # In this case, the max area of water (blue section) the container can contain is 49.

    # Input: height = [1,1]
    # Output: 1

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# Nested for-loop by getting area of every height x every other height

# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(n)

def maxArea(height):
    max_area = 0
    for left in range(len(height)):
        for right in range(left+1, len(height)):
            max_area = max(max_area, (right-left)*min(height[left], height[right]))
    return max_area

#==========================================================================================================

# ✅ ALGORITHM 2: TWO POINTERS
# Set left pointer as 1st element in heights, set right pointer as last element in heights
# Set max_area = 0
# while left < right, get area
    # if area < max_area, update max_area
    # if height[left] < height[right], move left to the right (i.e. left +1);
    # else, move right to the left (i.e. right -1)
        # rationale: if we shift pointer with lower height, the area might increase if next wall is taller
        # but if we shift pointer with taller height, area cannot possibly increase as area = min height x width!

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def maxArea(height):
    max_area = 0
    left, right = 0, len(height)-1 # initialize two pointers

    while left < right:
        max_area = max(max_area, (right-left)*min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area