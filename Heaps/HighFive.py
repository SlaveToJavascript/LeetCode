# 1086. High Five
# https://leetcode.com/problems/high-five/description/
# EASY
# Tags: heaplc, minheaplc, premiumlc, #1086

# GIVEN:
    # a list of the scores of different students, items, where items[i] = [ID_i, score_i] represents one score from a student with ID_i

# TASK:
    # calculate each student's top five average
    # Return the answer as an array of pairs result, where result[j] = [ID_j, topFiveAverage_j] represents the student with ID_j and their top five average
    # Sort result by ID_j in increasing order
    # NOTE: A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division

# EXAMPLES:
    # Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    # Output: [[1,87],[2,88]]
    # Explanation: 
    # The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
    # The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.

    # Input: items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
    # Output: [[1,100],[7,100]]

###########################################################################################################

# ✅ ALGORITHM 1: MIN-HEAP
# Create a dictionary to store the scores of each student (key: student_id, value: min-heap (array) of scores)
# Iterate through the items and add each score to the respective min-heap
    # if the student's heap has more than 5 scores, pop the smallest score from the min heap (this ensures there will always be at most 5 scores in each student's min-heap)
# Iterate through the dictionary and calculate the average of the top 5 scores for each student

# TIME COMPLEXITY: O(n log n)
    # iterating over items array = O(n) time
    # heappush takes O(log k) time, where k = size of min-heap, but since len(min_heap) <= 5, it's O(log 5) = O(1) time
    # likewise for heappop = O(1) time
    # sorting hashmap keys take O(n log n) time in the worst case where there are n unique IDs
    # -> overall TC = O(n log n)
# SPACE COMPLEXITY: O(n)
    # for hashmap

from collections import defaultdict
from heapq import heappush, heappop

def highFive(items):
    scores = defaultdict(list) # key: student_id, value: min-heap of scores
    for id, score in items:
        heappush(scores[id], score) # add each score to the respective student's min-heap
        if len(scores[id]) > 5:
            heappop(scores[id]) # pop the smallest score from the min-heap if it has more than 5 scores
    
    result = []
    for id in sorted(scores.keys()): # sort the student IDs
        result.append([id, sum(scores[id])/5])
    
    return result