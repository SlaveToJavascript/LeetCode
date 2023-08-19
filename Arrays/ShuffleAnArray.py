# https://leetcode.com/problems/shuffle-an-array/description/
# MEDIUM
# Tags: designlc, #384

# GIVEN:
    # an integer array, nums
    # NOTE: All the elements of nums are unique

# TASK: 
    # design an algorithm to randomly shuffle the array
    # All permutations of the array should be equally likely as a result of the shuffling
    # Implement the Solution class:
        # Solution(nums) Initializes the object with the integer array nums.
        # reset() Resets the array to its original configuration and returns it.
        # shuffle() Returns a random shuffling of the array.

# EXAMPLES:
    # Input
    # ["Solution", "shuffle", "reset", "shuffle"]
    # [[[1, 2, 3]], [], [], []]
    # Output
    # [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

    # Explanation
    # Solution solution = new Solution([1, 2, 3]);
    # solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
    #                        // Any permutation of [1,2,3] must be equally likely to be returned.
    #                        // Example: return [3, 1, 2]
    # solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
    # solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

###########################################################################################################

# ✅ ALGORITHM 1: BRUTE FORCE (my solution)
# Use random.choice(array) repeatedly, each time to select an element from array
# Every time random.choice(array) is called, remove the selected element from array before calling it again
# add the randomly selected elements into a new array and return it

# TIME COMPLEXITY: O(n^2)
    # shuffle() function uses a for-loop and in each iteration of for-loop, the array.remove() functions takes O(n) time -> O(n^2)
# SPACE COMPLEXITY: O(n)
    # new array created for randomly selected elements and new array to randomly select elements from (we remove selected elements from this array)

import random

class Solution(object):

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums
        
    def shuffle(self):
        array = [] # array of randomly selected values; to be returned
        select_from = self.nums[:] # this is the array we select random elements from and then delete these selected elements from; it is a deep copy of self.nums array

        for _ in range(len(self.nums)):
            rand = random.choice(select_from)
            array.append(rand)
            select_from.remove(rand) # remove the selected element from select_from array after selecting it
        
        return array
    
#==========================================================================================================

# ✅ ALGORITHM 2: RANDOM + MERGE SORT
# Generate a list of values between 0 and 1; this list has the same size as nums
# Create an integer array of indexes from 0 to len(nums)-1
# We sort this array of indexes according to the corresponding array of random values between 0-1 – the index corresponding to the smallest value between 0 and 1 will now be the first element after the sort, and so on
    # e.g. if random array of vals = [0.4, 0.2, 0.6, 0.5] 
              # and random indexes = [0,   1,   2,   3],
   # after sorting, random indexes = [1,   0,   3,   2]
# We then use the sorted array of indexes to shuffle the nums array according to the position of their corresponding indexes in the randomized random index array

# TIME COMPLEXITY: O(n log n)
    # TC depends on sorting algorithm used; if we use merge sort, TC = O(n log n)
# SPACE COMPLEXITY: O(n)
    # extra space for rand_values and rand_indexes

def shuffle(arr):
    rand_values = [random.random() for _ in range(len(arr))]
    rand_indexes = [i for i in range(len(arr))]
    rand_indexes.sort(key=lambda i: rand_values[i])
    arr = [arr[i] for i in rand_indexes]

#==========================================================================================================

# ✅ ALGORITHM 3: FISHER-YATES SHUFFLE
# Shuffle the array in-place; the array is split into 2 parts: unshuffled elements on the left, shuffled elements which will be on the right
# Make a copy of the self.nums array (we shouldn't change anything on self.nums as we need it for reset() function)
# Create a last_unshuffled_index which points to the last element in the array that is unshuffled
    # all elements including it and to its right are unshuffled; all elements on its left are shuffled
# Each time, randomly select an element index between 0 and last_unshuffled_index (inclusive) -> this will be the index of our selected element
# Swap places for the number at last_unshuffled_index and the selected index
# Return the array

def shuffle(nums):
    array = nums[:] # make a deep copy of nums before we make any changes to the copy
    
    last_unshuffled_idx = len(array)-1

    while last_unshuffled_idx > 0: # while unshuffled index hasn't reached the first element
        random_idx = random.randint(0, last_unshuffled_idx) # randomly select an index up to and including unshuffled index
        if random_idx != last_unshuffled_idx:
            array[random_idx], array[last_unshuffled_idx] = array[last_unshuffled_idx], array[random_idx]
        last_unshuffled_idx -= 1
    
    return array