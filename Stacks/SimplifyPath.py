# https://leetcode.com/problems/simplify-path/description
# MEDIUM
# Tags: stacklc, #71

# Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
# In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.
# The canonical path should have the following format:
    # The path starts with a single slash '/'.
    # Any two directories are separated by a single slash '/'.
    # The path does not end with a trailing '/'.
    # The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
# Return the simplified canonical path.

# EXAMPLES:
    # Input: path = "/home/"
    # Output: "/home"
    # Explanation: Note that there is no trailing slash after the last directory name.

    # Input: path = "/../"
    # Output: "/"
    # Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

    # Input: path = "/home//foo/"
    # Output: "/home/foo"
    # Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

###########################################################################################################

# ✅ ALGORITHM: STACK
# MAIN IDEA:
    # if segment = ".", ignore and continue to next segment
    # if segment = "..", pop the last segment from stack (unless last segment is root directory)
    # if segment = "//", replace it with "/"
    # for everything else, push segment to stack

def simplifyPath(path):
    path = path.split('/') # path becomes array of segments
    stack = []

    for segment in path:
        if segment == "." or segment == "":
            continue # ignore current segment and go to next segment
        elif segment == '..':
            if stack:
                stack.pop() # pop last segment from stack (if last segment is root, stack would be empty)
        else:
            stack.append(segment)
    
    return "/" + "/".join(stack) # canonical path always starts with /