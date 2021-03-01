"""
This script implements Selection Sort Algorithm

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

import random


def selectionSort(array):
    """returns sorted array"""
    length = len(array)
    for i in range(length - 1):
        unsortedElementIdx = i
        minElementIdx = i+1
        for j in range(i+1, length):
            if array[j] < array[minElementIdx]:
                minElementIdx = j

        if array[minElementIdx] < array[unsortedElementIdx]:
            array[minElementIdx], array[unsortedElementIdx] = array[unsortedElementIdx], array[minElementIdx]

    return array


if __name__ == "__main__":
    array = [random.randint(0, 100) for i in range(10)]
    print("Before Sort: ", array)
    print("After Sort: ", selectionSort(array))
