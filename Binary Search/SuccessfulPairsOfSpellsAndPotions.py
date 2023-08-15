# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
# MEDIUM
# Tags: binarysearchlc, #2300

# GIVEN:
    # 2 positive integer arrays, spells and potions
        # spells[i] represents the strength of the ith spell
        # potions[j] represents the strength of the jth potion
    # an integer, success
        # A spell and potion pair is considered successful if the product of their strengths is at least success

# TASK:
    # Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell

# EXAMPLES:
    # Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
    # Output: [4,0,3]
    # Explanation:
    # - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
    # - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
    # - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
    # Thus, [4,0,3] is returned.

    # Input: spells = [3,1,2], potions = [8,5,8], success = 16
    # Output: [2,0,2]
    # Explanation:
    # - 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
    # - 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
    # - 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
    # Thus, [2,0,2] is returned.

###########################################################################################################

# ❌ ALGORITHM 1: TWO POINTERS
# Sort potions array
# For each spell, iterate through potions array to find the smallest number where spell * potion >= success
# Once the smallest no. in potions that satisfies the requirement is found, the remaining elements also satisfy requirement -> add no. of potions that satisfy requirement to pairs

# TIME COMPLEXITY: O(p log p) + O(ps)
    # p = length of potions array
    # s = length of spells array
    # O(p log p) is for the sort function (we are sorting potions array)
    # O(ps): for every iteration of spells, we iterate through potions array up to p times
# SPACE COMPLEXITY: O(n)
    # for the sorted array

def successfulPairs(spells, potions, success):
    pairs = [0] * len(spells) # return value

    potions = sorted(potions)
    n = len(potions)

    for s in range(len(spells)): # s is pointer for spells array
        p = 0 # pointer for potions array
        while p < len(potions): # iterate potions array to find smallest element where s*p >= success
            if spells[s] * potions[p] >= success:
                pairs[s] = n-p # smallest element that satisfies condition found
                break # since the potions is sorted, remaining elements are bigger -> definitely satisfies condition -> no need to continue
            else:
                p += 1 # keep looking in potions array
    
    return pairs

#==========================================================================================================

# ❌ ALGORITHM 2: BINARY SEARCH WITH BISECT (TLE)
# Sort potions array
# For each spell, do binary search on potions array to find the smallest number where spell * potion >= success
    # use bisect_left() to get the smallest index where success may be inserted to maintain sort order
    # if index returned by bisect_left() is = length of potions, array, it means no potion is find that satisfies the requirement -> append 0 to return array
# Once the smallest no. in potions that satisfies the requirement is found, the remaining elements also satisfy requirement -> add no. of potions that satisfy requirement to pairs

# TIME COMPLEXITY: O(plogp + slogp)
    # Sort potions array -> O(p log p)
    # For each element in spells array, we do binary search on potions array -> O(s log p)
# SPACE COMPLEXITY: O(p)
    # for sorting potions array

from bisect import bisect_left

def successfulPairs(spells, potions, success):
    pairs = [] # return value
    potions.sort()

    for spell in spells:
        potions_multiplied = [i*spell for i in potions] # each potion multiplied by current spell
        pos = bisect_left(potions_multiplied, success) # smallest index to insert success in sorted order
        
        if pos >= len(potions): # this means that no element in potions satisfies the condition
            pairs.append(0)
        else:
            pairs.append(len(potions)-pos)
    
    return pairs

#==========================================================================================================

# ✅ ALGORITHM 3: BINARY SEARCH
# Sort potions array
# For each spell, do binary search on potions array to find the smallest number where spell * potion >= success
# Once the smallest no. in potions that satisfies the requirement is found, the remaining elements also satisfy requirement -> add no. of potions that satisfy requirement to pairs

# TIME COMPLEXITY: O(plogp + slogp)
    # Sort potions array -> O(p log p)
    # For each element in spells array, we do binary search on potions array -> O(s log p)
# SPACE COMPLEXITY: O(p)
    # for sorting potions array

def successfulPairs(spells, potions, success):
    pairs = [] # return value
    potions.sort()

    for spell in spells:
        l, r = 0, len(potions)-1
        idx = len(potions) # find leftmost potion that works
            # initiate to len(potions) so that we can later check if idx = len(potions) -> if yes, none of the potions work

        while l <= r:
            mid = (l+r) // 2
            if potions[mid] * spell >= success: # find smaller mid
                r = mid - 1
                idx = mid
            else:
                l = mid + 1
        
        pairs.append(len(potions)-idx)
    
    return pairs