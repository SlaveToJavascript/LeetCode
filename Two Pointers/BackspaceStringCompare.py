# https://leetcode.com/problems/backspace-string-compare/description/
# EASY

# GIVEN:
    # two strings S and T

# TASK:
    # return true if they are equal when both are typed into empty text editors
    # "#" means a backspace character
    # NOTE: after backspacing an empty text, the text will continue empty

# EXAMPLES:
    # Input: s = "ab#c", t = "ad#c"
    # Output: true
    # Explanation: Both s and t become "ac".

    # Input: s = "ab##", t = "c#d#"
    # Output: true
    # Explanation: Both s and t become "".

    # Input: s = "a#c", t = "b"
    # Output: false
    # Explanation: s becomes "c" while t becomes "b".

###########################################################################################################

# ✅ ALGORITHM: STACKS
# Iterate through each string
# If character is not "#", push to stack
# Else, pop from stack
# return the resulting string formed from the remaining characters in stack

# Time Complexity: O(S+T), where S and T = lengths of strings s and t respectively
# Space Complexity: O(S+T)

def backspaceCompare(s, t):
    
    def remove_hashes(string):
        stack = []
        for char in string:
            if char != "#":
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)
    
    return remove_hashes(s) == remove_hashes(t)