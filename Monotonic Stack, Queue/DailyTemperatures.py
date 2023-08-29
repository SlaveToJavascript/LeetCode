# https://leetcode.com/problems/daily-temperatures/
# MEDIUM
# Tags: monotonicstacklc, monotoniclc, stacklc, #739

# GIVEN:
    # an array of integers, temperatures, which represents the daily temperatures
    # temperatures[i] is the temperature on the ith day

# TASK:
    # return an array, answer, where answer[i] is the number of days you have to wait after the ith day to get a warmer temperature
    # If there is no future day for which this is possible, set answer[i] == 0

# EXAMPLES:
    # Input: temperatures = [73,74,75,71,69,72,76,73]
    # Output: [1,1,4,2,1,1,0,0]

    # Input: temperatures = [30,40,50,60]
    # Output: [1,1,1,0]

    # Input: temperatures = [30,60,90]
    # Output: [1,1,0]

###########################################################################################################

# ❌ APPROACH 1: BRUTE FORCE
# Iterate temperatures array
# For each element i in temperatures, iterate through all the elements behind it to find the index of the 1st element that is greater than i
# if a higher number is found, append the index difference to answer array
# else, if a higher element is not found on the right of element i, append 0 to the answer array

# TIME COMPLEXITY: O(n^2)
    # n = len(temperatures)
    # for each element in the array, we are iterating over all elements on its right to find the next higher element
# SPACE COMPLEXITY: O(n)
    # for answer array of size n

def dailyTemperatures(temperatures):
    answer = [] # return value

    for i in range(len(temperatures)):
        higher_found = False # if a higher element on the right of i is found, this would be True
        
        for j in range(i, len(temperatures)): # iterate elements on the right of i
            if temperatures[j] > temperatures[i]: # if a higher temperature is found,
                higher_found = True
                answer.append(j-i) # append index differences to answer
                break
        
        if not higher_found: # if higher temperature is not found,
            answer.append(0) # append 0 to answer
    
    return answer

#==========================================================================================================

# ✅ APPROACH 2: DECREASING MONOTONIC STACK
# Create a stack where stack[i] = (temperature, index)
    # stack will be decreasing -> when we get any temp that is greater than the temp at the top of stack, we keep popping from stack until the temp @ top of stack >= current temp
# Iterating through temperatures array, if we find a temp that is greater than temp at the top of stack, we keep popping from stack until the temp @ top of stack >= current temp
    # for each popped temperature at index i, we fill up answer[i] = index of the current temp - i
        # this is the no. of days between popped temp and current temp (which is higher than popped temp)
    # after we finish popping, we append the current temp to stack
# if current temp <= temp @ top of stack, we add current temp to stack without popping
# NOTE: we don't have to do anything if there are no higher temperatures on the right for the ith temperature, since the answer was already initialized to an array of 0's
# return the answer array

# TIME COMPLEXITY: O(n)
    # n = len(temperatures)
#SPACE COMPLEXITY: O(n)
    # max length of stack = n

def dailyTemperatures(temperatures):
    stack = [] # stack[i] = (temperature, index)
    answer = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]: # while stack is not empty and current temp is greater than temp @ top of stack,
            popped_temp, popped_idx = stack.pop() # pop from stack (this popped temp is lower than current temp)
            answer[popped_idx] = i - popped_idx # the no. of days after popped temp when a higher temp was encountered
        
        stack.append((temp, i)) # append current temp to stack
    
    return answer