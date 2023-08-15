# https://leetcode.com/problems/maximum-subsequence-score/description/
# MEDIUM
# Tags: heaplc, minheaplc, #2542

# GIVEN:
    # 2 integer arrays, nums1 and nums2, of equal length n
    # a positive integer, k

# TASK:
    # choose a subsequence of indices from nums1 of length k
    # For chosen indices i0, i1, ..., ik - 1,
        # score = sum(selected elements from nums1) * min(selected elements from nums2)
        # i.e. (nums1[i_0] + nums1[i_1] + ... + nums1[i_(k - 1)]) * min(nums2[i_0] , nums2[i_1], ... ,nums2[i_(k - 1)])
    # TODO: Return the maximum possible score

# EXAMPLES:
    # Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
    # Output: 12
    # Explanation: 
    # The four possible subsequence scores are:
    # - We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
    # - We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
    # - We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
    # - We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
    # Therefore, we return the max score, which is 12.

    # Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
    # Output: 30
    # Explanation: 
    # Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.

###########################################################################################################

# ✅ ALGORITHM: MIN HEAP
# Since we want to get max score, we should maximize each of the selected elements from nums1 and nums2
    # For nums2, since we only need the minimum of the selected elements, we should start finding the max score from the max element in nums2 -> this would ensure that min(selected elements from nums2) is maximized
# Create an array, pairs, where pairs (nums1[i], nums2[i]) are sorted by nums2[i] in decreasing order
# Create a min heap of max length = k, and add each nums1[i] into it; if length of min heap > k, we start popping the smallest elements from it
    # why add only nums1 elements to min heap? Because pairs are already sorted by nums2 elements in decreasing order, so for each new pair (nums1[i], nums2[i]) that we encounter, nums2[i] will be the minimum of all encountered pairs so far
    # so we should only focus on finding the k largest elements in nums1 to maximize score
    # after the process of: adding another nums1[i] to heap and popping from it whenever length of heap exceeds k, there will be k elements in heap and these are the k largest elements in nums1
# We keep track of the max score every time there are k elements in heap

# TIME COMPLEXITY: O(n log n)
    # n = length of nums1 or nums2
    # sorting pairs array takes O(n log n) time
    # We iterate each pair in pairs array, and for each iteration, we push into heap -> O(n) * O(log k)
        # each push operation takes O(log k) time because the max size of heap is k
# SPACE COMPLEXITY: O(n)
    # pairs array takes O(n) space
    # min heap, which has a max size of k, takes O(k) space

from heapq import heappush, heappop

def maxScore(nums1, nums2, k):
    pairs = [pair for pair in zip(nums1, nums2)] # combine the elements in nums1 and nums2 at each index i
        # pairs[i] = (nums1[i], nums2[i])
    pairs.sort(key=lambda x: x[1], reverse=True)

    n1sum = 0 # the sum of chosen elements from n1 so far
    max_score = 0 # return value
    min_heap = []

    for n1, n2 in pairs:
        heappush(min_heap, n1) # only need to push n1 to heap since we know current n2 is the minimum
        n1sum += n1 # sum of all n1 elements currently in heap

        if len(min_heap) > k: # if there are more than k elements in heap
            n1popped = heappop(min_heap) # pop the smallest n1 element in heap so far
            n1sum -= n1popped # subtract popped n1 element from sum of n1 elements in heap so far
        
        if len(min_heap) == k:
            max_score = max(max_score, n1sum * n2) # update max_score with current score

    return max_score