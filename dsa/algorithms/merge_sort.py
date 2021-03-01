"""
This script implements merge sorting algorithm
"""

import random

def mergeSort(array):
    l = len(array)

    if l <= 1:
        return array

    if l == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    mid = l//2
    firstHalf = mergeSort(array[:mid])
    secondHalf = mergeSort(array[mid:])
    return merge(firstHalf, secondHalf)

def merge(a, b):
    i, j = 0, 0
    ret = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ret += a[i],
            i += 1
        else:
            ret += b[j],
            j += 1

    while i < len(a):
        ret += a[i],
        i += 1

    while j < len(b):
        ret += b[j],
        j += 1

    return ret



if __name__ == "__main__":
    array = [random.randint(0, 9) for i in range(5)]
    print("Before Sort: ", array)
    print("After Sort: ", mergeSort(array))