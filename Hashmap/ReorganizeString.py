# https://leetcode.com/problems/reorganize-string/description/
# MEDIUM
# Tags: heaplc, maxheaplc, hashmaplc, #767

# GIVEN:
    # a string, s

# TASK:
    # rearrange the characters of s so that any two adjacent characters are not the same
    # TODO: Return any possible rearrangement of s or return "" if not possible

# EXAMPLES:
    # Input: s = "aab"
    # Output: "aba"

    # Input: s = "aaab"
    # Output: ""

###########################################################################################################

# ✅ ALGORITHM: MAX-HEAP
# 1. Create a hashmap of each character in s and its corresponding frequency
# 2. Create a max heap of the hashmap chars and respective counts
    # max_heap[i] = (count, char)
# 3. Pop the top element from the heap (which has the largest count)
# 4. If the popped char is equals to the last char in result, pop another element (char) from heap and push the 1st popped char back into heap
# 4. Decrement the popped char's count value by 1 and add them back to the heap if count > 0 (after decrement)
# 5. Repeat the above popping until heap is empty

# TIME COMPLEXITY: O(n log k)
    # n is the length of s
    # k is the no. of unique chars in s
# SPACE COMPLEXITY: O(k)
    # Counter(s) hashmap has max size of k (no. of unique chars in s)
    # heap has max size of k

from collections import Counter
from heapq import heapify, heappop, heappush

def reorganizeString(s):
    max_heap = [(-count, char) for char, count in Counter(s).items()]
    heapify(max_heap)
    result = ""
    
    while max_heap:
        count, char = heappop(max_heap)
        if result == "" or result[-1] != char: # if last char in result is not the same as popped char
            count = -count
        else: # if last char in result is the same as popped char, we need to find a different char to add to result
            if not max_heap: # if max_heap is empty at this point, there are no other unique chars to add
                return ""
            count2, char2 = heappop(max_heap) # pop a different char from heap
            heappush(max_heap, (count, char)) # push the 1st popped char back into heap
            count, char = -count2, char2
        result += char # add popped char to result
        if count - 1 > 0: # push the char and its count back into heap if count > 0
            heappush(max_heap, (-(count-1), char))
    
    return result