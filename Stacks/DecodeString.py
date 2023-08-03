# https://leetcode.com/problems/decode-string/description/
# MEDIUM
# Tags: stacklc, #394

# GIVEN:
    # a string s

# TASK:
    # for k[string], return the decoded string where each substring in the brackets are repeated k times

# EXAMPLES:
    # Input: s = "3[a]2[bc]"
    # Output: "aaabcbc"

    # Input: s = "3[a2[c]]"
    # Output: "accaccacc"

    # Input: s = "2[abc]3[cd]ef"
    # Output: "abcabccdcdcdef"

###########################################################################################################

# ✅ ALGORITHM 1: STACKS
# Iterate the string and push each character into the stack if character is not the closing bracket "]"
# When character is closing bracket "]", pop the stack until you reach the opening bracket "["
    # for each popped character, concatenate it to the front of a concatenated string
    # e.g. if we pop b, then a, the concatenated string is "ab"
# pop the opening bracket "[" as well
# keep popping the stack if the last integer is a digit
    # for each popped digit, concatenate it to the front of a concatenated integer string
    # e.g. if we pop 2, then 3, the concatenated integer string is "23"
# multiply the resulting popped integer with the resulting popped string and push the whole thing into stack
    # e.g. if resulting popped integer string is "12" and resulting popped string is "ab", pop the string resulting from the operation 12 * "ab" into stack
# after the iteration is finished, return the remaining elements in the stack joined together

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def decodeString(s):
    stack = []
    for char in s:
        if char != "]": # if current char is not ], push current char to stack
            stack.append(char)
        else:
            popped_string = ""
            while stack and stack[-1] != "[": # while stack not empty and last item in stack is not [
                popped_string = stack.pop() + popped_string # keep popping from stack and add popped char to front of popped string
            
            stack.pop() # pop the "["
            
            popped_digits = ""
            while stack and stack[-1].isdigit(): # while stack not empty and last item in stack is a no.
                popped_digits = stack.pop() + popped_digits # keep popping from stack and add popped digit to front of popped digits
            
            stack.append(int(popped_digits) * popped_string) # multiply the resulting digits with the resulting string and push resulting multiplied string into stack

    return ''.join(stack)