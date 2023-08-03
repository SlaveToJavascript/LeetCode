# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# MEDIUM
# Tags: backtracklc, #17

# GIVEN:
    # a string containing digits from 2-9 inclusive

# TASK:
    # return all possible letter combinations that the number could represent
    # Return the answer in any order
    # A mapping of digits to letters (just like on the telephone buttons) is given

# EXAMPLES:
    # Input: digits = "23"
    # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    # Input: digits = ""
    # Output: []

    # Input: digits = "2"
    # Output: ["a","b","c"]

###########################################################################################################

# ✅ ALGORITHM: BACKTRACKING
# Once the string built is of the same length as digits, we can add it to result array

# TIME COMPLEXITY: O(n * 4^n), n = length of integer string
    # on average, it should be 3^n, but since 7 and 9 are mapped to 4 digits each, the worst case complexity is 4^n
    # 4^n for building every possible string combination * n to form the string by joining each character
# SPACE COMPLEXITY: O(n)
    # the max recursion depth will be n, where n is the length of input string
    # If the space required for ans is considered as well, the complexity will be O(4^n)

def letterCombinations(digits):
    hm = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    result = []

    def backtrack(i, curr_string): # i = the current index in digit string
        if len(curr_string) == len(digits): # if current string's length becomes the same as length of digits string,
            result.append(curr_string) # add to results array
            return
        
        for char in hm[digits[i]]: # for every character that current digits[i] can be mapped to,
            backtrack(i + 1, curr_string + char) # build current string and move to the next digit
    
    if digits: # this line exists because of the edge case where digits = ""
        backtrack(0, "")
    
    return result