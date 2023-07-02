# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
# MEDIUM

# GIVEN:
    # positive integer array, spells, where spells[i] = strength of the ith spell
    # positive integer array, potions, where potions[i] = strength of the ith potion
    # integer, success
        # A spell and potion pair is successful if the product of their strengths is at least success

# TASK:
    # Return integer array of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell

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

# ❌ ALGORITHM 1: BRUTE FORCE
# Divide success by each spell and only count no. of elements in potions greater than this result

def successfulPairs(spells, potions, success):
    pairs = []
    for spell in spells:
        minn = float(success)/spell
        pairs.append(len(filter(lambda x: x >= minn, potions)))
    return pairs

#==========================================================================================================

# ✅ ALGORITHM 2: TWO POINTERS
# Sort potions array
# Find the smallest integer in potions that, after multiplied by spell, is >= success
# that integer and all other integers behind it are >= success

def successfulPairs(spells, potions, success):
    pairs = []
    