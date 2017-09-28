"""
A simple recursive solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""

MAX_REMOVE = 3


# recursive solver with no memoization

def evaluate_position(current_num):
    """
    Recursive solver for Nim
    "Recursion is divine and powerful", so we can assume this function has been implemented and within that implementation there's a lot of complex logic!!!!!
    What we need to pay attention is just input and output, in this case, we can assume that the implementation can determine who the current player is by input, so we can get the expected output!!!!

    The most applications of Tree are searching and sorting, and they're both based on tree traversal!!!!!!
    and note that tree traversal is linear!!!!!so we must determine one kind of order to traverse the tree, like pre-order, in-order, post-order, breath-first.......!!

    time complexity: O(3^n)
    """
    global counter
    counter += 1

    # if current_num <= 0:
    #     return "lost"
    for removed_num in range(1, min(MAX_REMOVE + 1, current_num + 1)):
        new_num = current_num - removed_num
        if evaluate_position(new_num) == "lost":
            return "won"
    return "lost"


def run_standard(items):
    """
    Encapsulate code to run regular recursive solver
    """
    global counter
    counter = 0
    print
    print "Standard recursive version"
    print "Position with", items, "items is", evaluate_position(items)
    print "Evaluated in", counter, "calls"



# memoized version with dictionary

def evaluate_memo_position(current_num, memo_dict):
    """
    Memoized version of evaluate_position
    memo_dict is a dictionary that stores previously computed results

    Using memoization collapses the exponential method's tree to a graph, so its complexity is O(n)!!!!!
    """
    global counter
    counter += 1

    for removed_num in range(1, min(MAX_REMOVE + 1, current_num + 1)):
        new_num = current_num - removed_num
        # maintain the dictionary for memoization
        if new_num in memo_dict:
           result = memo_dict[new_num]
        else:
            result = evaluate_memo_position(new_num, memo_dict)
            memo_dict[new_num] = result
        # get the result of the original problem according to the results of subproblems
        if result == "lost":
            return "won"
    return "lost"


def run_memoized(items):
    """
    Run the memoized version of the solver
    """
    global counter
    counter = 0
    print
    print "Memoized version"
    print "Position with", items, "items is", evaluate_memo_position(items, {0: "lost"})
    print "Evaluated in", counter, "calls"


# dynamic programming version using tabulation!!!
def evaluate_DP_position(current_num):
    table = {0:"lost"} # initialize the table
    for num in range(1, current_num + 1):
        result = "lost"
        for removed_num in range(1, min(MAX_REMOVE + 1, num + 1)):
            new_num = num - removed_num
            if table[new_num] == "lost":
                result = "won"
        table[num] = result # maintain the table
    return table[current_num]

def run_DP(items):
    """
    Run the DP version of the solver
    """
    print
    print "DP version"
    print "Position with", items, "items is", evaluate_DP_position(items)

run_standard(19)
run_memoized(19)
run_DP(19)
