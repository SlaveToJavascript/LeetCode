# 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive/
# HARD
# Tags: arraylc, hashmaplc, #41

# GIVEN:
    # unsorted integer array, nums

# TASK:
    # Return the smallest positive integer that is not present in nums
    # NOTE: You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space

# EXAMPLES:
    # Input: nums = [1,2,0]
    # Output: 3

    # Input: nums = [3,4,-1,1]
    # Output: 2

    # Input: nums = [7,8,9,11,12]
    # Output: 1

###########################################################################################################

# ✅ ALGORITHM: MARK VISITED ELEMENTS IN INPUT ARRAY (CUSTOM HASHMAP) – THREE PASSES
# MAIN IDEA:
    # the smallest positive missing number, i, can only be in the range [1, n+1], where n = len(nums)
        # WHY? because it's not mathematically possible to have the smallest positive missing number > n+1 given that nums array is bounded by length n
        # e.g. nums = [1,2,3] -> smallest possible missing no. = 4, i.e. n+1
    # therefore, for each potential missing no. x in [1, n+1], the index x-1 is a valid index in nums -> nums[x-1] is a valid reference to an element in nums
        # we can use the index as our hash key, and the sign of the element (+ve / -ve) as a presence indicator
        # after marking visited no.s as -ve, if we want to check if a no. y exists in nums, we check if nums[y-1] is negative
            # if YES, then y exists in nums!
# STEPS:
    # 1. Replace all integers in nums array that are <= 0 or > n with a default value of n+1
        # i.e. we are removing -ve values, 0's, and no.s > n, bc they're not in the range [1, n+1]*** and hence they're not valid missing numbers -> we can ignore those no.s
            # this also ensures valid indexing, since valid indexes are in [0, n-1], s we replace out-of-bounds values with n+1 to ensure the "mark as visit" process only attempts to access valid indexes
            # *** n+1 is a valid missing no. but (n+1)-1 is NOT a valid index in nums, so we ignore it until the last line of code
    # 2. iterate nums array, and for every element x, mark nums[abs(x)-1] as visited (i.e. existing in nums array) by making it negative
        # if abs(x)-1 is not a valid array, skip it
            # e.g. if nums = [3,4,-1,1], then we mark nums[3-1] as visited, and nums[4-1] as visited, and so on
        # NOTE: need to use index = abs(x)-1 instead x-1 since we're marking visited num as -ve, so it's possible that num is -ve when we encounter it
    # 3. Iterate [1, n] inclusive (these are valid potential missing no.s), checking each no. x in [1, n] if nums[x-1] is positive
        # nums[x-1] is negative -> means we marked nums[x-1] as negative (i.e. visited, i.e. exists in nums array) previously -> x is not the missing no.
        # nums[x-1] is positive -> means nums[x-1] is not visited, i.e. not in nums array -> x is the missing no.!
            # RETURN x
    # 4. If nothing has been returned after the iteration, it means n+1 is the missing no., since this is the only no. we haven't iterated to yet -> RETURN n+1

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def firstMissingPositive(nums):
    n = len(nums)

    # 1. replace nums that are <= 0 and > n with the default value of n+1
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n+1
    
    # 2. mark visited elements in nums as -ve
    for i in range(n):
        index = abs(nums[i])-1 # need to use abs(nums[i]) instead of nums[i] since nums[i] may be -ve (if we marked it -ve previously)
        if 1 <= abs(nums[i]) <= n and nums[index] > 0:
            nums[index] *= -1
    
    # 3. for each element x in [1,n] inclusive, check if nums[x-1] is positive
        # if yes -> return x
    for x in range(1, n+1):
        if nums[x-1] > 0:
            return x
    
    # if we reached this point, it means the missing no. was not in [1,n], so the missing no. must be n+1
    return n+1