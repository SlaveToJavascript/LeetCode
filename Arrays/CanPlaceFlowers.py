# https://leetcode.com/problems/can-place-flowers/description/
# EASY
# Tags: arraylc, leetcode75lc, lc75lc, #605

# GIVEN:
    # an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
    # and an integer n (number of new flowers to be planted)

# TASK:
    # check if n new flowers can be planted in flowerbed
    # NOTE: flowers cannot be planted in adjacent plots!

# RETURN:
    # True if n new flowers can be planted in flowerbed, False otherwise

# EXAMPLES:
    # Input: flowerbed = [1,0,0,0,1], n = 1
    # Output: true

    # Input: flowerbed = [1,0,0,0,1], n = 2
    # Output: false

###########################################################################################################

def canPlaceFlowers(flowerbed, n):
    f = 0 # pointer for flowerbed array
    while n > 0 and f < len(flowerbed): # while there are more flowers to be placed, and f is not out of bounds,
        left_empty = (f == 0) or (flowerbed[f-1] == 0) # left spot is empty
        right_empty = (f == len(flowerbed)-1) or (flowerbed[f+1] == 0) # right spot is empty
        if flowerbed[f] == 0 and left_empty and right_empty: # if current, left and right spots are empty
            flowerbed[f] = 1 # plant flower here
            n -= 1 # reduce remaining flowers to be planted by 1
        f += 1 # mmove t the next spot
    return n == 0 # if n = 0, all flowers have been planted