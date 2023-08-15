# https://leetcode.com/problems/search-suggestions-system/description
# MEDIUM
# Tags: trieslc, twopointerslc, #1268

# GIVEN:
    # an array of strings, products
    # a string, searchWord

# TASK:
    # Design a system that suggests at most 3 product names from products after each character of searchWord is typed
    # Suggested products should have common prefix with searchWord
    # If there are more than 3 products with a common prefix, return the 3 lexicographically minimum products
    # Return a list of lists of the suggested products after each character of searchWord is typed

# EXAMPLES:
    # Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
    # Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
    # Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
    # After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
    # After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

    # Input: products = ["havana"], searchWord = "havana"
    # Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
    # Explanation: The only word "havana" will be always suggested while typing the search word.

###########################################################################################################

# ✅✅✅ ALGORITHM 1: SORT WORDS LIST + TWO POINTERS
# Sort the products array -> this sorts the words in the array alphabetically
    # after sorting, the words that have a common prefix would all be consecutive in the products array
# Maintain l and r pointers that point to the 1st and last words in products array respectively
# Iterate through every char in searchWord, to generate all prefix strings of searchWord and search for the words in products array that start with these prefix strings
# if word at current l pointer in products array does not have the current prefix, we increment l pointer until we find a word in products array that has the current prefix
# if word at current r pointer in products array does not have the current prefix, we decrement r pointer until we find a word in products array that has the current prefix
# now, the words at l and r pointers in products array both start with current prefix
# if there are 3 or more words between and including the l and r pointers, append the top 3 words to output array
# else, if there are 2 or less words between and including the l and r pointers, append the words between and including l and r pointers to output array

# TIME COMPLEXITY: O(nlogn + n*m) = O(nlogn)
    # n = len(products)
    # m = len(searchWord)
    # O(n log n) = sorting products array
    # O(n*m) = iterating through every char in searchWord and searching for words in products array that start with the current prefix
# SPACE COMPLEXITY: O(n)
    # n = len(products)
    # O(n) = sorting products array

def suggestedProducts(products, searchWord):
    products.sort() # sort products word array alphabetically

    l, r = 0, len(products)-1
    result = [] # return value

    for i in range(len(searchWord)):
        words = [] # this array holds the words (max 3) that start with the current suffix, i.e. searchWord[i+1]

        while l <= r and products[l][:i+1] != searchWord[:i+1]: # while current word at pointer l doesn't start with current suffix searchWord[:i+1],
            l += 1 # increment the l pointer until a word that starts with current suffix is found
        
        while l <= r and products[r][:i+1] != searchWord[:i+1]: # while current word at pointer r doesn't start with current suffix searchWord[:i+1],
            r -= 1 # decrement the r pointer until a word that starts with current suffix is found

        # at this point, both l and r would be pointing to a word in products array that starts with current suffix

        for j in range(min(3, r-l+1)): # if there are less than 3 words between and including l and r pointers, the words between and at l and r pointers will be added; else if there are more than/equal to 3 words, then we add 3 words
            words.append(products[l+j]) # we add the top 3 or less words in products array, starting at l pointer
        result.append(words)
    
    return result

#==========================================================================================================

# ✅ ALGORITHM 2: TRIE