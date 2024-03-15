# 740. Delete and Earn
# https://leetcode.com/problems/delete-and-earn/description/
# MEDIUM
# Tags: dplc, hashmaplc, #740

# GIVEN:
    # an integer array, nums, of points that can be earned

# TASK:
    # maximize the no. of points earned by performing the following operation any no. of times:
        # Pick any nums[i] and delete it to earn nums[i] points
        # Afterwards, you must delete every occurrence of nums[i]-1 and nums[i]+1

# EXAMPLES:
    # Input: nums = [3,4,2]
    # Output: 6
    # Explanation: You can perform the following operations:
    # - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
    # - Delete 2 to earn 2 points. nums = [].
    # You earn a total of 6 points.

    # Input: nums = [2,2,3,3,3,4]
    # Output: 9
    # Explanation: You can perform the following operations:
    # - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
    # - Delete a 3 again to earn 3 points. nums = [3].
    # - Delete a 3 once more to earn 3 points. nums = [].
    # You earn a total of 9 points.

###########################################################################################################

# ✅ ALGORITHM 1A: DYNAMIC PROGRAMMING (ITERATIVE)
# HINT: If you take a number x, have to delete all x-1's and x+1's, so you might as well take all x's (to maximize no. of points earned)
    # therefore we can get the total points earned from deleting no. x = (frequency of x) * x
# let nums = sorted array of unique no.s in nums
# create a hashmap of each unique no. in nums mapped to its frequency
# create dp array, where each dp[i] = max possible points earned from deleting no.s up till nums[i]
# for each no. x in nums, points earned from deleting all occurrences of x = frequency of x (from hashmap) * x
    # if the no. before x is x-1, we can choose to either delete x or x-1 but not both -> dp[i] = max(dp[i-1], points from deleting x + dp[i-2])
        # because dp[i-2] = points earned from deleting up until nums[i-2] ; nums[i-2] can still be deleted even if nums[i] is deleted

# TIME COMPLEXITY: O(n log n)
    # for the sort function
# SPACE COMPLEXITY: O(n)
    # for hashmap and dp

from collections import Counter

def deleteAndEarn(nums):
    hm = Counter(nums)
    nums = sorted(list(set(nums))) # sorted array of unique no.s in nums

    dp = [0] * len(nums) # initiate dp with length of array of unique no.s
    for i in range(len(nums)):
        points = hm[nums[i]] * nums[i]
        if i > 0 and nums[i-1] == nums[i]-1:
            if i >= 2:
                points += dp[i-2]
            dp[i] = max(dp[i-1], points)
        elif i > 0:
            dp[i] = points + dp[i-1]
        else:
            dp[i] = points
    return dp[-1]

#==========================================================================================================

# ✅ ALGORITHM 1B: DYNAMIC PROGRAMMING (ITERATIVE)
# same as above algorithm but less verbose:
# HINT: If you take a number x, have to delete all x-1's and x+1's, so you might as well take all x's (to maximize no. of points earned)
# For each num in nums, add it to a hashmap as key and its corresponding value as frequency in nums
# Create integer array, dp, of length = no. of unique no.s in nums, where each dp[i] = max no. of points that can be earned up till i)
# But first, start by populating dp with total points earned from deleting each no.
    # i.e. each number (key) in dictonary * frequency (value) of that number
# also get a list, s, of unique sorted integers in nums (which should have the same length as dp)
# formula for each dp[i] (where dp[i] = max no. of points that can be earned up till i):
    # if s[i]-s[i-1] == 1, dp[i] = max(dp[i] + dp[i-2], dp[i-1])
    # else, dp[i] = dp[i] + dp[i-1]
# return the last element in dp

# TIME COMPLEXITY: O(n log n)
    # for the sort function
# SPACE COMPLEXITY: O(n)
    # for hashmap and dp

def deleteAndEarn(nums):
    if len(nums) == 1: 
        return nums[0] # if there's only 1 element, that element is directly returned since deleting it earns its points
    nums.sort()
    
    hm = Counter(nums) # hashmap of each unique no. in nums (as key) and their corresponding frequencies (as values)
    if len(hm) == 1:
        return list(hm)[0] * list(hm.values())[0] # if hashmap has only 1 number, i.e. nums only has 1 unique no., we return the product of that no. and its freq (i.e. total points earned from deleting all instances of that number)
    
    dp = [] # each dp[i] = max no. of points that can possibly be earned up till element at i
    for key in hm:
        dp.append(key * hm[key]) # initialize each dp[i] = nums[i] * frequency of nums[i] in nums
    
    s = sorted(list(hm)) # sorted array of unique no.s in nums
    dp[1] = max(dp[1], dp[0]) if s[1]-s[0]==1 else dp[1]+dp[0] # if 2nd unique no. (i.e. s[1]) is consecutive to the 1st, choose max between 1st and 2nd unique no.s ; otherwise, add up 1st and 2nd unique no.s
    
    for i in range(2, len(dp)):
        dp[i] = max(dp[i] + dp[i-2], dp[i-1]) if s[i]-s[i-1]==1 else dp[i]+dp[i-1] # if ith unique no. is consecutive to (i-1)th unique no., dp[i] = max(current points + 2nd previous points OR previous points) ; else (if difference between nums[i] and nums[i-1] is >= 2), dp[i] = current points + prev points
    
    return dp[-1]

#==========================================================================================================

# ✅ ALGORITHM 1C: DYNAMIC PROGRAMMING (ITERATIVE) – space optimized
# Since we technically only need to keep track of each dp[i] as well as its previous 2 dp values (i.e. dp[i-1] and dp[i-2]), we don't need to keep a dp array – we can just have 2 variables, points1 and points2, keeping track of the 2 previous values, and update them as we go
    # any dp value before that is not needed i our calculations
    # points1 = 2nd previous value to dp[i], points2 = 1st previous value to dp[i]
    # we will update points1 and points2 as we go -> eventually points2 will represent dp[-1] which is the return value!

# TIME COMPLEXITY: O(n log n)
    # for the sort function
# SPACE COMPLEXITY: O(n) 👍
    # sort() function uses O(n) time
    # BUT this space complexity is still more space optimized compared to the above 2 algorithms

def deleteAndEarn(nums):
    hm = Counter(nums)
    nums = sorted(list(set(nums)))

    points1, points2 = 0, 0 # points1 and points2 are 2 previous values of dp[i]
        # points1 = 2nd previous dp value
        # points2 = previous dp value
    for i in range(len(nums)):
        current_points = nums[i] * hm[nums[i]] # no. of points earned from deleting all instances of nums[i]
        
        # CASE 1: if difference between current no. vs prev no. = 1 -> we can choose to delete either current no. or previous no., but not both
        if i > 0 and nums[i-1] == nums[i] - 1:
            # update points1 and points2 by making points1 = points2 and points2 = current dp[i]
            temp = points2
            points2 = max(current_points + points1, points2)
            # "current_points + points1" = total points earned from deleting current no. + up until 2nd prev no.
            # "points2" = total points earned from deleting up until prev no.
            points1 = temp
        
        # CASE 2: if difference between current no. vs prev no. > 1 -> we can delete both current no. and previous no.
        else:
            temp = points2
            points2 = current_points + points2
            points1 = temp
        
    return points2 # eventually points2 will represent dp[-1] which is the return value