# Google technical screen
# 29 March 2024
# https://leetcode.com/discuss/interview-question/1671654/google-onsite-new-grad-checks-for-groups-of-three-values-within-d-distance-of-one-another
# Tags: binarysearchlc, googlelc, interviewlc

# Your task is to write a function that given a distance d and a stream of floating point values received one at a time, checking for groups of three values that are within at most d distance.
# As values are received they should be stored in memory.
# Whenever any group is found meeting the distance criteria, return the three values and remove them from memory.
# REAL-WORLD EXAMPLE:
# Imagine you are standing at an incoming conveyor belt of items that need to be packaged into boxes of exactly three items that all fit together (means that all items are within distance d of each other) and placed on a second, outgoing, conveyor belt
# You have sufficient storage space to place items off to the side while you wait for a full triplet that all fit together.
# Conveyor belt items are floating point numbers.

###########################################################################################################

# ✅ ALGORITHM 1: SORT + BINARY SEARCH

# TIME COMPLEXITY: O(n log n)
    # for sorting
# SPACE COMPLEXITY: O(n)

import bisect

class ConveyerBeltSystem:
    def __init__(self, d):
        self.d = d
        self.items = []

    def process_item(self, item):
        bisect.insort(self.items, item) # Insert the item while maintaining the sorted order

        # Try to find a group of three items that fit together
        for i in range(len(self.items)-2):
            if self.items[i+2] - self.items[i] <= self.d: # Found a valid group
                group = self.items[i:i+3]
                del self.items[i:i+3] # remove them from the list
                return group
        
        return None # if no group is found, return None



# EXAMPLE USAGE
system = ConveyorBeltSystem(d=1.0)
stream = [1.2, 2.5, 3.1, 1.8, 2.2, 4.0]

for item in stream:
    group = system.process_item(item)
    if group:
        print(f"Group packaged: {group}")