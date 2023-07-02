# https://leetcode.com/problems/count-primes/description/
# MEDIUM

# GIVEN:
    # an integer n, return the number of prime numbers that are less than n

###########################################################################################################

# ALGORITHM: SIEVE OF ERATOSTHENES
# create a boolean array (seen) of size n to represent each of the numbers less than n
# start at 2 and for each no., mark each multiple of num as False (i.e. non-prime), starting at num^2
    # start at num^2 bc every multiple up to the num'th multiple will have been guaranteed to have been seen before, since they're also a multiple of a smaller no.
    # e.g. when processing 5s, we can skip to 25 because 10 will have been seen when we processed 2s, 15 when we processed 3s, and 20 when we processed 2s
# Then move num forward, skipping any numbers that have already been seen
    # By doing this, we will only stop on prime no.s, because they haven't been seen as a multiple of a previous iteration
    # We just have to update our count (ans) each time we stop and then return ans once we reach n

def countPrimes(n):
    seen = [False] * n
    ans = 0
    for num in range(2, n):
        if seen[num]: continue # if True, num is not prime -> skip current iteration
        ans += 1
        seen[num*num:n:num] = [True] * ((n - 1) // num - num + 1) # mark multiples of num as primes
    return ans