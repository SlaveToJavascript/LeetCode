# https://leetcode.com/problems/excel-sheet-column-title/
# MEDIUM
# Tags: stringlc, #168

# GIVEN:
    # an integer columnNumber

# TASK:
    # return its corresponding column title as it appears in an Excel sheet
    # For example:
        # A -> 1
        # B -> 2
        # C -> 3
        # ...
        # Z -> 26
        # AA -> 27
        # AB -> 28 
        # ...

# EXAMPLES:
    # Input: columnNumber = 1
    # Output: "A"

    # Input: columnNumber = 28
    # Output: "AB"

    # Input: columnNumber = 701
    # Output: "ZY"

###########################################################################################################

# ✅ ALGORITHM:
# To get each character of the resulting string in reverse,
# keep dividing columnNumber-1 by 26 -> remainder + ASCII A is the ASCII of the character we want

# TIME COMPLEXITY: O(log_26 n)
    # on each iteration of for-loop, we're 

def convertToTitle(columnNumber):
    result = "" # return value
    while columnNumber > 0:
        remainder = (columnNumber-1) % 26
        result += chr(ord('A') + remainder) # ASCII of A + remainder = ASCII of char we want
        columnNumber = (columnNumber-1) // 26 # update column number after getting the previous char
    
    return result[::-1] # above, each char of the resulting string was obtained in reverse -> return reverse of the string obtained