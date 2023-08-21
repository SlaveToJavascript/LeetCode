# https://leetcode.com/problems/4sum/description/
# MEDIUM
# Tags: ksumlc, k-sumlc, 4 sum, k sum, twopointerslc, backtracklc, #18

# GIVEN:
    # an array, nums, of n integers

# TASK:
    # return an array of all the UNIQUE quadruplets [nums[a], nums[b], nums[c], nums[d]] such that nums[a] + nums[b] + nums[c] + nums[d] == target
    # NOTE: a, b, c, d must be distinct

# EXAMPLES:
    # Input: nums = [1,0,-1,0,-2,2], target = 0
    # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    # Input: nums = [2,2,2,2,2], target = 8
    # Output: [[2,2,2,2]]

###########################################################################################################

# ✅ ALGORITHM: RECURSIVE, K-SUM
# A recursive function that keeps picking the current element, then reducing the k to pick k-1 elements from the rest of the array, and at the same time reducing the target (to target-current element)
# Once k becomes 2, we can just do 2 sum
# PREVENTING DUPLICATES:
    # e.g. nums = [2,3,3], target = 5, k = 2
    # the 1st [2,3] is a valid triplet
    # -> right pointer (at 3) moves to the next element which is also 3
    # we already have [2,3] so we cannot have another [2,3]
    # to prevent duplicates, while next element is 3, we increase the right pointer until the element is not 3

# TIME COMPLEXITY: O(n^(k-1)) or O(n^3)
    # Worst case:
        # kSum(4, 0, target) takes O(n) time because of for-loop
        # inside this loop, kSum(3, i+1, target-nums[i]) takes O(n) time because of for-loop
        # inside that loop, kSum(2, i+1, target-nums[i]) takes O(n) time for the Two Sum II approach
        # -> TC = O(n^3)
# SPACE COMPLEXITY: O(n^3)

def fourSum(nums, target):
    nums.sort()
    result = [] # contains all unique quadruplets/k-plets that sum up to target
    current_quad = [] # current quadruplet/k-plet (if sum(current_quad) = target, append this current_quad to result)

    def kSum(k, start, target): # start is the starting index of the array where we search for k numbers
        if k > 2:
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]: # if current num = previous num, we skip current nums until current num != that previous num
                    continue # this is to prevent duplicates
                
                current_quad.append(nums[i]) # add current num to current quadruplet
                kSum(k-1, i+1, target-nums[i]) # continue looking for k-1 elements in the array excluding current num (since current num has been picked); target also reduces to target - current_num
                current_quad.pop()
            return
        
        # k = 2 -> use Two Sum II (two pointers approach)
        l, r = start, len(nums)-1
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else: # nums[l] + nums[r] = target
                current_quad.append(nums[l])
                current_quad.append(nums[r])
                result.append(current_quad)

                # after adding current l and r to result, if element at the next l is a duplicate of the current l, increase l pointer until we reach a non-duplicate
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
        
    kSum(4, 0, target) # if this is a k-sum problem instead of a 4-Sum problem, 4 would be replaced by k
    return result