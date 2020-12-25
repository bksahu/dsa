"""
Given an array of numbers which is sorted in ascending order and is rotated 
‘k’ times around a pivot, find ‘k’.

You can assume that the array does not have any duplicates.

Input: [10, 15, 1, 3, 8]
Output: 2
Explanation: The array has been rotated 2 times.

Input: [4, 5, 7, 9, 10, -1, 2]
Output: 5
Explanation: The array has been rotated 5 times.

Input: [1, 3, 8, 10]
Output: 0
Explanation: The array has been not been rotated.
"""

def rotation_count(nums):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = left + (right - left)//2

        if mid < right and nums[mid] > nums[mid+1]:
            return mid+1

        if mid > left and nums[mid-1] > nums[mid]:
            return mid

        if nums[left] < nums[mid]:
            left = mid + 1
        else:
            right = mid - 1 

    return 0 # not rotated

if __name__ == "__main__":
    print(rotation_count([10, 15, 1, 3, 8]))
    print(rotation_count([4, 5, 7, 9, 10, -1, 2]))
    print(rotation_count([1, 3, 8, 10]))

