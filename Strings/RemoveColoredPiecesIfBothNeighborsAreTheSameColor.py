# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
# MEDIUM
# Tags: arraylc, slidingwindowlc, #2038

# Take alternating turns removing chars A's and B's from the string, colors
# char A is removed first, then B
# a char A can only be removed if its left and right neighbors are both A's
# a char B can only be removed if its left and right neighbors are both B's
# if char A cannot be removed on its turn, B wins -> return False; else if char B cannot be removed on its turn, A wins -> return True

# EXAMPLES:
    # Input: colors = "AAABABB"
    # Output: true
    # Explanation:
    # AAABABB -> AABABB
        # A moves first and removes the 2nd 'A' from the left since that is the only 'A' whose neighbors are both 'A'
    # B cannot make a move on its turn since there are no 'B's whose neighbors are both 'B'.
    # Thus, A wins -> return true

    # Input: colors = "AA"
    # Output: false
    # Explanation:
    # On A's turn, there are only 2 'A's and both are on the edge of the line, so it cannot move on its turn
    # Thus, B wins -> return false.

    # Input: colors = "ABBBBBBBAAA"
    # Output: false
    # Explanation:
    # ABBBBBBBAAA -> ABBBBBBBAA
        # A's only option is to remove the 2nd to last 'A' from the right.
    # ABBBBBBBAA -> ABBBBBBAA
        # B has many options for which 'B' piece to remove
    # On Alice's second turn, she has no more pieces that she can remove.
    # Thus, B wins -> return false

###########################################################################################################

# ✅ ALGORITHM 1: SLIDING WINDOW
# the no. of A's and B's to be removed is determined by shifting left and right pointers -> for every window of consecutive A's / consecutive B's, if the length of the window >= 3, subtract 2 from the length of the window
    # subtract 2 because only the leftmost and righmost chars of the window cannot be removed
# using the above method, get the no. of A's and B's to be removed
# the character (A or B) that has the greater no. to be removed is the winner (because after all of the other char have been removed, the winning char will make the final turn in the game)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def winnerOfGame(colors):
    a_count = b_count = 0 # no. of A's and B's to be removed
    l = 0 # left pointer
    window_size = 0 
    
    for r in range(len(colors)):
        if colors[r] == colors[l]:
            window_size += 1
        else:
            if window_size > 2:
                if colors[l] == "A":
                    a_count += window_size-2
                else:
                    b_count += window_size-2
            window_size = 1 # reset window size to 1 for the current char at colors[r]
            l = r
    
    # for the last window (last window_size is not added to a_count/b_count)
    if window_size > 2:
        if colors[l] == "A":
            a_count += window_size-2
        else:
            b_count += window_size-2

    return a_count > b_count # char A or B with the higher no. of chars to be removed wins
        # if A wins, return true, else return false

#==========================================================================================================

# ✅ ALGORITHM 2: ITERATE ARRAY, COMPARING LEFT AND RIGHT NEIGHBORS
# Instead of using a sliding window, we can simply iterate colors array and check that current element = its left neighbor = its right neighbor -> if yes, increment no. of A's / B's to remove

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def winnerOfGame(colors):
    a_count = b_count = 0

    for i in range(1, len(colors)-1): # iterate colors array, skipping 1st and last elements in the array to prevent going out of bounds + these 1st and last elements cannot be removed
        if colors[i-1] == colors[i] == colors[i+1]: # if current element = its left and right neighbors,
            if colors[i] == "A":
                a_count += 1
            else:
                b_count += 1
    
    return a_count > b_count # char A or B with the higher no. of chars to be removed wins
        # if A wins, return true, else return false