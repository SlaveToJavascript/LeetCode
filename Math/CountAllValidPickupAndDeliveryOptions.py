# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
# HARD
# Tags: mathlc, dplc, #1359

# GIVEN:
    # n orders
        # each order consists of pickup and delivery services

# TASK:
    # return the number of valid pickup/delivery sequences such that pickup1 is always before delivery1
    # Since the answer may be too large, return it modulo 10^9 + 7

# EXAMPLES:
    # Input: n = 1
    # Output: 1
    # Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

    # Input: n = 2
    # Output: 6
    # Explanation: All possible orders: 
    # (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
    # This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.

    # Input: n = 3
    # Output: 90

###########################################################################################################

# ✅ ALGORITHM: DISCRETE MATH
# There are 2n slots
    # e.g. if n=2, sequence would include P1, P2, D1, D2 (4 slots)
# no. of ways to place 1 set of (P1, D1) = 2n * (2n-1)
    # there are 2n slots to place P1
    # after placing P1, there will be 2n-1 slots to place D1
    # -> total no. of ways to place (P1, D1) = 2n * (2n-1)
# in half of these 2n * (2n-1) ways, P1 comes before D1, and in the other half of these 2n * (2n-1) ways, D1 comes before P1
    # since D1 coming before P1 is an invalid choice, there are 2n(2n-1)/2 invalid choices for each n
# for the 2nd set of (P2, D2), there are 2n-2 slots to choose from (since 2 slots have been taken up by P1, D1)

# ✅ ALGORITHM: DISCRETE MATH
# While there are still slots to be filled, not all pairs (Px, Dx) have been assigned places
# slots = no. of slots remaining
# for the placement of each pair (Px, Dx), there are slots * (slots-1) ways to place the pair
    # half of those placements will have Dx come before Px, which are invalid
    # -> valid no. of placements for each pair = slots * (slots-1) / 2 (half of the total no. of ways to place current pair)
# multiply the valid no. of placements for each pair together to get the total no. of valid placements
# reduce the no. of slots by 2 each time (to indicate each pair taking their 2 slots) -> the next pair has 2 less choices to choose from

def countOrders(n):
    slots = 2*n # no. of slots to begin with
    result = 1 # initialize result to 1 (if n=1, result=1 AND 1 is a neutral value for multiplication)
    
    while slots > 0: # while there are still slots to fill, it means not all pairs have been assigned places
        valid_choices = slots * (slots-1) // 2 # no. of valid placements for current pair
        result *= valid_choices
        slots -= 2 # -2 slots since this current pair has taken their 2 places and the next pair will have 2 less slots to choose from
    
    return result % (10**9 + 7)