# https://leetcode.com/problems/top-k-frequent-elements/
# MEDIUM

# GIVEN:
    # an integer array, nums
    # an integer k

# TASK:
    # return the k most frequent elements
    # You may return the answer in any order
    # NOTE: Time complexity must be better than O(n log n)
        # i.e. cannot use sorting of hashmap since TC of sorting hashmap = O(n log n)

# EXAMPLES:
    # Input: nums = [1,1,1,2,2,3], k = 2
    # Output: [1,2]

    # Input: nums = [1], k = 1
    # Output: [1]

###########################################################################################################

# ❌ ALGORITHM 1: HASHMAP + SORTING (exceeds O(n log n) time complexity)
# Create a hashmap from nums array where key = element, value = frequency of element in nums array
# Sort the hashmap by value in descending order (i.e. sort hashmap by maximum frequency of element)
# Return the top k elements in the sorted hashmap

# TIME COMPLEXITY: O(n log n) 👎
    # adding elements to hashmap = O(n)
    # sorting hashmap = O(n log n) 👎
    # NOTE: since question requires our TC to be better than O(n log n), this solution does not work!
# SPACE COMPLEXITY: O(n)

def topKFrequent(nums, k):
    hm = {}
    for num in nums:
        if num in hm:
            hm[num] += 1
        else:
            hm[num] = 1
    sorted_hm = sorted(hm.items(), key=lambda x:x[1], reverse=True)
    return [x[0] for x in sorted_hm[:k]]

#==========================================================================================================

# ✅ ALGORITHM 2: HASHMAP + HEAP
# Create a hashmap from nums array where key = element, value = frequency of element in nums array
# Create a min heap of size k

# TIME COMPLEXITY: O(n log k) if k < n and O(n) if k = n
# SPACE COMPLEXITY: O(n + k)
    # O(n) for hashmap + O(k) for heap with k elements

from collections import Counter
import heapq

def topKFrequent(nums, k):
    hm = Counter(nums)
    return heapq.nlargest(k, hm, key=hm.get) # returns n (n=k) largest elements in hm by value (hm.get(key) returns value of key in hm)

#==========================================================================================================

# ✅✅✅ ALGORITHM 3: HASHMAP + BUCKET SORT
# Create a hashmap from nums array where key = element, value = frequency of element in nums array
# Create a 2D array, frequency, where each nested array, frequency[i], in frequency = [numbers with frequency = i]
    # max length of frequency array = len(nums), i.e. if all numbers in nums are the same, the max possible frequency = len(nums)
    # e.g. if nums = [1, 1, 1, 2, 3, 3, 100], frequency = [ [], [2, 100], [3], [1], [], [], [] ]
        # explanation: 2 and 100 each appear 1 time in nums -> frequency[1] = [2,100]
                    #  3 appears 2 times in nums -> frequency[2] = [3]
                    #  1 appears 3 times in nums -> frequency[3] = [1]
                    # for frequency = 4, 5, 6, there are no no.s that appear 4/5/6 times, so frequency[i] where i = 4, 5 or 6 is empty

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
    # O(n) for hashmap + O(n) for frequency array

from collections import Counter

def topKFrequent(nums, k):
    hm = Counter(nums)
    frequency = [[] for i in range(len(nums)+1)]

    for num, freq in hm.items():
        frequency[freq].append(num)

    result = [] # return value
    for i in range(len(frequency)-1, 0, -1): # can end the iteration at i=0
        result += frequency[i]
        if len(result) >= k:
            return result