# https://leetcode.com/problems/string-compression/description/
# MEDIUM
# Tags: twopointerslc, #443

# GIVEN:
    # an array of characters, chars

# TASK:
    # compress it using the following algorithm:
        # Begin with an empty string s
        # For each group of consecutive repeating characters in chars:
            # If the group's length is 1, append the character to s
            # Otherwise, append the character followed by the group's length
        # The compressed string s should not be returned separately, but instead, be stored in the input character array chars
    # NOTE: group lengths that are 10 or longer will be split into multiple characters in chars
    # After you are done modifying the input array, return the new length of the array

###########################################################################################################

# ✅ ALGORITHM: TWO POINTERS
# result integer keeps track of length of compressed string
# i is the index of the 1st character of the current group
    # a group refers to a contiguous group of the same character
# while i < len(chars):
    # for each group, track the group length; keep incrementing group length until a different char is encountered
    # set char at result as char at i
        # since char at i is the index of the 1st char in the current group
    # result + 1
        # +1 so result is now at the index where we start filling up with the group length
    # if group length is > 1, 
        # convert group length to string and fill up with each digit
        # result += length of group length string (we move result pointer to the index where the next character will be compressed and filled up with)
    # i += group length so we move i to point to the 1st character of the next group

# TIME COMPLEXITY: O(n)
    # n = length of chars
# SPACE COMPLEXITY: O(1)

def compress(chars):
    i = 0 # i is the index of the 1st char of every group
    result = 0 # result will become the length of the final compressed string

    while i < len(chars): # every iteration of this loop indicates the beginning of another group in chars
        group_len = 1 # for every new group, initiate length of group to 1 (since min. length of group = 1)

        while i + group_len < len(chars) and chars[i + group_len] == chars[i]:
            group_len += 1 # keep incrementing group length as long as the next char = char at i and i + group_len is not out of bounds

        # at this point, group_len would be the length of the current group

        chars[result] = chars[i] # set char at current index (result) as the 1st char in current group
        result += 1 # increment result so it points to the index where we fill up chars array with the group length
        
        if group_len > 1: # if group length is more than 1, we fill up with each digit of the string of the current group's length
            chars[result : result + len(str(group_len))] = list(str(group_len))
            result += len(str(group_len)) # move result pointer to the index after where the group length has been placed
        
        i += group_len # move i to point to the 1st char of the next group
    
    return result