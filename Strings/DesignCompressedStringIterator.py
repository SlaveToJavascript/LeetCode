# 604. Design Compressed String Iterator
# https://leetcode.com/problems/design-compressed-string-iterator/
# EASY
# Tags: stringlc, premiumlc, designlc, #604

# Design and implement a data structure for a compressed string iterator. The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.
# Implement the StringIterator class:
    # next() Returns the next character if the original string still has uncompressed characters, otherwise returns a white space.
    # hasNext() Returns true if there is any letter needs to be uncompressed in the original string, otherwise returns false.

# EXAMPLES:
    # Input
    # ["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
    # [["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
    # Output
    # [null, "L", "e", "e", "t", "C", "o", true, "d", true]

    # Explanation
    # StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
    # stringIterator.next(); // return "L"
    # stringIterator.next(); // return "e"
    # stringIterator.next(); // return "e"
    # stringIterator.next(); // return "t"
    # stringIterator.next(); // return "C"
    # stringIterator.next(); // return "o"
    # stringIterator.hasNext(); // return True
    # stringIterator.next(); // return "d"
    # stringIterator.hasNext(); // return True

###########################################################################################################

# ❌ ALGORITHM 1: DECOMPRESS STRING (TLE)
# decompress string and keep track of current index in string

# TIME COMPLEXITY: O(n)
    # n = length of compressed string
# SPACE COMPLEXITY: O(n)

class StringIterator(object):
    def __init__(self, compressedString):
        self.chars = []
        self.integers = []
        for i in range(len(compressedString)):
            if compressedString[i].isalpha():
                self.chars.append(compressedString[i])
            else:
                if compressedString[i-1].isalpha():
                    self.integers.append(compressedString[i])
                else:
                    self.integers[-1] += compressedString[i]
        self.string = ""
        for i in range(len(self.chars)):
            num = int(self.integers[i])
            self.string += num * self.chars[i]
        self.i = 0

    def next(self):
        if self.hasNext():
            char = self.string[self.i]
            self.i += 1
            return char
        return ' '

    def hasNext(self):
        return self.i < len(self.string)

#==========================================================================================================

# ✅ ALGORITHM 2: REGEX WITH INTEGER ARRAY + CHARS ARRAY
# use regex to split compressed string into chars and integers into 2 separate arrays respectively
    # both arrays have the same length
# initialize pointer to 0
    # this pointer tracks the index of the current char in both arrays (chars array and integers array)
# hasNext() returns True if pointer < length of chars array
# next() returns the at the current pointer index in chars array and decrements the integer at the current pointer index in integers array
    # if integer at current pointer index in integers array becomes 0 after the decrement, pointer +1 to move to the next char

# TIME COMPLEXITY: O(n)
    # __init__() function takes O(n) time for the regex split and findall
    # hasNext() and next() functions take O(1) time each
# SPACE COMPLEXITY: O(n)
    # n = length of compressed string
    # chars and integers array store a total of n elements

import re

class StringIterator(object):
    def __init__(self, compressedString):
        self.chars = re.split(r'[0-9]+', compressedString)[:-1] # [:-1] to remove the last empty string, since we are splitting by integers and compressedString ends with an integer hence results in an empty string at the end
        self.nums = list(map(int, re.findall(r'[0-9]+', compressedString)))
        self.i = 0 # keeps track of the pointer index in chars or integers array

    def next(self):
        if not self.hasNext():
            return ' '
        
        char = self.chars[self.i]
        self.nums[self.i] -= 1
        if self.nums[self.i] == 0:
            self.i += 1

    def hasNext(self):
        return self.i < len(self.chars)