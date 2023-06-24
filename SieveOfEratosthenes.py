# SIEVE OF ERATOSTHENES
# Main idea:
    # To get all prime numbers less than n,
    # Make a boolean array of size n; the booleans will tell us if the numbers are prime or not
    # Initially, everything is set to true; go through all numbers and mark non-prime no.s False
        # 1) 2 is marked True -> Mark all multiples of 2 that are > 2 as False
        # 2) 3 is marked True -> Mark all multiples of 3 that are > 3 as False
        # 3) 4 is marked False (fromt step 1 above) -> skip
        # 4) 5 is marked True -> Mark all multiples of 5 that are > 5 as False
        # ...

# Time complexity: O(n log(log n))

from math import isqrt

def primes_less_than(n):
    if n <= 2:
        return []
    
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, isqrt(n)): # optimization: a non-prime no. has a least 2 factors; at least 1 of them must be > sqrt(n)
        if is_prime[i]: # e.g. 2
            for x in range(i**2, n, i): # optimization: if a factor < i, it should already have been marked out by previous iteration of the loop -> can start with multiples of i that are >= i**2
                is_prime[x] = False # e.g. mark all multiples of x as not prime
    
    return [i for i in range(n) if is_prime[i]] # returns integer array of all prime no.s less than n