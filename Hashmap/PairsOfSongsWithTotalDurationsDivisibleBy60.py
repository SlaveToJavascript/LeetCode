# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/

# GIVEN:
    # integer array time, where time[i] represents the duration of the ith song

# TASK:
    # Return the number of pairs of songs for which their total duration in seconds is divisible by 60
    # Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0

# EXAMPLES:
    # Input: time = [30,20,150,100,40]
    # Output: 3
    # Explanation: Three pairs have a total duration divisible by 60:
    # (time[0] = 30, time[2] = 150): total duration 180
    # (time[1] = 20, time[3] = 100): total duration 120
    # (time[1] = 20, time[4] = 40): total duration 60

    # Input: time = [60,60,60]
    # Output: 3
    # Explanation: All three pairs have a total duration of 120, which is divisible by 60

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# Get every pair of elements from array and check if their sum is divisible by 60

# TIME COMPLEXITY: O(n^2) ❌
# SPACE COMPLEXITY: O(1)

def numPairsDivisibleBy60(time):
    counter = 0
    for i in range(len(time)-1):
        for j in range(i+1, len(time)):
            if (time[i] + time[j]) % 60 == 0:
                counter += 1
    return counter

#==========================================================================================================

# ✅ ALGORITHM 2: HASHMAP
# Formula to use: for a given integer i, i%60 + x%60 = 60, where x is the number to be found (i.e. x+i is a multiple of 60)
    # => x%60 = 60 - i%60

def numPairsDivisibleBy60(time):
    remainders = {}
    for t in time:
        remainder = t % 60
        if remainder in remainders:
            remainders[remainder] += 1
        else:
            remainders[remainder] = 1
    