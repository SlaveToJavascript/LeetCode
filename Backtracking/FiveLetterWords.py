# https://leetcode.com/discuss/interview-question/3297037/Google-or-Onsite-or-Bangalore
# Tags: backtracklc, google

# Given a dictionary of English words, return distinct sentences of 5-letter unique words with 5 words each which can be made out of dictionary words
# Note that none of the words can be repeated once used in any sentence
# Each word must have distinct letters

# Example:
    # Input: dictionary = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "afkpu", "bglqv", "chmrw", "dinsx", "ejoty"]
    # Output: [  ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy'], 
                #['abcde', 'fghij', 'klmno', 'pqrst', 'ejoty'], ...]

###########################################################################################################

# ✅ ALGORITHM: BACKTRACKING

def fiveLetterWords(dictionary):
    def isValidWord(word):
        return len(word) == 5 and len(set(word)) == 5
    
    def isValidSentence(sentence): # sentence is an array of words forming the sentence
        for word in sentence:
            if not isValidWord(word):
                return False
        
        return len(sentence) == 5 and len(set(sentence)) == 5
    
    result = [] # return value

    def backtrack(start, curr_sentence):
        if isValidSentence(curr_sentence):
            result.append(curr_sentence[:])
            return
        
        for i in range(start, len(dictionary)):
            curr_sentence.append(dictionary[i])
            backtrack(i+1, curr_sentence)
            curr_sentence.pop()
    
    backtrack(0, [])

    return result