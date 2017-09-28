"""
Infrastructure code for Word Wrangler game
"""

import urllib2
# import sys

import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    new_list = []
    temp = 2**31 - 1        # maximum integer!!!
    for elem in list1:
        if elem != temp:
            temp = elem
            new_list.append(elem)
    return new_list


def binary_search(lst, target):
    """
    search target in the range of [lo, hi) of the list
    :param lst: must be sorted
    :param target:
    :return: found=>true, not found=>false
    """
    low = 0
    high = len(lst)
    while low < high:
        mid = low + ((high - low) >> 1)  # use shift operation rather than division for speed
        if lst[mid] == target:
            return True
        elif lst[mid] > target:  # enter the front sub-list [lo, mid)
            high = mid
        else:  # enter the back sub-list [mid + 1, hi)
            low = mid + 1
    return False


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    return [elem for elem in list1 if binary_search(list2, elem)]


# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    merged_list = []
    index1 = len(list1) - 1
    index2 = len(list2) - 1
    while (index1 != -1) and (index2 != -1):
        if list1[index1] > list2[index2]:
            merged_list.insert(0, list1[index1])
            index1 -= 1
        elif list1[index1] < list2[index2]:
            merged_list.insert(0, list2[index2])
            index2 -= 1
        else:
            merged_list.insert(0, list1[index1])
            index1 -= 1
            merged_list.insert(0, list2[index2])
            index2 -= 1
    if(index1 == -1 and index2 != -1):
        return list2[:(index2 + 1)] + merged_list
    if(index2 == -1 and index1 != -1):
        return list1[:(index1 + 1)] + merged_list
    return merged_list


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <= 1:     # trivial case===>the list with only one element is ordered by nature
        return list1
    mid = len(list1) >> 1
    return merge(merge_sort(list1[:mid]), merge_sort(list1[mid:]))


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    all_substrs = []
    if word == "":
        return [word]
    first_letter = word[0]
    sol_to_subprob = gen_all_strings(word[1:])
    all_substrs = all_substrs +  sol_to_subprob
    for substr in sol_to_subprob:
        all_substrs.append(first_letter + substr)
        for index in range(len(substr)):
            all_substrs.append(substr[:(index + 1)] + first_letter + substr[(index + 1):])
    return all_substrs


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    file_obj = open(filename, 'r')
    return [line[:-1] for line in file_obj.readlines()]


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)


# Uncomment when you are ready to try the game
run()
# print "remove duplicate elememts:", remove_duplicates([1, 2, 3, 4, 4, 4, 5, 5, 6, 7, 8, 8])
# print "binarySearch", binarySearch([1, 2, 3, 4, 5], 5)
# print "binarySearch", binarySearch([1, 2, 3, 4, 5], -1)
# print "binarySearch", binarySearch([], 10)
# print "intersect", intersect([1, 2, 3, 4], [0, 0, 1, 2])
# print "intersect", intersect([1, 2, 3, 4], [0, 0, 2, 2])
# print "intersect", intersect([1, 2, 3, 4], [0, 0, 2, 2, 3, 3, 4, 5, 6])
# print "intersect", intersect([1, 2, 3, 4], [])
# print "merge", merge([-3, -2, 0, 3, 5, 10, 20], [1, 3, 4, 8, 12, 31])
# print "merge", merge([], [1, 3, 4, 8, 12, 31])
# print "merge", merge([], [])
# print "mergeSort", merge_sort([2, 45, 32, 2, 5, 7, 34, 1313])
# print "mergeSort", merge_sort([])
# print "genAllStrs", gen_all_strings("aab")
# print "readLines", load_words(WORDFILE)