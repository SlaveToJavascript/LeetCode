# https://leetcode.com/problems/find-the-duplicate-number
# MEDIUM
# Tags: linkedlistlc, arraylc, twopointerslc, #287

# GIVEN:
    # an array of integers nums containing n + 1 integers where each integer is in the range [1, n]
    # there is only one repeated number in nums

# TASK:
    # return this repeated number in nums
    # ! You must solve the problem without modifying the array nums and uses only constant extra space

# EXAMPLES:
    # Input: nums = [1,3,4,2,2]
    # Output: 2

    # Input: nums = [3,1,3,4,2]
    # Output: 3

###########################################################################################################

# ✅ ALGORITHM: FAST-SLOW POINTERS / FLOYD'S CYCLE DETECTION (TORTOISE-HARE) ALGORITHM
# STEP 1: initialize pointers
    # set 2 pointers, slow and fast, both to nums[0]
    # This is the starting point for both pointers
# STEP 2: move pointers + detect cycle
    # enter while-loop where slow moves 1 step at a time, while fast moves 2 steps, i.e.
        # slow = nums[slow]
        # fast = nums[nums[fast]]
        # NOTE: this simply means we take the nums element value that the pointer is pointing at (i.e. nums[fast] or nums[slow]), then convert this element value into index value and jump to this index value of nums
            # slow makes 1 such jump, while fast makes 2 such jumps
    # loop continues until both pointers meet at the same element in nums
        # Once a cycle is detected, algorithm breaks out of loop
        # NOTE: this meeting point is not necessarily the duplicate number (it's just a point inside the cycle)
        # *** WHY DOES THIS HAPPEN?
            # Because there is a duplicate number, there must be a cycle in the 'linked list' created by following nums[i] as next elements
# STEP 3: find the start of the cycle (which is the duplicate no.)
    # After identifying a meeting point inside the cycle,
        # reinitialize slow back to nums[0]
        # fast stays at the meeting point
    # Enter another while-loop where both pointers move one step at a time
        # *** The reason behind this is mathematical: according to Floyd's algorithm, when both pointers move at the same speed, they will eventually meet at the starting point of the cycle
            # This is the duplicate no. we're looking for!
# STEP 4: return duplicate no.
    # Finally, when slow and fast meet again, the meeting point will be the duplicate number, and we return it as the output

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def findDuplicate(nums):
    # 1) Initialize slow/fast pointers
    slow = nums[0]
    fast = nums[0]

    # 2) Detect cycle's intersection point
    while True:
        slow = nums[slow] # jump 1 step
        fast = nums[nums[fast]] # jump 2 steps
        if slow == fast: # slow and fast intersect at the same index
            break

    # 3) Find start of cycle (i.e. duplicate no.)
    slow = nums[0] # reinitialize slow back to 1st element in nums ; fast stays at intersection point
    while slow != fast:
        slow = nums[slow] # slow moves 1 step at a time
        fast = nums[fast] # fast moves 1 step at a time
        
    return slow # return either slow or fast, since they are at the same index now