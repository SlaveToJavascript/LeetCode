# https://leetcode.com/problems/text-justification/description/
# HARD
# Tags: stringlc, #68

# GIVEN:
    # an array of strings, words
    # a width, maxWidth

# TASK:
    # format the text such that each line has exactly maxWidth characters and is fully (left and right) justified
    # You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters
    # Extra spaces between words should be distributed as evenly as possible
        # If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right
    # For the last line of text, it should be left justified and no extra space is inserted between words

# EXAMPLES:
    # Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
    # Output:
    # [
    #    "This    is    an",
    #    "example  of text",
    #    "justification.  "
    # ]

    # Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
    # Output:
    # [
    #   "What   must   be",
    #   "acknowledgment  ",
    #   "shall be        "
    # ]
    # Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
    # Note that the second line is also left-justified because it contains only one word.

    # Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
    # Output:
    # [
    #   "Science  is  what we",
    #   "understand      well",
    #   "enough to explain to",
    #   "a  computer.  Art is",
    #   "everything  else  we",
    #   "do                  "
    # ]

###########################################################################################################

# ✅ ALGORITHM:

# TIME COMPLEXITY: O(n*w)
    # n = no. of words
    # w = average length of each word
    # outer for-loop: O(n) since it iterates through all words
    # ' '.join(sentence + [words[i]]) -> constructs a new list and joins it into a string -> O(w) for each word
    # inner for-loop takes O(w) time for each word
    # Overall = O(n*w)
# TIME COMPLEXITY: O(n)
    # sentence array has max length of n

def fullJustify(words, maxWidth):
    result = [] # return value
    sentence = [] # current sentence being formed
    
    for i in range(len(words)):
        if len(' '.join(sentence + [words[i]])) <= maxWidth: # if current word can be added to sentence
            sentence.append(words[i])
        else:
            spaces = 1 # min. no. of spaces between each word (initialized to 1)
            remaining_spaces = maxWidth - len(''.join(sentence)) # remaining no. of spaces to be distributed evenly between words, with left words having more spaces
            
            if len(sentence)-1 > 0: # this check is needed so we don't divide by 0
                spaces = (maxWidth - len(''.join(sentence))) // (len(sentence)-1) # 3 // 2 = 1
                remaining_spaces = (maxWidth - len(''.join(sentence))) % (len(sentence)-1) # 3 % 2 = 1
            
            sentence_str = "" # string version of sentence array
            for word in sentence:
                if sentence_str: # if sentence_str is not empty, i.e. if current word is not the 1st word to be added to sentence_str
                    sentence_str += spaces * " " # add the min. no. of spaces before each word
                    if remaining_spaces > 0: # add the remaining spaces that are to be evenly distributed across words
                        sentence_str += " "
                        remaining_spaces -= 1
                sentence_str += word # add current word to sentence_str
            
            # edge case: sentence_str only has 1 word -> add extra strings to the end of sentence_str until length = maxWidth
            if len(sentence_str) < maxWidth:
                sentence_str += ' ' * (maxWidth - len(sentence_str))
            
            result.append(sentence_str)
            sentence = [words[i]] # after adding existing sentence to result output, reset sentence and add current word to it (current word will be the start of a new line)
    
    # handle last line
    if sentence:
        sentence_str = ' '.join(sentence)
        if len(sentence_str) < maxWidth:
            sentence_str += (maxWidth - len(sentence_str)) * ' ' # last line -> add extra strings to the end of sentence_str until length = maxWidth
        result.append(sentence_str)
    
    return result