"""
Given a sorted array of numbers, find if a given number ‘key’ is present in the array. 
Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. 
You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Example 1:
Input: [4, 6, 10], key = 10
Output: 2

Example 2:
Input: [1, 2, 3, 4, 5, 6, 7], key = 5
Output: 4

Example 3:
Input: [10, 6, 4], key = 10
Output: 0

Example 4:
Input: [10, 6, 4], key = 4
Output: 2
"""

def binary_search(nums, key):
    left, right = 0, len(nums)-1

    while left < right:
        mid = (left + right) >> 1
        if nums[left] < nums[right]:
            if nums[mid] < key:
                left = mid+1
            else:
                right = mid
        else:
            if nums[mid] > key:
                left = mid+1
            else:
                right = mid

    return left if 0 <= left < len(nums) else -1

if __name__ == "__main__":
    print(binary_search([4, 6, 10], key = 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], key = 5))
    print(binary_search([10, 6, 4], key = 10))
    print(binary_search([10, 6, 4], key = 4))
    print(binary_search([4, 4, 4], key = 4))