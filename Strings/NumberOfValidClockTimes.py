# 2437. Number of Valid Clock Times
# https://leetcode.com/problems/number-of-valid-clock-times/description/
# EASY
# Tags: stringlc, #2437

# GIVEN:
    # string of length 5 called time, representing the current time on a digital clock in the format "hh:mm"
        # The earliest possible time is "00:00" and the latest possible time is "23:59"

# TASK:
    # In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a digit from 0 to 9
    # Return an integer answer, i.e. the number of valid clock times that can be created by replacing every ? with a digit from 0 to 9

# EXAMPLES:
    # Input: time = "?5:00"
    # Output: 2
    # Explanation: We can replace the ? with either a 0 or 1, producing "05:00" or "15:00". Note that we cannot replace it with a 2, since the time "25:00" is invalid. In total, we have two choices.

    # Input: time = "0?:0?"
    # Output: 100
    # Explanation: Each ? can be replaced by any digit from 0 to 9, so we have 100 total choices.

    # Input: time = "??:??"
    # Output: 1440
    # Explanation: There are 24 possible choices for the hours, and 60 possible choices for the minutes. In total, we have 24 * 60 = 1440 choices.

###########################################################################################################

# ✅ ALGORITHM: 4 NESTED FOR-LOOPS
# for a time in the format "h1 h2 : m1 m2", these are the no. of possible options at each char:
    # "h1" can be from 0-2 -> there are 3 possible options
    # "h2" can be from 0-9 -> there are 10 possible options
    # "m1" can be from 0-5 -> there are 6 possible options
    # "m2" can be from 0-9 -> there are 10 possible options
# if any char is not "?", there is only 1 possible option

# TIME COMPLEXITY: O(1)
    # there are 4 nested for-loops, each with a constant no. of iterations
    # in the worst case, the nested loops will iterate 3 x 10 x 6 x 10 = 1,800 times
# SPACE COMPLEXITY: O(1)
    # the space used by the variables is constant

def countTime(time):
    # if char is not "?", we use an array with a single element (e.g. [4], [5], etc.) so that in the for-loops below, these single-digit arrays would still work
    h1 = range(3) if time[0] == '?' else [int(time[0])]
    h2 = range(10) if time[1] == '?' else [int(time[1])]
    m1 = range(6) if time[3] == '?' else [int(time[3])]
    m2 = range(10) if time[4] == '?' else [int(time[4])]
    
    total = 0
    
    for h in h1:
        for hh in h2:
            for m in m1:
                for mm in m2:
                    if f"{h}{hh}:{m}{mm}" <= "23:59": # f-string is used to create a string from the variables
                        # this is a lexicographical comparison of the string created from the variables, with the string "23:59"
                        total += 1
    
    return total