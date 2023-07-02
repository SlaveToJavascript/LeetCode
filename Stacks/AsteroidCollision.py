# https://leetcode.com/problems/asteroid-collision/
# MEDIUM

# GIVEN:
    # an array, asteroids, of integers representing asteroids in a row.
    # For each element (i.e. each asteroid), the absolute value represents its size
    # the sign represents its direction (positive meaning right, negative meaning left)
    # Each asteroid moves at the same speed.

# TASK:
    # Find out the state of the asteroids after all collisions
    # If two asteroids meet, the smaller one will explode
    # If both are the same size, both will explode
    # Two asteroids moving in the same direction will never meet

# EXAMPLES:
    # Input: asteroids = [5,10,-5]
    # Output: [5,10]
    # Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

    # Input: asteroids = [8,-8]
    # Output: []
    # Explanation: The 8 and -8 collide exploding each other.

    # Input: asteroids = [10,2,-5]
    # Output: [10]
    # Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

###########################################################################################################

# ✅ ALGORITHM 1: STACK
# Iterate the asteroids array
# if stack is empty, add current asteroid to array
# if stack not empty, check if current asteroid will clash with existing asteroid in stack
    # if existing asteroid in stack is positive and current asteroid is negative, they will clash (they are moving towards each other)
    # if existing asteroid in stack is negative and current asteroid is positive, they will not clash (they are moving away from each other)
# if existing asteroid in stack is smaller, it will get destroyed -> pop existing asteroid from stack
# else if current asteroid is smaller, it will get destroyed -> do not add current asteroid to stack
# else if both asteroids are the same size, they will both get destroyed -> pop existing asteroid from stack and do not add current asteroid to stack

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def asteroidCollision(asteroids):
    stack = []
    for current in asteroids:
        while stack and stack[-1] > 0 and current < 0: # existing asteroid is moving to the right and current asteroid is moving to the left -> clash
            if abs(stack[-1]) > abs(current): # current is smaller than existing -> current clashes
                # make current = 0 so it wouldn't be added to the array after the while loop
                current = 0
            elif abs(stack[-1]) < abs(current): # existing is smaller than current -> existing clashes
                stack.pop() # pop existing from stack
            else: # both current and existing destroyed
                current = 0 # make current = 0 so it wouldn't be added to the array after the while loop
                stack.pop() # pop existing from stack
        if current: # if (stack is empty) OR if (stack is not empty and current is not 0 i.e. not destroyed)
            stack.append(current) # add current asteroid to stack
    return stack