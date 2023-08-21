# https://www.lintcode.com/problem/3620/
# EASY
# Tags: hashmaplc, designlc, #359

# Design a logger system that receives a stream of messages along with its timestamps
# Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10)
# All messages will come in chronological order. Several messages may arrive at the same timestamp.
# Implement the Logger class:
    # Logger(): Initializes the logger object.
    # shouldPrintMessage(int timestamp, string message): Returns true if the message should be printed in the given timestamp, otherwise returns false

# EXAMPLE:
    # Logger logger = new Logger();

    # logging string "foo" at timestamp 1
    # logger.shouldPrintMessage(1, "foo"); returns true; 

    # logging string "bar" at timestamp 2
    # logger.shouldPrintMessage(2, "bar"); returns true;

    # logging string "foo" at timestamp 3
    # logger.shouldPrintMessage(3, "foo"); returns false;

    # logging string "bar" at timestamp 8
    # logger.shouldPrintMessage(8, "bar"); returns false;

    # logging string "foo" at timestamp 10
    # logger.shouldPrintMessage(10, "foo"); returns false;

    # logging string "foo" at timestamp 11
    # logger.shouldPrintMessage(11, "foo"); returns true;

    # Explanation:
        # [1,foo]  => message "foo" needs to be printed at time  1, when the queue for message "foo" is empty and can be printed, return true
        # [2,bar]  => message "bar" needs to be printed at time  2, when the queue for message "bar" is empty and can be printed, return true
        # [3,foo]  => message "foo" needs to be printed at time  3, when the queue for message "foo" is not empty (predecessor moment 1 is still in progress), so it cannot be printed, return false
        # [8,bar]  => message "bar" needs to be printed at time  8, when the queue for message "bar" is not empty (predecessor moment 2 is still in progress), so it can't be printed, false
        # [10,foo] => message "foo" needs to be printed at time 10, when the queue for message "foo" is not empty (predecessor moment 1 is still in progress), so it cannot be printed, return false
        # [11,foo] => message "foo" needs to be printed at time 11, when the queue for message "foo" is empty (predecessor moment 1 has finished at moment 11), so it can be printed, return true

###########################################################################################################

# ✅ ALGORITHM: HASHMAP

# Create a hashmap to store the message and its timestamp
# If the message is not in the hashmap, add it and return True
# If the message is in the hashmap, check if the timestamp is greater than or equal to the previous timestamp + 10
# If it is, update the timestamp and return True
# If it is not, return False

from collections import defaultdict

class Logger:
    def __init__(self):
        self.timestamps = defaultdict(int)

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.timestamps:
            self.timestamps[message] = timestamp
            return True
        
        if timestamp >= self.timestamps[message] + 10:
            self.timestamps[message] = timestamp
            return True
        
        return False