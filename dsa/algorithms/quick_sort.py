"""
This following code implements quick sort algorithm
"""

def quickSortLeft(arr):
    # leftmost element is the pivot
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

    return quickSortLeft(arr[:smallerThanPivotIdx]) + \
            [arr[smallerThanPivotIdx]] + \
            quickSortLeft(arr[smallerThanPivotIdx+1:])

def quickSortRight(arr, left, right):
    # rightmost element is the pivot
    if left < right:
        pivotIdx = partion(arr, left, right)
        quickSortRight(arr, left, pivotIdx-1)
        quickSortRight(arr, pivotIdx+1, right)

def partion(arr, left, right):
    if left < right:
        smallerThanPivotIdx = left - 1
        for i in range(left, right):
            if arr[i] <= arr[right]:
                smallerThanPivotIdx += 1
                arr[i], arr[smallerThanPivotIdx] = arr[smallerThanPivotIdx], arr[i]

        arr[right], arr[smallerThanPivotIdx+1] = arr[smallerThanPivotIdx+1], arr[right]
        return smallerThanPivotIdx + 1

if __name__ == "__main__":
    array = [10, 5, 8, 9, 3, 6, 15, 12, 16]
    print("Before Sort: ", array)
    print("After Sort (Left as pivot): ", quickSortLeft(array.copy()))

    print("Before Sort: ", array)
    quickSortRight(array, 0, len(array)-1)
    print("After Sort (Right as pivot): ", array)
