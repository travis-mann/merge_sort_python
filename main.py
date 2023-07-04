#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""main.py: inversion counter algorithm implementation"""


# --- metadata ---
__author__ = "Travis Mann"
__version__ = "1.0"
__maintainer__ = "Travis Mann"
__email__ = "tmann.eng@gmail.com"


# --- imports ---
from typing import List


# --- func ---
def merge(array_1: List[int], array_2: List[int], total_length: int) -> List[int]:
    """
    purpose: merge 2 arrays into one array in sorted ascending order
    :param array_1: 1st array to merge
    :param array_2: 2nd array to merge
    :return merged_array: array containing all elements in arrays 1 & 2 in sorted ascending order
    """
    array_1_index = 0
    array_2_index = 0
    merged_array = []
    for merged_array_index in range(total_length):
        # ensure array_1 has elements and either array 2 is out of elements or next element in array 1 is smaller
        if not (array_1_index == len(array_1)) and (
                array_2_index == len(array_2) or array_1[array_1_index] < array_2[array_2_index]):
            merged_array.append(array_1[array_1_index])
            array_1_index += 1
        else:
            merged_array.append(array_2[array_2_index])
            array_2_index += 1

    # output merged array and split count
    return merged_array


def merge_sort(array: List[int], length: int) -> List[int]:
    """
    purpose: merge sort algorithm using recursive divide and conquer to sort an array
    :param array: array to sort
    :return sorted_array: sorted array in ascending order
    """
    # base case
    if length == 1:
        return array

    # count left, right and split inversions
    sorted_A_half_1 = merge_sort(array[0:length // 2], len(array[0:length // 2]))
    sorted_A_half_2 = merge_sort(array[length // 2:], len(array[length // 2:]))
    sorted_A = merge(sorted_A_half_1, sorted_A_half_2, length)
    return sorted_A


# --- main ---
if __name__ == "__main__":
    array = [8, 1, 3, 5, 4, 7, 6, 9, 2]
    sorted_array = merge_sort(array, len(array))
    print(f'sorted_array: {sorted_array}')
