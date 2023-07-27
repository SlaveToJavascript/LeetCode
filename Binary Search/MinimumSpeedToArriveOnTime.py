# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description/
# MEDIUM

# GIVEN:
    # a decimal number, hour, representing the amount of time you have to reach the office
    # integer array, dist, where dist[i] = distance of the ith train ride
        # you need to take all trains in dist (in sequential order) to reach the office

# TASK:
    # Each train can only depart at an integer hour, so you may need to wait in between each train ride
        # e.g. if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before departing on the 2nd train ride at the 2 hour mark
    # Return the minimum positive integer, speed, that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time
    # NOTE: the answer, speed, will not exceed 10^7

# EXAMPLES:
    # Input: dist = [1,3,2], hour = 6
    # Output: 1
    # Explanation: At speed 1:
    # - The first train ride takes 1/1 = 1 hour.
    # - Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
    # - Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
    # - You will arrive at exactly the 6 hour mark.

    # Input: dist = [1,3,2], hour = 2.7
    # Output: 3
    # Explanation: At speed 3:
    # - The first train ride takes 1/3 = 0.33333 hours.
    # - Since we are not at an integer hour, we wait until the 1 hour mark to depart. The second train ride takes 3/3 = 1 hour.
    # - Since we are already at an integer hour, we depart immediately at the 2 hour mark. The third train takes 2/3 = 0.66667 hours.
    # - You will arrive at the 2.66667 hour mark.

    # Input: dist = [1,3,2], hour = 1.9
    # Output: -1
    # Explanation: It is impossible because the earliest the third train can depart is at the 2 hour mark.

###########################################################################################################

# ✅ ALGORITHM 1: BINARY SEARCH
# MAIN IDEA: if at a certain speed s, we can reach in time, then we only need to check for speeds < s if any lower speed can also reach in time
    # We don't care about any speeds > s, since we want to find the minimum speed (i.e. lowest value of s that can reach in time)

# BINARY SEARCH:
    # since max value of speed = 10^7, we perform binary search from 1 to 10^7 to find speeds than can let us reach in time
    # if certain speed s can reach in time, we look at the top half (s = 1 to s-1) to find a lower speed that can also reach in time
    # else, if a certain speed s cannot reach in time, we look at the bottom half (s = s+1 to 10^7) to find a higher speed that can reach in time
    # if there is no such speed that can let us reach in time, return -1

# TIME COMPLEXITY: O(n log 10^7), where n = len(dist)
    # O(n) is for the time_required() function which iterates once through dist array
    # 10^7 is the size of the search space which we are reducing at each step
# SPACE COMPLEXITY: O(1)
    # no extra space needed except the 3 variables

import math

def minSpeedOnTime(dist, hour):
    # function to calculate time needed to finish riding all buses in dist with given speed
    def time_needed(speed, dist):
        time = 0
        for d in dist[:-1]: # remember we only need to round up the train ride time if we are not at the last train
            time += math.ceil(float(d) / speed) # in Python 2, if we do d/speed instead of float(d)/speed or d/float(speed), we will only get a truncated integer (e.g. 2/5 = 2)
        time += float(d) / speed # remember to add back the time taken on the last train; we don't need to round up for this as we don't need to wait for any next trains
        return time
    
    l, r = 1, 10**7 # lower and upper pointers
    min_speed = -1 # this is the return value, i.e. the lowest speed we need to reach on time; we initialize to -1 in case we can't find any speeds where we can reach on time

    while l <= r:
        mid = (l + r) // 2 # this is the speed we're checking which is in the middle of our search space
        
        if time_needed(mid, dist) <= hour: # if we are able to reach in time at speed = mid,
            min_speed = mid # we update min_speed to mid
            r = mid - 1 # update our upper boundary pointer to mid-1 so our new search space is between 1 and mid-1, as we want to find a lower speed that can also make it
            
        else: # we cannot reach in time, so we have to find a higher speed in the right half of search space
            l = mid + 1
    
    return min_speed