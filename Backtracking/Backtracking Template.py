# From https://gist.github.com/RuolinZheng08/cdd880ee748e27ed28e0be3916f56fa6

# validates if a state can be used as a final solution
# e.g. a state is a valid solution if all N queens are placed on a board and none of them can attack each other
def is_valid_state(state):
    return True

# this function returns a list of candidates that can be used to construct the next state
def get_candidates(state):
    return []

# a recursive function that calls the above 2 functions and checks if the state is a valid solution to backtracking problem
# if it is, it records the solution by making a deep copy of the state
# NOTE: we need a deep copy instead of a shallow copy as we will continue to modify the state as the search goes, but we need a static snapshot of the valid state here
def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
        # return

    # if the state isn't yet a valid solution, we find candidates to build the next state
    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)

# This is the main function that returns the valid solutions; other functions above are helper functions
def solve():
    solutions = []
    state = set()
    search(state, solutions)
    return solutions