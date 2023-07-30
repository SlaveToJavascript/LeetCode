# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
# MEDIUM
# Tags: heaplc, minheaplc, #373

# GIVEN:
    # 2 integer arrays, nums1 and nums2, sorted in increasing order
    # an integer k

# TASK:
    # Define a pair (u, v) which consists of 1 element from nums1 and 1 element from nums2
    # Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums

# EXAMPLES:
    # Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
    # Output: [[1,2],[1,4],[1,6]]
    # Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

    # Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
    # Output: [[1,1],[1,1]]
    # Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

    # Input: nums1 = [1,2], nums2 = [3], k = 3
    # Output: [[1,3],[2,3]]
    # Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

###########################################################################################################

# ✅ ALGORITHM 1: MIN HEAP
# Create a minHeap
    # every minHeap[i] = (sum, index_of_no._in_nums1, index_of_no._in_nums2)
# Create pairs between every element of nums1 and the 1st element in nums2
    # While creating these pairs, add them to the minHeap
# While minHeap is not empty and no. of pairs in result < k:
    # pop from minHeap and save the indexes of both elements popped -> this will be the min sum in heap
    # add the pair to result
    # since we already created pairs between every element in nums1 with 1st element in nums2, we only increment the popped index of nums2 by 1
    # if the new index for nums2 is within length range of nums2, push the new pair of popped index for nums1 and new index for nums2 into minHeap with their sum
# return result array

# TIME COMPLEXITY: O(n log n)
    # first for-loop = O(n1 log n1), n1 = len(nums1)
    # while-loop runs at most k times; each iteration takes O(log n) for the push operation, where n = length of heap => O(k log n)
# SPACE COMPLEXITY: O(n), for heap

from heapq import *

def kSmallestPairs(nums1, nums2, k):
    result = []
    minHeap = [] # minHeap[i] = (sum, index_of_no._in_nums1, index_of_no._in_nums2)

    # create pairs using every element of nums1 and the 1st element in nums2
    for i in range(len(nums1)):
        heappush(minHeap, (nums1[i] + nums2[0], i, 0)) # push each pair into minHeap
    
    # while minHeap not empty and no. of pairs checked < k,
    while minHeap and len(result) < k:
        pairSum, idx_nums1, idx_nums2 = heappop(minHeap) # pop from minHeap (this is the smallest sum)
        result.append([nums1[idx_nums1], nums2[idx_nums2]]) # add this smallest sum to result

        idx_nums2 += 1 # increment idx in nums2 by 1 since we already created pairs between every element in nums1 with 1st element in nums2

        if idx_nums2 < len(nums2): # if new idx in nums2 is within the range of nums2,
            heappush(minHeap, (nums1[idx_nums1] + nums2[idx_nums2], idx_nums1, idx_nums2)) # push the newly created pair into minHeap
    
    return result

#==========================================================================================================

# ✅ ALGORITHM 2: MIN HEAP + HASHSET FOR VISITED PAIRS
# Create a list, result, to store the pairs with smallest sums (this is the return value)
# Create a hashset, visited, to keep track of pairs that are seen
# Initialize minHeap that takes a triplet tuple of integers: sum of the pair, the index in nums1 of the 1st element of the pair, and index in nums2 of the 2nd element of the pair
# Push the sum and indexes of the 1st element in each nums1 and nums2 into minHeap, i.e. push (nums1[0] + nums2[0], 0, 0) into minHeap
# Also insert (0,0) into visited
# Iterate until we get k pairs in result array and minHeap is not empty:
    # Pop from minHeap and set i = popped index for nums1 and j = popped index for nums2
    # Add pair (nums1[i], nums2[j]) into result array
    # If i+1 < length of nums1 (i.e. index i+1 is within the nums1 range) and if the pair (i+1, j) is not in visited, we push a new pair nums1[i+1] + nums2[j] into the heap
    # If j+1 < length of nums2 (i.e. index j+1 is within the nums2 range) and if the pair (i, j+1) is not in visited, we push a new pair nums1[i] + nums2[j+1] into the heap
# return result array

# TIME COMPLEXITY: O( min(k log k, n1*n2 log (n1*n2)) )
    # We iterate O(min(k, n1*n2)) times to get the required no. of pairs
    # At each iteration we are pushing at most 2 pairs and popping 1 pair
        # each push into heap = O(log n)
    # So depending on whether minimum is k or n1*n2, the TC can either be O(k log k) or O(n1*n2 log (n1*n2))
# SPACE COMPLEXITY: O(min(k, n1*n2))
    # n1 and n2 are the lengths of nums1 and nums2 respectively
    # The visited set and heap can both grow up to a size of O(min(k, m*n)) because at each iteration we are inserting at most two pairs and popping one pair

def kSmallestPairs(nums1, nums2, k):
    result = []
    visited = set()

    minHeap = [(nums1[0] + nums2[0], 0, 0)]
    visited.add((0, 0))

    while minHeap and len(result) < k:
        val, i, j = heappop(minHeap)
        result.append([nums1[i], nums2[j]])

        if i+1 < len(nums1) and (i+1, j) not in visited: # if index i+1 is within the nums1 range AND the pair (i+1, j) is not in visited
            heappush(minHeap, (nums1[i+1] + nums2[j], i+1, j)) # create the new pair and push into heap
            visited.add((i+1, j)) # add new pair to visited

        if j+1 < len(nums2) and (i, j+1) not in visited: # if index j+1 is within the nums2 range AND the pair (i, j+1) is not in visited
            heappush(minHeap, (nums1[i] + nums2[j+1], i, j+1)) # create the new pair and push into heap
            visited.add((i, j+1)) # add new pair to visited
    
    return result