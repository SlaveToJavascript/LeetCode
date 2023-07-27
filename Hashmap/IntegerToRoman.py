# https://leetcode.com/problems/integer-to-roman/description/
# MEDIUM
# Tags: hashmaplc

# GIVEN:
    # an integer, num

# TASK:
    # Convert it to a Roman numeral string and return it
    # Roman numerals are usually written largest to smallest from left to right
    # However, the numeral for four is not IIII. Instead, the number four is written as IV.
        # Because the one is before the five we subtract it making four
    # The same principle applies to the number nine, which is written as IX. 

    # There are six instances where subtraction is used:
        # I can be placed before V (5) and X (10) to make 4 and 9. 
        # X can be placed before L (50) and C (100) to make 40 and 90. 
        # C can be placed before D (500) and M (1000) to make 400 and 900.

# EXAMPLES:
    # Input: num = 3
    # Output: "III"
    # Explanation: 3 is represented as 3 ones.

    # Input: num = 58
    # Output: "LVIII"
    # Explanation: L = 50, V = 5, III = 3.

    # Input: num = 1994
    # Output: "MCMXCIV"
    # Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

###########################################################################################################

# ✅ ALGORITHM 1: HASHMAP (my solution - unoptimized)
# Create hashmap of integer to Roman numeral mappings
# Start iterating string num from the back to front
# As we iterate, new Roman numeral characters obtained for num[i] will be added to the front of the existing string (since we iterate from back to front)

# TIME COMPLEXITY: O(n)
    # n is the length of str(num)
# SPACE COMPLEXITY: O(1) + dictionary

def intToRoman(num):
    hm = { # hashmap of integer to Roman numeral mappings
        1:'I',
        5:'V',
        10:'X',
        50:'L',
        100:'C',
        500:'D',
        1000:'M'
    }

    roman = "" # return value; this is the resulting Roman numeral string we want
    num = str(num) # convert num to string number

    multiply = 1 # this is the x's place of the ith character in string num, e.g. if num = 1234, then 3 is at the 10's place, 2 is at the 100's place, 4 is at the 1's place, etc.
    for i in range(len(num)-1, -1, -1): # iterate string num from the back
        if num[i] == "0": # if ith digit of num is 0, we skip current iteration and move to the i-1th place
            multiply *= 10
            continue
        
        curr_num = int(num[i]) * multiply # e.g. if num = 9876, i is at 3rd digit, then curr_num = 30
        if int(num[i]) in (4,9): # if curr_num starts with 4 or 9
            second_char = hm[curr_num + multiply] # 2nd char is mapping for either 5xxx or 10xxx
            first_char = hm[multiply] # 1st char is the mapping for the no. subtracted from 2nd char to get curr_num
            roman = first_char + second_char + roman # add the 2 chars to the front of the string roman
        else: # if curr_num doesn't start with 4 and 9
            if curr_num in hm: # if curr_num already in mapping,
                roman = hm[curr_num] + roman # add the mapping to roman string
            else: # if curr_num not in in mapping,
                curr_roman = "" # the new string mapped to curr_num which is to be added to roman 
                if int(num[i]) > 5: # if curr_num starts with 6 or 7 or 8
                    curr_num -= 5 * multiply # e.g. if curr_num = 80, subtract 50 in this step
                    curr_roman = hm[5 * multiply] # add the mapping for the subtracted number to curr_roman
                curr_roman = curr_roman + curr_num / multiply * hm[multiply] # add the mapping for the remaining curr_num (after subtraction) to curr_roman
                roman = curr_roman + roman # add curr_roman to resulting string
        
        multiply *= 10 # multiply the x's place for the next iteration

    return roman

#==========================================================================================================

# ✅ ALGORITHM 2: MANUALLY CREATE NEW PAIRS OF MAPPINGS FOR EDGE CASES

def intToRoman(num):
    # use 2D list instead of hashmap to preserve ascending order
    symList = [ ["I", 1], 
                ["IV", 4], 
                ["V", 5], 
                ["IX", 9]
                ["X" , 10], 
                ["XL", 40],
                ["L", 50],
                ["XC", 90], 
                ["C", 100],
                ["CD", 400], 
                ["D", 500], 
                ["CM", 900],
                ["M", 1000]
    ]

    result = ""

    for symbol, value in reversed(symList):
        if num // value: # if num = 400 and value = 1000, 400//1000 = 0 which means the mapping for M (1000) would not be in result; but if num // value > 0, it means the M symbol should be added to result by num // value times
            count = num // value
            result += count * symbol
            num %= value # e.g. gets the remainder of num after removing the character before it
    
    return result