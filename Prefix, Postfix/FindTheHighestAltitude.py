# 1732. Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/
# EASY
# Tags: prefixlc, leetcode75lc, lc75lc, #1732

# GIVEN:
    # an integer array, gain, of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1
    # start from an altitude of 0

# TASK:
    # Return the highest altitude of a point

# EXAMPLES:
    # Input: gain = [-5,1,5,0,-7]
    # Output: 1
    # Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

    # Input: gain = [-4,-3,-2,-1,4,3,2]
    # Output: 0
    # Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

###########################################################################################################

# ✅ ALGORITHM: PREFIX SUMS

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def largestAltitude(gain):
    curr = 0 # current altitude ; start from 0
    max_altitude = 0
    
    for g in gain:
        curr += g
        max_altitude = max(max_altitude, curr)
    
    return max_altitude