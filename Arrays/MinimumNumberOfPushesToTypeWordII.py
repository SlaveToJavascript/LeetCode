# 3016. Minimum Number of Pushes to Type Word II
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/
# MEDIUM
# Tags: greedylc, arraylc, #3016

# You are given a string word containing lowercase English letters.
# Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .
# It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.
# Return the minimum number of pushes needed to type word after remapping the keys.
# An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.

# EXAMPLES:
    # Input: word = "abcde"
    # Output: 5
    # Explanation: The remapped keypad given in the image provides the minimum cost.
    # "a" -> one push on key 2
    # "b" -> one push on key 3
    # "c" -> one push on key 4
    # "d" -> one push on key 5
    # "e" -> one push on key 6
    # Total cost is 1 + 1 + 1 + 1 + 1 = 5.
    # It can be shown that no other mapping can provide a lower cost.

    # Input: word = "xyzxyzxyzxyz"
    # Output: 12
    # Explanation: The remapped keypad given in the image provides the minimum cost.
    # "x" -> one push on key 2
    # "y" -> one push on key 3
    # "z" -> one push on key 4
    # Total cost is 1 * 4 + 1 * 4 + 1 * 4 = 12
    # It can be shown that no other mapping can provide a lower cost.
    # Note that the key 9 is not mapped to any letter: it is not necessary to map letters to every key, but to map all the letters.

    # Input: word = "aabbccddeeffgghhiiiiii"
    # Output: 24
    # Explanation: The remapped keypad given in the image provides the minimum cost.
    # "a" -> one push on key 2
    # "b" -> one push on key 3
    # "c" -> one push on key 4
    # "d" -> one push on key 5
    # "e" -> one push on key 6
    # "f" -> one push on key 7
    # "g" -> one push on key 8
    # "h" -> two pushes on key 9
    # "i" -> one push on key 9
    # Total cost is 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24.
    # It can be shown that no other mapping can provide a lower cost.

###########################################################################################################

# ✅ ALGORITHM: GREEDY SORTING
# ! MAIN IDEA: we map the most frequent characters to the keys that require the least number of presses
    # e.g. if 'a' is the most frequent character, ensure 'a' is mapped as a 1st character of any key (i.e. need only 1 press)
# We get the frequencies of each character in s and sort them in descending order using an array
    # NOTE: we don't need to use hashmap since we don't actually need to care which characters has which frequency, we just care how many times we need to press based on the frequencies of chars
# since there are 8 keys that we can map to, we map the top 8 most frequent chars to each of these 8 keys (i.e. assign them to be the 1st char in each of these 8 respective keys), then map the next 8 chars to become the 2nd char of each of these 8 keys (i.e. require 2 presses), and so on

# TIME COMPLEXITY: O(n log n)
    # for sorting
# SPACE COMPLEXITY: O(n)
    # sort() function takes O(n) space

def minimumPushes(word):
    counts = [0] * 26 # don't need hashmap since we don't care what the chars are, we only care about the occurrences of the chars
    for char in word:
        counts[ord(char)-ord('a')] += 1 # e.g. counts[0] = no. of 'a's, counts[1] = no. of 'b's, etc.
    counts.sort(reverse=True) # sort frequencies in descending order

    result = 0
    distinct_chars = 0 # no. of distinct chars in word
    for count in counts:
        result += count * (1 + distinct_chars//8) # 1 press each for 1st 8 chars, 2 presses each for 2nd group of 8 chars, etc.
        distinct_chars += 1 # each count iteration is for a different char

    return result