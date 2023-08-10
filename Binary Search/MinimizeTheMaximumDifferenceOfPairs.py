# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/
# MEDIUM
# Tags: binarysearchlc, #2616

# GIVEN:
    # integer array, nums
    # integer, p


# TASK:
    # Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized
    # Also, ensure no index appears more than once amongst the p pairs
    # TODO: Return the minimum maximum difference among all p pairs

# EXAMPLES:
    # Input: nums = [10,1,2,7,1,3], p = 2
    # Output: 1
    # Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
    # The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.

    # Input: nums = [4,2,1,2], p = 1
    # Output: 0
    # Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.

###########################################################################################################

# ✅ ALGORITHM: GREEDY + BINARY SEARCH
# Greedy: Define a helper function countValidPairs(threshold), where for a given threshold (e.g. 0), return the no. of pairs in nums where the absolute difference is <= threshold
# Binary search: do a binary search, from threshold = 0 to threshold = max difference of nums array
    # mid is the value of threshold – run countValidPairs(mid) to find no. of pairs whose difference = mid
    # if no. of pairs with difference = mid is greater than/equal to p, then we continue searching on the lower half (i.e. with a lower threshold) as we are trying to find the lowest possible threshold
    # else, if no. of pairs with difference = mid is less than p, it means our threshold has to be greater -> we continue searching for the threshold in the upper half (i.e. a higher threshold) where there are at least p pairs for said threshold

# TIME COMPLEXITY: O(n log n)
    # O(n log n) for sorting +
    # O(log n) for binary search
# SPACE COMPLEXITY: O(1)

def minimizeMax(nums, p):
    # Greedy
    def countValidPairs(threshold):
        num_pairs = 0
        i = 0

        while i < len(nums)-1:
            if nums[i+1] - nums[i] <= threshold: # if a pair's difference is at least threshold
                num_pairs += 1
                i += 2 # since this pair has been processed, we move to the element after the pair
            else:
                i += 1 # since this pair has a higher threshold, we move to the next pair
        
        return num_pairs
    
    nums.sort()

    # binary search
    l, r = 0, nums[-1] - nums[0] # r (upper bound) is the max possible difference in nums array
    while l < r:
        mid = (l+r) // 2
        if countValidPairs(mid) >= p: # if we at least have p pairs with this threshold,
            r = mid # we continue searching for the minimum mid in the lower half
        else:
            l = mid + 1 # threshold is higher -> we search for mid in the upper half
    
    return l # at this point, l = r so we can return l or return r