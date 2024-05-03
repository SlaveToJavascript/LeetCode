# 165. Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers/
# MEDIUM
# Tags: stringlc, arraylc, #165

# Given 2 version numbers, version1 and version2, compare them.
    # Version numbers consist of one or more revisions joined by a dot '.'
    # Each revision consists of digits and may contain leading zeros. Every revision contains at least one character.
    # Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on
        # For example 2.5.33 and 0.1 are valid version numbers.
# To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.
# Return the following:
    # If version1 < version2, return -1.
    # If version1 > version2, return 1.
    # Otherwise, return 0.

# EXAMPLES:
    # Input: version1 = "1.01", version2 = "1.001"
    # Output: 0
    # Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

    # Input: version1 = "1.0", version2 = "1.0.0"
    # Output: 0
    # Explanation: version1 does not specify revision 2, which means it is treated as "0".

    # Input: version1 = "0.1", version2 = "1.1"
    # Output: -1
    # Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.

###########################################################################################################

# ✅ ALGORITHM: SPLIT INTO ARRAY AND COMPARE EACH SEGMENT FROM LEFT TO RIGHT
# 1. split each version no. into array of segments
# 2. if one version no. has less segments than the other, add ".0" to the shorter version no. until it's the same length as the longer version no.
# 3. iterate the corresponding segments from left to right, and return -1/1/0 depending on whether the segment is greater/less/equal to the corresponding segment of the other version no.

# TIME COMPLEXITY: O(m+n)
    # where m and n are the lengths of version1 and version2, respectively
# SPACE COMPLEXITY: O(n)
    # n = max no. of segments in the split version strings

def compareVersion(version1, version2):
    v1, v2 = version1.split('.'), version2.split('.') # v1 and v2 are arrays of the respective version strings
    n = max(len(v1), len(v2))
    
    # if one version no. has less segments than the other, add "0" segments to the shorter version no. until it's the same length as the longer version no.
    v1 += (n-len(v1)) * ['0']
    v2 += (n-len(v2)) * ['0']

    for i in range(min(len(v1), len(v2))):
        # NOTE: int("0001") = 1
        if int(v1[i]) > int(v2[i]):
            return 1
        elif int(v1[i]) < int(v2[i]):
            return -1
    
    return 0