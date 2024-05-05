# 422. Valid Word Square
# https://leetcode.com/problems/valid-word-square/description
# EASY
# Tags: matrixlc, premiumlc, #422

# GIVEN:
    # an array of strings, words

# TASK:
    # return true if it forms a valid word square
        # A sequence of strings forms a valid word square if the kth row and column read the same string

# EXAMPLES:
    # Input: words = ["abcd","bnrt","crmy","dtye"]
    # Output: true
    # Explanation:
        # ['a', 'b', 'c', 'd']
        # ['b', 'n', 'r', 't']
        # ['c', 'r', 'm', 'y']
        # ['d', 't', 'y', 'e']
    # The 1st row and 1st column both read "abcd".
    # The 2nd row and 2nd column both read "bnrt".
    # The 3rd row and 3rd column both read "crmy".
    # The 4th row and 4th column both read "dtye".
    # Therefore, it is a valid word square.

    # Input: words = ["abcd","bnrt","crm","dt"]
    # Output: true
    # Explanation:
        # ['a', 'b', 'c', 'd']
        # ['b', 'n', 'r', 't']
        # ['c', 'r', 'm', ' ']
        # ['d', 't', ' ', ' ']
    # The 1st row and 1st column both read "abcd".
    # The 2nd row and 2nd column both read "bnrt".
    # The 3rd row and 3rd column both read "crm".
    # The 4th row and 4th column both read "dt".
    # Therefore, it is a valid word square.

    # Input: words = ["ball","area","read","lady"]
    # Output: false
    # Explanation:
        # ['b', 'a', 'l', 'l']
        # ['a', 'r', 'e', 'a']
        # ['r', 'e', 'a', 'd']
        # ['l', 'a', 'd', 'y']
    # The 3rd row reads "read" while the 3rd column reads "lead".
    # Therefore, it is NOT a valid word square.

###########################################################################################################

# ✅ ALGORITHM: COMPARE DIAGONAL LETTERS OF MATRIX TO ENSURE THEY ARE EQUAL
# for a matrix to be valid, each matrix[r][c] char must be equal to matrix[r][c] char for all r, c within matrix -> check each matrix[r][c]
# NOTE: if we cannot form a square matrix, then it's definitely invalid

# TIME COMPLEXITY: O(n^2)
    # for the nested for-loop
# SPACE COMPLEXITY: O(1)
    # for the constant variables

def validWordSquare(words):
    n = len(max(words, key=len)) # n is the width of the matrix (i.e. the length of the longest word in words array)
    if n != len(words):
        return False # if we cannot form a square matrix, then it's definitely invalid

    for i in range(len(words)):
        words[i] = list(words[i])
        if len(words[i]) < n: # if current word is shorter than the longest word
            words[i] += (n-len(words[i])) * [""] # pad it with empty strings to make it the same length as the longest word

    for r in range(len(words)):
        for c in range(n):
            if words[r][c] != words[c][r]: # check that each matrix[r][c] is equal to matrix[c][r]
                return False

    return True