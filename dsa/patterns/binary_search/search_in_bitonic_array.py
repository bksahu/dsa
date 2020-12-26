"""
Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered bitonic if it is 
monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means 
that for any index i in the array arr[i] != arr[i+1].

Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

Example 1:
Input: [1, 3, 8, 4, 3], key=4
Output: 3

Example 2:
Input: [3, 8, 3, 1], key=8
Output: 1

Example 3:
Input: [1, 3, 8, 12], key=12
Output: 3

Example 4:
Input: [10, 9, 8], key=10
Output: 0
"""

def search_bitonic_array(arr, key):
    left, right = 0, len(arr)-1

    while left < right:
        mid = left + (right - left)//2

        if arr[mid] > arr[mid+1]:
            right = mid 
        else:
            left = mid + 1

    res = binary_search(arr, key, 0, left)
    if res != -1:
        return res

    return binary_search(arr, key, left+1, len(arr)-1)

def binary_search(arr, key, left, right):
    while left <= right:
        mid = left + (right - left)//2

        if arr[mid] == key:
            return mid
        elif arr[left] < arr[right]:
            if key < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if key > arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return -1

if __name__ == "__main__":
    print(search_bitonic_array([1, 3, 8, 4, 3], key=4))
    print(search_bitonic_array([3, 8, 3, 1], key=8))
    print(search_bitonic_array([1, 3, 8, 12], key=12))
    print(search_bitonic_array([10, 9, 8], key=10))