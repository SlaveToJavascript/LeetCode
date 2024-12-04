# 2938. Separate Black and White Balls
# https://leetcode.com/problems/separate-black-and-white-balls/
# MEDIUM
# Tags: twopointerslc, #2938

# GIVEN:
    # a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively
    # There are n balls on a table, each ball has a color black or white

# TASK:
    # In each step, you can choose two adjacent balls and swap them
    # Return the minimum number of steps to group all the black balls to the right and all the white balls to the left

# EXAMPLES:
    # Input: s = "101"
    # Output: 1
    # Explanation: We can group all the black balls to the right in the following way:
    # - Swap s[0] and s[1], s = "011".
    # Initially, 1s are not grouped together, requiring at least 1 step to group them to the right.

    # Input: s = "100"
    # Output: 2
    # Explanation: We can group all the black balls to the right in the following way:
    # - Swap s[0] and s[1], s = "010".
    # - Swap s[1] and s[2], s = "001".
    # It can be proven that the minimum number of steps needed is 2.

    # Input: s = "0111"
    # Output: 0
    # Explanation: All the black balls are already grouped to the right.

###########################################################################################################

# ✅ ALGORITHM 1: TWO POINTERS
# NOTE: you don't have to actually move the 0's to the front, just count the number of swaps needed
# initialize l and r pointers from the start of s
# l pointer will always point to the position where a 0 (at the current r pointer) should be moved to
# r pointer iterates through s, looking for 0's to swap with the element at l pointer (to bring 0's to the front)
# once a 0 is found by r pointer, result += r-l (i.e. number of swaps needed to bring 0 to the front), then l += 1 (to indicate the index where the next 0 needs to be moved to)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def minimumSteps(s):
    result = 0
    l = 0
    for r in range(len(s)):
        if s[r] == '0':
            result += r-l
            l += 1
    
    return result

#==========================================================================================================

# ✅ ALGORITHM 2: KEEP TRACK OF NO. OF BLACK BALLS
# since we need to move white balls to the front, when we iterate the balls and encounter a white ball, we have to swap it once with each black ball that has been encountered so far
    # e.g. W W B B B W B B W B
    #        w<----- ^
        # the white ball indicated by w has to swap with 3 black balls to be moved to the front, and the next white ball after that has to swap with 3+2=5 black balls to be moved to the front
        # i.e. the no. of swaps needed for a white ball to be moved to the front is the no. of black balls encountered so far (up until the current ball of the iteration)
# hence, whenever we encounter a white ball, add the no. of black balls to the result
    # whenever we encounter a black ball, increment the no. of black balls by 1

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def minimumSteps(s):
    black_balls = 0
    total_swaps = 0 # return result

    for ball in s:
        if ball == '0': # white
            total_swaps += black_balls
        else: # black
            black_balls += 1
    
    return total_swaps