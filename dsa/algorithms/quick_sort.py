"""
This following code implements quick sort algorithm
"""
import random

def quickSort(arr):
    if len(arr) < 2:
        return arr

    # 0 is the pivot
    smallerThanPivotIdx = 0

    for i in range(1, len(arr)):
        if arr[i] < arr[0]:
            smallerThanPivotIdx += 1
            arr[i], arr[smallerThanPivotIdx] = arr[smallerThanPivotIdx], arr[i]
    
    # since now smallerThanPivotIdx is pointing to last element smaller than pivot
    # we now put pivot in it's right position
    arr[smallerThanPivotIdx], arr[0] = arr[0], arr[smallerThanPivotIdx]

    return quickSort(arr[:smallerThanPivotIdx]) + [arr[smallerThanPivotIdx]] + quickSort(arr[smallerThanPivotIdx+1:])
    

if __name__ == "__main__":
    array = [10, 5, 8, 9, 3, 6, 15, 12, 16]
    print("Before Sort: ", array)
    print("After Sort: ", quickSort(array))