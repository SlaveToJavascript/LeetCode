# 1272. Remove Interval
# https://leetcode.com/problems/remove-interval/description/?envType=study-plan-v2&envId=premium-algo-100
# MEDIUM
# Tags: intervalslc, premiumlc, #1272

# A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form [a, b). A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b).
# You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above, where intervals[i] = [ai, bi] represents the interval [ai, bi). You are also given another interval toBeRemoved.
# Return the set of real numbers with the interval toBeRemoved removed from intervals. In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved. Your answer should be a sorted list of disjoint intervals as described above.

# EXAMPLES:
    # Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
    # Output: [[0,1],[6,7]]

    # Input: intervals = [[0,5]], toBeRemoved = [2,3]
    # Output: [[0,2],[3,5]]

    # Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
    # Output: [[-5,-4],[-3,-2],[4,5],[8,9]]

###########################################################################################################

# ✅ ALGORITHM: SWEEP LINE ALGORITHM, ONE PASS
# for each interval in intervals, check if toBeRemoved is on the left/right of interval or found within interval
    # if toBeRemoved is on the left/right of the interval (i.e. no overlap with interval), we can add the whole interval to result
    # else, if toBeRemoved intersects/overlaps with current interval,
        # if toBeRemoved_start falls within current interval, add the left part of the interval to result, i.e. [interval_start, toBeRemoved_start]
        # if toBeRemoved_end falls within current interval, add the right part of the interval to result, i.e. [toBeRemoved_end, interval_end]

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
    # O(n) if result is considered extra space, else O(1)

def removeInterval(intervals, toBeRemoved):
    result = []
    remove_start, remove_end = toBeRemoved

    for start, end in intervals:
        if remove_start > end or remove_end < start: # if toBeRemoved is on the left/right of the interval (i.e. no overlap with interval)
            result.append([start, end]) # add the whole interval to result
        else:
            if remove_start > start:
                result.append([start, remove_start])
            if remove_end < end:
                result.append([remove_end, end])
    
    return result