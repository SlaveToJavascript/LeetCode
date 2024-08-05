# 1190. Reverse Substrings Between Each Pair of Parentheses
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
# MEDIUM
# Tags: stacklc, #1190

# GIVEN:
    # a string, s, that consists of lower case English letters and brackets

# TASK:
    # Reverse the strings in each pair of matching parentheses, starting from the innermost one
    # Your result should not contain any brackets

# EXAMPLES:
    # Input: s = "(abcd)"
    # Output: "dcba"

    # Input: s = "(u(love)i)"
    # Output: "iloveu"
    # Explanation: The substring "love" is reversed first, then the whole string is reversed.

    # Input: s = "(ed(et(oc))el)"
    # Output: "leetcode"
    # Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

###########################################################################################################

# ✅ ALGORITHM 1: STACK
    # https://youtu.be/n_pCJmg-RyU?si=bO7r1aSJcr1uA0Yb
# use a stack to track indexes of opening brackets, i.e. "("
    # when traversing string s, whenever we encounter an opening parenthesis "(", push the current length of our result string onto the stack
        # This length serves as a marker for result array, indicating the start position of the substring that will need to be reversed (in result array) once we find its corresponding closing parenthesis ")"
    # When we encounter a closing parenthesis ")", pop the last index from the stack
        # This popped index = the index of the matching opening parenthesis for the current closing parenthesis
        # Using this index, we know the starting index of the substring that needs to be reversed (in results array)
        # reverse the substring starting from this start index (popped from the stack) to the current end of the result array
    # when we encounter an alphabet, add it to stack
# NOTE: This approach ensures that we correctly handle nested parentheses by always reversing the innermost pairs first before moving outward, ultimately producing the desired output string

# TIME COMPLEXITY: O(n^2)
    # O(n) to iterate each char of string s once
    # the reversing operation may taken O(n) in the worst case where the whole string needs to be reversed
    # -> overall TC = O(n^2)
# SPACE COMPLEXITY: O(n)
    # the stack may take O(n) space in the worst case

def reverseParentheses(s):
    result = [] # resulting string builder
    open_parentheses_indexes = [] # stack that tracks indexes of opening brackets i.e. "("

    for char in s:
        if char == "(":
            open_parentheses_indexes.append(len(result))
        elif char == ")":
            start = open_parentheses_indexes.pop()
            result[start:] = result[start:][::-1] # reverse the portion of the string beginning from "start"
        else:
            result.append(char)
    
    return "".join(result)

#==========================================================================================================

# ✅✅ ALGORITHM 2: WORMHOLE TELEPORTATION TECHNIQUE
# ! MAIN IDEA: use an array, pair, of len(s) where for each "(" or ")" in s, the corresponding index in "pair" array indicates the index of the other parenthesis pair in s
    # e.g. s = "(u(love)i)"
    #   pair = [9_7____2_0]
        # pair is an array where each integer represents the index of its corresponding parenthesis pair (e.g. the 1st element in pair is 9, which corresponds to the opening bracket in s, and 9 refers to the index of the closing bracket that corresponds to this opening bracket)
# STEPS:
    # 1. 1ST PASS (pair up parentheses):
        # initialize "open_bracket_indexes" stack and "pair" array to establish "wormhole" connections
        # for '('s, push its index into "open_bracket_indexes" stack
        # for ')'s, pop from "open_bracket_indexes" stack and link both indices in "pair" to create the "wormhole"
    # 2. 2ND PASS (build the result string):
        # Initialize "result" string-builder array, curr_index, and "direction" to traverse and build the result
            # NOTE: direction = 1 means forward, direction = -1 means backward
        # for "("s and ")"s, jump through the "wormhole" using "pair" and reverse direction to simulate reversal
        # Otherwise, append the character to result to build the result string
        # Move "curr_index" by "direction" to continue traversal
# Return result as the final string with all reversals simulated
# for visualization, see https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/editorial/

# TIME COMPLEXITY: O(n)
    # O(n) for each pass
# SPACE COMPLEXITY: O(n)
    # the stack "open_bracket_indexes" holds up to n/2 elements
    # "pair" array takes O(n)

def reverseParentheses(s):
    open_bracket_indexes = []
    pair = [0] * len(s)

    for i in range(len(s)):
        if s[i] == "(":
            open_bracket_indexes.append(i)
        elif s[i] == ")":
            j = open_bracket_indexes.pop()
            pair[i] = j
            pair[j] = i
    
    result = []
    curr_idx = 0
    direction =  1 # 1 for forward, -1 for backward

    while curr_idx < len(s):
        if s[curr_idx] == "(" or s[curr_idx] == ")":
            curr_idx = pair[curr_idx] # teleport to find the other parenthesis pair
            direction = -direction # change the direction
        else: # if char is an alphabet
            result.append(s[curr_idx])
        curr_idx += direction
    
    return "".join(result)