# https://leetcode.com/problems/zigzag-conversion/description/
# MEDIUM
# Tags: stringlc, #6

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    # P   A   H   N
    # A P L S I I G
    # Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows

# EXAMPLES:
    # Input: s = "PAYPALISHIRING", numRows = 3
    # Output: "PAHNAPLSIIGYIR"

    # Input: s = "PAYPALISHIRING", numRows = 4
    # Output: "PINALSIGYAHRPI"
    # Explanation:
    # P     I    N
    # A   L S  I G
    # Y A   H R
    # P     I

    # Input: s = "A", numRows = 1
    # Output: "A"

###########################################################################################################

# ✅ ALGORITHM: INDEX PATTERN
# Some rules and common patterns that can be observed:
    # If rows are numbered 0 to numRows-1, then the 1st character of the resulting string for each row is s[row]
    # To jump to the next character in the row (e.g. 1st row: P -> I), we increment current index by 2*(numRows-1) for the 1st and last rows
        # e.g. for numRows = 4, each increment = 2*(4-1) = 6
            # 0th row: P(0) -> I(6) -> N(12)
            # last (3rd) row: P(3) -> I(9)
    # For the other rows that are not 1st/last rows, there are additional characters in between that we have to add
        # for current index i, the index of the next char in the resulting string = i + 2*(numRows-1) - 2*row

# TIME COMPLEXITY: O(n)
    # n = len(s)
    # even though there is nested for-loop, we are visiting each char only once
# SPACE COMPLEXITY: O(1)

def convert(s, numRows):
    if numRows == 1: return s

    result = "" # return value
    for row in range(numRows):
        increment = 2 * (numRows-1) # no. of jumps to get to the next character in the resulting string
        for i in range(row, len(s), increment): # for loop but instead of increasing by 1, increase by increment
            # we start iterating from i=row instead of i=0 because the 1st element in the ith row is s[i]
            result += s[i]

            if 0 < row < numRows-1 and i + increment - 2*row < len(s): # if current row is not 1st/last row and index of the next char in resulting string is not out of bounds
                result += s[i + increment - 2*row]
    
    return result