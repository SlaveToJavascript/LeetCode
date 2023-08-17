# https://leetcode.com/problems/palindrome-number/
# EASY
# Tags: stringlc, #9

# GIVEN:
    # integer x

# TASK:
    # check if x is a palindrome
    # return True if x is a palindrome, False otherwise

###########################################################################################################

# ✅ ALGORITHM 1: CONVERT NUMBER TO STRING

# Time complexity: O(1)
# Space complexity: O(n) since additional space required for the string of x

def isPalindrome(x):
    return str(x) == str(x)[::-1]

#==========================================================================================================

# ✅ ALGORITHM 2: DO NOT CONVERT NUMBER TO STRING
# Algorithm:
    # Reverse last half of the number and compare it with the first half
    # If they are equal, then True; else, False

# Time complexity: O(log(n)) since we are dividing x by 10 for every iteration
# Space complexity: O(1), no additional space required

def isPalindrome(x):
    # EDGE CASES:
        # Negative numbers will always be False
        # If x == 0, always True
        # 0 < x < 10 will always be True
        # If x is divisible by 10, always False
    if x < 0: # negative numbers can never be palindromes
        return False
    if x < 10: # one-digit numbers (e.g. 9) will always be same from front and back
        return True
    if x % 10 == 0: # round numbers (ending with 0, divisible by 10) are never palindromes
        return False
    reversed = 0
    while x > reversed: # when the reversed x is >= original x, stop
        reversed = reversed * 10 + x % 10 # reversed keeps adding last digit of x to reversed x e.g. if x = 123: 3, then 32, then 321
        x = x // 10 # remove the last digit from x
    return x == reversed or x == reversed // 10 # x == reversed // 10 is for x with odd no. of digits