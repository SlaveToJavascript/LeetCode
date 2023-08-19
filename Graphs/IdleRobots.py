# AWS Software Development Engineer Full-Time Opportunity (Online Assessment)
# Tags: graphlc, amazon

# A robot with coordinates (x, y) is said to be idle if it has a robot located above, below, left, and right of it
# It is guaranteed that no two robots are at the same location
# TODO: Given the locations of n robots where the x- and y-coordinates of the ith robot is (x[i], y[i]), find the number of idle robots

# EXAMPLE:
    # x = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
    # y = [1, 2, 3, 1, 2, 3, 5, 1, 2, 3]
    # The 10 robots are arranged as follows:

    # 5       x
    # 4
    # 3   x   X   x
    # 2   x   X   x
    # 1   x   x   x
    # 0   1   2   3

    # where each x is a robot and X is an idle robot
        # The robot at (2, 2) is idle because it has robots at (1, 2), (3, 2), (2, 3), and (2, 1) directly to the left, right, up, and down respectively
        # The robot at (2, 3) is idle because it has robots at (1, 3), (3, 3), (2, 5), and (2, 2) directly to the left, right, up, and down respectively
    # There are 2 idle robots in this arrangement

###########################################################################################################

# ✅ ALGORITHM: MAP X TO Ys AND Y TO Xs

from collections import defaultdict

def countIdleRobots(x, y):
    robots = set() # get the x-y coordinates of each robot
    for i in range(len(x)):
        robots.add((x[i], y[i]))

    x_to_ys = defaultdict(set) # key = x[i], value = {all y-coords that share the same x-coord x[i]}
    y_to_xs = defaultdict(set) # key = y[i], value = {all x-coords that share the same y-coord y[i]}
    for i in range(len(x)):
        x_to_ys[x[i]].add(y[i])
        y_to_xs[y[i]].add(x[i])
    print(x_to_ys)

    for i in x_to_ys:
        x_to_ys[i].sort()
    for i in y_to_xs:
        y_to_xs[i].sort()
    
    def has_neighbor(coord, direction): # returns True if robot at coord has a neighbor in specified direction (left/right/up/down)
        xi, yi = coord
        if direction == "left":
            return any(x < xi for x in y_to_xs[yi])
        if direction == "right":
            return any(x > xi for x in y_to_xs[yi])
        if direction == "up":
            return any(y > yi for y in x_to_ys[xi])
        if direction == "down":
            return any(y < yi for y in x_to_ys[xi])
    
    idle_robots = 0

    for robot in robots:
        if has_neighbor(robot, "left") and has_neighbor(robot, "right") and has_neighbor(robot, "up") and has_neighbor(robot, "down"):
            idle_robots += 1
    
    return idle_robots