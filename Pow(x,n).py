# https://leetcode.com/problems/powx-n/description/
# MEDIUM
# Tags: divideconquerlc, #50

# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n)

# EXAMPLES:
    # Input: x = 2.00000, n = 10
    # Output: 1024.00000

    # Input: x = 2.10000, n = 3
    # Output: 9.26100

    # Input: x = 2.00000, n = -2
    # Output: 0.25000
    # Explanation: 2-2 = 1/22 = 1/4 = 0.25

###########################################################################################################

# ✅ ALGORITHM: DIVIDE AND CONQUER
# Base cases:
    # any number x in x^0 will always be 1
    # any number n in 0^n will always be 0
# MAIN RULES/IDEA:
    # pow(x, n) = pow(x, n/2) * pow(x, n/2), if n is an even number
    # pow(x, n) = pow(x, n//2) * pow(x, n//2) * x, if n is an odd number
    # if n is negative, pow(x, -n) = 1/pow(x, n)

# TIME COMPLEXITY: O(log n)
    # we divide n by 2 each time -> number of divisions = O(log_2 n)

def myPow(x, n):
    def power(x, n): # when calling this function, we always use positive value of n, i.e. abs(n)
        # base cases:
        if x == 0: return 0
        if n == 0: return 1

        result = power(x, n//2)
        result *= result # i.e. result = power(x, n//2) * power(x, n//2)
        return result if n % 2 == 0 else result * x # if n is even, return result; else, return result * x
    
    result = power(x, abs(n))
    return result if n > 0 else 1/result