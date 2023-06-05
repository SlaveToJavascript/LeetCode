# https://leetcode.com/problems/excel-sheet-column-number/

# GIVEN:
    # string columnTitle that represents the column title as appears in an Excel sheet

# TASK:
    # return its corresponding column number
    # e.g.
    # A -> 1
    # B -> 2
    # C -> 3
    # ...
    # Z -> 26
    # AA -> 27
    # AB -> 28 
    # ...

###########################################################################################################

# Algorithm:
# To get number that each individual char is mapped to, use ord(char)-64
# Formula for getting BCD (e.g.):
    # start from last char to 1st char, i.e. D (4) -> C (3) -> B (2) = 4 * 26^0 + 3 * 26^1 + 2 * 26^2

def titleToNumber(columnTitle):
    result = 0
    for idx, char in enumerate(columnTitle[::-1]):
        result += (ord(char)-64) * 26**idx
    return result