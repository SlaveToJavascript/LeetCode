# 950. Reveal Cards In Increasing Order
# https://leetcode.com/problems/reveal-cards-in-increasing-order/
# MEDIUM
# Tags: queuelc, #950

# You are given an integer array deck. There is a deck of cards where every card has a unique integer. The integer on the ith card is deck[i].
# You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.
# You will do the following steps repeatedly until all cards are revealed:
    # 1. Take the top card of the deck, reveal it, and take it out of the deck.
    # 2. If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
    # 3. If there are still unrevealed cards, go back to step 1. Otherwise, stop.
# Return an ordering of the deck that would reveal the cards in increasing order.
# NOTE: the first entry in the answer is considered to be the top of the deck.

# EXAMPLES:
    # Input: deck = [17,13,11,2,3,5,7]
    # Output: [2,13,3,11,5,17,7]
    # Explanation: 
    # We get the deck in the order [17,13,11,2,3,5,7] (this order does not matter), and reorder it.
    # After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
    # We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
    # We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
    # We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
    # We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
    # We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
    # We reveal 13, and move 17 to the bottom.  The deck is now [17].
    # We reveal 17.
    # Since all the cards revealed are in increasing order, the answer is correct.

    # Input: deck = [1,1000]
    # Output: [1,1000]

###########################################################################################################

# ✅ ALGORITHM 1: REVERSE SIMULATION (my solution, atttempted April 10 2024)
# Create result array to contain the ressult to be returned
# Sort the deck in reverse order
# Iterate through deck array ; each step of the reverse simulation should be:
    # 1. If result array is not empty, move the last element in result to the front
    # 2. add current element of the deck array iteration to the front of the result array

# TIME COMPLEXITY: O(n log n)
    # for sorting
# SPACE COMPLEXITY: O(n)

def deckRevealedIncreasing(deck):
    # reverse simulation: move last number in result to the front, then add the next largest no. from deck to the front of result
    result = []
    deck.sort(reverse=True)
    for i in range(len(deck)):
        if len(result) > 1: # if there's more than 1 element in result array,
            result = [result[-1]] + result[:-1] # move the last element in result to the front of the array
        result = [deck[i]] + result
    
    return result

#==========================================================================================================

# ✅ ALGORITHM 2: SIMULATION USING DECK INDICES
# simulate the revealing process using a queue of indices of deck array to find the order in which the cards in the sorted deck array will be revealed
    # We do this by popping the front index from the queue, then adding the current card in the sorted(deck) iteration to result array at the popped index
    # then, we move the next index in the queue to the back

# TIME COMPLEXITY: O(n log n)
    # for sorting
# SPACE COMPLEXITY: O(n)

from collections import deque

def deckRevealedIncreasing(self, deck):
    index_q = deque(range(len(deck))) # create a queue of the indexes of deck
    result = [0] * len(deck) # return array

    for card in sorted(deck):
        result[index_q.popleft()] = card # pop 1st index from q, and add current sorted card to that index in result array
        if index_q:
            index_q.append(index_q.popleft()) # move 1st element in index_q to become last element

    return result