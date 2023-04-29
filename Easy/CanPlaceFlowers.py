# https://leetcode.com/problems/can-place-flowers/description/

# GIVEN:
    # an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
    # and an integer n (number of new flowers to be planted)

# TASK:
    # check if n new flowers can be planted in flowerbed
    # NOTE: flowers cannot be planted in adjacent plots!

# RETURN:
    # True if n new flowers can be planted in flowerbed, False otherwise

def canPlaceFlowers(flowerbed, n):
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            left_empty = (i==0) or (flowerbed[i-1] == 0)
            right_empty = (i==len(flowerbed)-1) or (flowerbed[i+1] == 0)
            if left_empty and right_empty:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
    return n == 0