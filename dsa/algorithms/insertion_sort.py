"""
This script implements Insertion Sort Algorithm

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

import random


def insertionSort(array):
    """returns sorted array"""
    length = len(array)
    for i in range(1, length):
        key = array[i]
        j = i - 1
        while(j>=0 and key < array[j]):
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

    return array


if __name__ == "__main__":
    array = [random.randint(0, 100) for i in range(10)]
    print("Beofore Sort: ", array)
    print("After Sort: ", insertionSort(array))
