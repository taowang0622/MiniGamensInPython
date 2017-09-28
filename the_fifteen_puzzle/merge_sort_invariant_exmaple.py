"""
Examples of invariants
"""

###############################################################
# Invariants for loops
def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in both list1 and list2.

    This function can be iterative.
    """
    answer = []
    assert answer == sorted(answer)     # invariant

    idx1 = 0
    idx2 = 0
    while (idx1 < len(list1)) and (idx2 < len(list2)):
        if list1[idx1] < list2[idx2]:
            answer.append(list1[idx1])
            idx1 += 1
        elif list1[idx1] > list2[idx2]:
            answer.append(list2[idx2])
            idx2 += 1
        else:
            answer.append(list1[idx1])
            answer.append(list2[idx2])
            idx1 += 1
            idx2 += 1
        assert answer == sorted(answer)     # loop invariant

    answer.extend(list1[idx1:])
    answer.extend(list2[idx2:])

    assert answer == sorted(answer)     # invariant
    return answer


############################################
# Invariants for recursive functions

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <= 1:
        answer = list(list1)
        assert answer == sorted(answer)     # recursive invariant
        return answer

    mid = len(list1) // 2

    list_low = merge_sort(list1[0: mid])
    list_high = merge_sort(list1[mid:])

    answer = merge(list_low, list_high)
    assert answer == sorted(answer)     # recursive invariant
    return answer


def run_examples():
    """
    Run several examples
    """
    print "merge([1, 3, 5, 8], [2, 4, 10]) is", merge([1, 3, 5, 8], [2, 4, 10])

    print "merge_sort([4, 2, 1, 4, 6, 7, 2, 1]) is", merge_sort([4, 2, 1, 4, 6, 7, 2, 1])


run_examples()
