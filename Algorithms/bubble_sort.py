"""
This script implements Bubble Sort Algorithm

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

import random


def bubbleSort(array):
    """returns sorted array"""
    length = len(array)
    for i in range(length):
        for j in range(length - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


if __name__ == "__main__":
    array = [random.randint(0, 100) for i in range(10)]
    print("Beofore Sort: ", array)
    print("After Sort: ", bubbleSort(array))
