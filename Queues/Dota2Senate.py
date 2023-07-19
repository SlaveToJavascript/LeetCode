# https://leetcode.com/problems/dota2-senate/description/
# MEDIUM

# GIVEN:
    # a string, senate, representing the senators from 2 parties, Radiant ("R") and Dire ("D")
    # each senator can either ban a senator of the opposing party, OR 
    # declare victory if there are no opponents left in the senate

# RETURN:
    # the name of the party that will declare victory

# EXAMPLE:
    # Input: senate = "RD"
    # Output: "Radiant"
    # Explanation: 
    # The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
    # And the second senator can't exercise any rights anymore since his right has been banned. 
    # And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

    # Input: senate = "RDD"
    # Output: "Dire"
    # Explanation: 
    # The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
    # And the second senator can't exercise any rights anymore since his right has been banned. 
    # And the third senator comes from Dire and he can ban the first senator's right in round 1. 
    # And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.

###########################################################################################################

# ✅ ALGORITHM 1: QUEUES
# Maintain 2 queues, 1 for indexes of R and another for indexes of D
# while both stacks are not empty, dequeue from both stacks and compare indexes
    # -> smaller index senator will ban the other -> gets added back to queue with new index = prev index + length of senator string
# when only one queue is not empty, return the party (Radiant/Dire) of that queue

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def predictPartyVictory(senate):
    r_q = []
    d_q = []

    # add indexes of "R" and "D" into the respective queues
    for idx, char in enumerate(senate):
        if char == 'R': r_q.append(idx)
        else: d_q.append(idx)
    
    # while both queues are not empty,
    while r_q and d_q:
        r, d = r_q.pop(0), d_q.pop(0) # dequeue from both queues and compare indexes
        # the smaller index wins and gets added back to its queue
        if r < d:
            r += len(senate)
            r_q.append(r) # the new index need to += length of senate string, else it will always be smaller after all iterations
        else:
            d += len(senate)
            d_q.append(d)
    
    # at this point, only 1 queue is not empty
    # there will definitely be 1 queue that is not empty and the other is empty here
    # the non-empty queue here is the one with the victorious party
    while r_q: return "Radiant" # if Radiant queue is empty, return Radiant
    return "Dire" # else, return Dire