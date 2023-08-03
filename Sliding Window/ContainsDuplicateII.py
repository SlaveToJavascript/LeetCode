# https://leetcode.com/problems/contains-duplicate-ii/description/
# EASY
# Tags: hashmaplc, slidingwindowlc, #219

# GIVEN:
    # integer array, nums
    # integer, k

# TASK:
    # return true if there are two duplicate elements (at indexes i and j) where abs(i-j) <= k

# EXAMPLES:
    # Input: nums = [1,2,3,1], k = 3
    # Output: true

    # Input: nums = [1,0,1,1], k = 1
    # Output: true

    # Input: nums = [1,2,3,1,2,3], k = 2
    # Output: false

###########################################################################################################

# ❌ ALGORITHM 1: BRUTE FORCE
# Check if there are duplicates in every window where len(window) = k+1

# TIME COMPLEXITY: O(nk)

def containsNearbyDuplicate(nums, k):
    if len(nums) < 2:
        return False
    k = min(k, len(nums)-1)
    for end in range(k, len(nums)):
        start = end-k
        if len(set(nums[start:end+1])) != len(nums[start:end+1]):
            return True
    return False

#==========================================================================================================

# ✅ ALGORITHM 2: INDEX OF LAST OCCURRENCE HASHMAP
# Iterate nums, adding the key-value pair num:index into a hashmap if num not in hashmap
# if num in hashmap (i.e. there is duplicate), check if abs(current index of num - stored index of num in hashmap) <= k
    # if True, return True
    # else, update value of num in hashmap as current index (i.e. update index of last occurrence of num)
# return False

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def containsNearbyDuplicate(nums, k):
    hm = {} # stores the last index of every element occurrence
    for idx, num in enumerate(nums):
        if num in hm: # if there is duplicate
            if abs(idx-hm[num]) <= k: # condition is satisfied
                return True
            else: # the duplicate element is not within the window
                hm[num] = idx # update value of num in hashmap (i.e. last occurrence of index) as current index
        else:
            hm[num] = idx # add num to hashmap, with the key:value of num:index of num
    return False

#==========================================================================================================

# ✅ ALGORITHM 2: SLIDING WINDOW
# Set window as a hash set (to check for duplicates)
# set left and right pointers to indicate start and end of the window
# iterate nums
    # check if window length <= k+1
        # if false, remove the leftmost element in the window and increment left pointer by 1
    # check if element at right pointer is in window
        # if true, return True as there is a duplicate (i.e. current element of iteration is already in window)
        # else, add current element at right pointer to window
# return False

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(k)

def containsNearbyDuplicate(nums, k):
    window = set()
    left_pointer = 0

    for right_pointer in range(len(nums)):
        if right_pointer - left_pointer > k: # since desired condition: right-left <= k
            window.remove(nums[left_pointer]) # remove element at left pointer
            left_pointer += 1
        if nums[right_pointer] in window: # current element already exists in window -> there is duplicate
            return True
        else: # no duplicate
            window.add(nums[right_pointer]) # add element at right pointer to nums
    return False