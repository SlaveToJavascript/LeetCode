# https://leetcode.com/problems/roman-to-integer/

# For every pair of consecutive letters, if the 1st letter is smaller than the next, the 1st letter is -ve
# Else, both letters are +ve

# Time complexity: O(n)
# Space complexity: O(1) + dictionary

def romanToInt(s): # 1 <= s <= 3999
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    for i in range(len(s)-1):
        if dic[s[i]] < dic[s[i+1]]:
            res += -dic[s[i]]
        else:
            res += dic[s[i]]
    return res