# 948. Bag of Tokens
# https://leetcode.com/problems/bag-of-tokens/description/
# MEDIUM
# Tags: twopointerslc, greedylc, #948

# GIVEN:
    # an initial power of power
    # an initial score of 0
    # a bag of tokens given as an integer array tokens, where each tokens[i] denotes the value of token_i

# TASK:
    # maximize the total score by playing these tokens
    # In 1 move, you can play an UNPLAYED token in 1 of the 2 ways:
        # Face-up: If your current power >= tokens[i], you may play token_i, losing tokens[i] power and gaining 1 score
        # Face-down: If your current score >= 1, you may play token_i, gaining tokens[i] power and losing 1 score
        # Return the max possible score you can achieve after playing any number of tokens

# EXAMPLES:
    # Input: tokens = [100], power = 50
    # Output: 0
    # Explanation: Since your score is 0 initially, you cannot play the token face-down. You also cannot play it face-up since your power (50) is less than tokens[0] (100).

    # Input: tokens = [200,100], power = 150
    # Output: 1
    # Explanation: Play token1 (100) face-up, reducing your power to 50 and increasing your score to 1.
    # There is no need to play token0, since you cannot play it face-up to add to your score. The maximum score achievable is 1.

    # Input: tokens = [100,200,300,400], power = 200
    # Output: 2
    # Explanation: Play the tokens in this order to get a score of 2:
    # Play token0 (100) face-up, reducing power to 100 and increasing score to 1.
    # Play token3 (400) face-down, increasing power to 500 and reducing score to 0.
    # Play token1 (200) face-up, reducing power to 300 and increasing score to 1.
    # Play token2 (300) face-up, reducing power to 0 and increasing score to 2.
    # The maximum score achievable is 2.

###########################################################################################################

# ✅ ALGORITHM 1: SORTING + GREEDY + TWO POINTERS
# in summary:
    # face-up (power >= tokens[i]): score += 1, power -= tokens[i]
    # face-down (score >= 1): score -= 1, power += tokens[i]
# GREEDY ALGORITHM means maximizing score by:
    # playing FACE-UP as much as possible (as long as power > tokens[i])
        # when playing face-up, always choose the SMALLEST token (since power -= tokens[i] when playing face-up, we want to reduce the power lost -> pick smallest token)
    # only playing FACE-DOWN if face-up cannot be played (as long as score >= 1)
        # when playing face-down, always choose the BIGGEST token (since power += tokens[i] when playing face-down, we want to increase power gain -> pick largest token)
# sort tokens array and use 2 pointers, l and r, to keep track of smallest and largest tokens respectively
# keep checking if face-up can be played; if not, check if face-down can be played; if not, game over (since power < smallest token and score = 0, we can't play any other tokens either)
# for every token played, keep checking for max score

# TIME COMPLEXITY = O(n log n)
    # for sorting
    # while-loop takes O(n) time
# SPACE COMPLEXITY = O(n)
    # sorting takes O(n) space

def bagOfTokensScore(tokens, power):
    tokens.sort()
    score = max_score = 0
    l, r = 0, len(tokens)-1 # l for smallest token, r for largest token

    while l <= r:
        if power >= tokens[l]: # play face-up
            score += 1
            power -= tokens[l]
            l += 1
        elif score >= 1: # play face-down
            score -= 1
            power += tokens[r]
            r -= 1
        else: # cannot play anything
            break
        max_score = max(score, max_score) # update max score (if needed) with every token encountered
    
    return max_score