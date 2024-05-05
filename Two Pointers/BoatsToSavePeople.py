# 881. Boats to Save People
# https://leetcode.com/problems/boats-to-save-people/
# MEDIUM
# Tags: twopointerslc, greedylc, #881

# GIVEN:
    # an array, people, where people[i] is the weight of the i'th person, and an infinite number of boats where each boat can carry a maximum weight of limit
    # Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit

# TASK:
    # Return the minimum number of boats to carry every given person

# EXAMPLES:
    # Input: people = [1,2], limit = 3
    # Output: 1
    # Explanation: 1 boat (1, 2)

    # Input: people = [3,2,2,1], limit = 3
    # Output: 3
    # Explanation: 3 boats (1, 2), (2) and (3)

    # Input: people = [3,5,3,4], limit = 5
    # Output: 4
    # Explanation: 4 boats (3), (3), (4), (5)

###########################################################################################################

# ✅ ALGORITHM: TWO POINTERS
# Greedy: the lightest person should pair with the heaviest person, the 2nd lightest person pairs with the 2nd heaviest person, and so on
# sort the array, and use 2 pointers pointing to the 1st (lightest) and last (heaviest) people
# if the combined weight of the 2 people <= limit, shift both pointers inward and result+1
# else, add only the heavier person (on the right) to the boat -> shift r pointer to the left, result+1
# eventually, if l=r, result+1 since we need 1 more boat for this one last person

# TIME COMPLEXITY: O(n log n)
    # sorting
# SPACE COMPLEXITY: O(n)
    # sort() takes O(n) space

def numRescueBoats(people, limit):
    people.sort()
    result = 0

    l, r = 0, len(people)-1
    while l < r:
        if people[l] + people[r] <= limit:
            l += 1
            r -= 1
        else:
            r -= 1
        result += 1
    
    if l == r:
        result += 1 # add 1 more boat to result for the last person at people[l]
    
    return result