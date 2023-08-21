# https://leetcode.com/problems/top-k-frequent-words/description/
# MEDIUM
# Tags: hashmaplc, heaplc, maxheaplc, #692

# GIVEN:
    # an array of strings, words
    # an integer, k

# TASK:
    # return the k most frequent strings
    # Return the answer sorted by the frequency from highest to lowest
    # Sort the words with the same frequency by their lexicographical order

# EXAMPLES:
    # Input: words = ["i","love","leetcode","i","love","coding"], k = 2
    # Output: ["i","love"]
    # Explanation: "i" and "love" are the two most frequent words.
    # Note that "i" comes before "love" due to a lower alphabetical order.

    # Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
    # Output: ["the","is","sunny","day"]
    # Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

###########################################################################################################

# ✅ ALGORITHM 1: SORT HASHMAP BY 2 KEYS
# Create a hashmap of each word (key) -> the frequency of that word in words array (value)
# Sort the items in the hashmap by 2 keys: frequency (in descending order) and alphabetical (in ascending order)
# Return the words in the 1st k items in the sorted hashmap items

# TIME COMPLEXITY: O(n log n)
    # Counter(words) = O(n)
    # sorted() = O(n log n)
    # [:k] = O(k)
    # r[0] for r in top_k = O(k)
    # -> overall TC = O(n log n)
# SPACE COMPLEXITY: O(n)
    # O(n) for freq hashmap + O(n) for sorted list of unique words

from collections import Counter

def topKFrequent(words, k):
    freq = Counter(words) # creates hashmap where key = word -> value = frequency of that word in words array
    top_k = sorted(freq.items(), key=lambda x:(-x[1], x[0]))[:k] # sort items in hashmap by 2 keys: frequency (in descending order) and alphabetical lexicography (in ascending order) -> then retrieve top k elements after sorting
    return [r[0] for r in top_k] # return the words in those top k elements after sorted

#==========================================================================================================

# ✅ ALGORITHM 2: HEAP
# Create a hashmap of each word (key) -> the frequency of that word in words array (value)
# Create a max-heap with the elements (-freq, word)
    # This would ensure that the max frequency will be returned first
    # in case of a tie, the word will be returned in ascending order
# pop the first k elements from the heap

# TIME COMPLEXITY: O(n + k log n)
    # heappop() has a time complexity of O(log n) for each operation
    # we're popping k times
    # O(n) for creating freqMap
# SPACE COMPLEXITY: O(n)
    # O(n) for freq hashmap + O(n) for sorted list of unique words

import heapq

def topKFrequent(words, k):
    freqMap = Counter(words) # creates hashmap where key = word -> value = frequency of that word in words array
    maxheap = [(-freq, word) for word, freq in freqMap.items()]
    heapq.heapify(maxheap)
    
    return [heapq.heappop(maxheap)[1] for _ in range(k)] # pop and return the word in the 1st k elements from the heap