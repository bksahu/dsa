"""
Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. 
The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

Example 1:
Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]

Example 2:
Input: [1, 3, 8, 10, 15], key = 10
Output: [3, 3]

Example 3:
Input: [1, 3, 8, 10, 15], key = 12
Output: [-1, -1]
"""

def number_range(nums, key):
    start, end = -1, -1
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] < key:
            left = mid + 1
        else:
            right = mid
    start = left

    if nums[start] != key:
        return [-1, -1]
    
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left + right + 1) >> 1
        if nums[mid] > key:
            right = mid - 1
        else:
            left = mid 
    end = right

    return [start, end]

if __name__ == "__main__":
    print(number_range([4, 6, 6, 6, 9], key = 6))
    print(number_range([1, 3, 8, 10, 15], key = 10))
    print(number_range([1, 3, 8, 10, 15], key = 12))