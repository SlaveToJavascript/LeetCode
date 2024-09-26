# https://leetcode.com/problems/roman-to-integer/
# EASY
# Tags: hashmaplc

# GIVEN:
    # a Roman numeral string, s

# TASK:
    # Convert it to an integer and return it
    # Roman numerals are usually written largest to smallest from left to right
    # However, the numeral for four is not IIII. Instead, the number four is written as IV.
        # Because the one is before the five we subtract it making four
    # The same principle applies to the number nine, which is written as IX. 

    # There are six instances where subtraction is used:
        # I can be placed before V (5) and X (10) to make 4 and 9. 
        # X can be placed before L (50) and C (100) to make 40 and 90. 
        # C can be placed before D (500) and M (1000) to make 400 and 900.

# EXAMPLES:
    # Input: s = "III"
    # Output: 3
    # Explanation: III = 3.

    # Input: s = "LVIII"
    # Output: 58
    # Explanation: L = 50, V= 5, III = 3.

    # Input: s = "MCMXCIV"
    # Output: 1994
    # Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

###########################################################################################################

# ✅ ALGORITHM 1: HASHMAP
# For every pair of consecutive letters, if the 1st letter is smaller than the next, it represents subtraction (i.e. subtract the 1st letter and add 2nd letter)
# Else, both letters are added

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1) + dictionary

def romanToInt(s): # 1 <= s <= 3999
    hm = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0

    for i in range(1, len(s)): # i iterates from 2nd element
        if hm[s[i-1]] < hm[s[i]]: # if the value of the 1st letter is smaller than the next, it represents subtraction of the 1st letter (e.g. CM = 1000-100 = 900)
            result -= hm[s[i-1]]
        else:
            result += hm[s[i-1]]
    
    # after for loop finishes, remember to add the last digit
    result += hm[s[-1]]
    return result