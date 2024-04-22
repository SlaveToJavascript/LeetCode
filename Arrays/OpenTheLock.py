# 752. Open the Lock
# https://leetcode.com/problems/open-the-lock/description
# MEDIUM
# Tags: bfslc, #752

# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.
# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

# EXAMPLES:
    # Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
    # Output: 6
    # Explanation: 
    # A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
    # Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
    # because the wheels of the lock become stuck after the display becomes the dead end "0102".

    # Input: deadends = ["8888"], target = "0009"
    # Output: 1
    # Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".

    # Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
    # Output: -1
    # Explanation: We cannot reach the target without getting stuck.

###########################################################################################################

# ✅ ALGORITHM: BFS
# source "node" is "0000", and each "node" has 8 neighbors – +1 and -1 to each respective integer in the string
    # e.g. "1234" has neighbors "2234", "0234", "1334", "1134", "1244", "1224", "1235", "1233"
# use BFS to find the shortest path (i.e. no. of turns) to get from source to target

# TIME COMPLEXITY: O(n)
    # BFS visits each node once
# SPACE COMPLEXITY: O(n)
    # O(n) for queue
    # O(n) for visited set

def openLock(deadends, target):
    deadends = set(deadends)
    if "0000" in deadends:
        return -1 # if source is in deadends, we cannot turn the lock at all
    
    result = 0 # return value, i.e. min. no. of turns to get from source to target
    q = ["0000"]
    visited = set(["0000"])

    while q:
        for _ in range(len(q)):
            code = q.pop(0)
            if code == target:
                return result
            
            for i in range(4):
                for diff in [-1, 1]: # -1 from each char in code, +1 to each char in code
                    new_digit = (int(code) + diff) % 10 # % 10 implements wrap-around behavior (i.e. 9+1 becomes 0, and 0-1 becomes 9)
                    neighbor = code[:i] + str(new_digit) + code[i+1:]
                    if neighbor not in deadends and neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
        
        result += 1 # increment result AFTER processing each layer (each layer takes 1 turn)
    
    return -1 # if we reached this line, it means result still has not been returned in the code above -> no solution found