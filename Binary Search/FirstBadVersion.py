# https://leetcode.com/problems/first-bad-version/description/?envType=study-plan&id=algorithm-i

# GIVEN:
    # n, an integer no. of versions
        # the first x number of versions are good, the rest behind are bad
    # isBadVersion(version), a function that returns whether a version is bad

# TASK:
    # return the integer no. of the first bad element (i.e. the first True returned from isBadVersion())
    # Reduce the number of calls to the isBadVersion(version) function

# EXAMPLES:
    # Input: n = 5, bad = 4
    # Output: 4
    # Explanation:
    # call isBadVersion(3) -> false
    # call isBadVersion(5) -> true
    # call isBadVersion(4) -> true
    # Then 4 is the first bad version.

    # Input: n = 1, bad = 1
    # Output: 1

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# Call isBadVersion() on each version until the first True is encountered

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def firstBadVersion(n):
    for version in range(1, n):
        if isBadVersion(version):
            return version

#============================================================================================================

# ✅ ALGORITHM 2: BINARY SEARCH
# If mid is a good version (i.e. isBadVersion() = False), the bad version lies in 2nd half AFTER mid
    # => lower = mid+1 (+1 because AFTER mid)
# If mid is a bad version (i.e. isBadVersion() = True), the bad version lies in 1st half incl. mid
    # => upper = mid

# TIME COMPLEXITY: O(log n) for binary search
# SPACE COMPLEXITY: O(1)

def firstBadVersion(n):
    lower = 1
    upper = n
    while lower < upper:
        mid = lower + (upper-lower)//2
        if isBadVersion(mid):
            upper = mid
        else:
            lower = mid+1
    return lower