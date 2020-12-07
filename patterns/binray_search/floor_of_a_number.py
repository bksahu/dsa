"""
Given an array of numbers sorted in ascending order, find the floor of a given number ‘key’. 
The floor of the ‘key’ will be the biggest element in the given array smaller than or equal to the ‘key’

Write a function to return the index of the floor of the ‘key’. If there isn’t a floor, return -1.

Example 1:
Input: [4, 6, 10], key = 6
Output: 1
Explanation: The biggest number smaller than or equal to '6' is '6' having index '1'.

Example 2:
Input: [1, 3, 8, 10, 15], key = 12
Output: 3
Explanation: The biggest number smaller than or equal to '12' is '10' having index '3'.

Example 3:
Input: [4, 6, 10], key = 17
Output: 2
Explanation: The biggest number smaller than or equal to '17' is '10' having index '2'.

Example 4:
Input: [4, 6, 10], key = -1
Output: -1
Explanation: There is no number smaller than or equal to '-1' in the given array.


1, 3, 8, 10, 15             12
0  1  2   3   4
"""
def search_floor_of_a_number(nums, key):
    left, right = 0, len(nums)-1
    if nums[0] > key:
        return -1

    while left < right:
        mid = (left + right + 1) >> 1
        if key < nums[mid]:
            right = mid - 1
        else:
            left = mid
    return left

if __name__ == "__main__":
    print(search_floor_of_a_number([4, 6, 10], key = 6))
    print(search_floor_of_a_number([1, 3, 8, 10, 15], key = 12))
    print(search_floor_of_a_number([4, 6, 10], key = 17))
    print(search_floor_of_a_number([4, 6, 10], key = -1))
    print(search_floor_of_a_number([3, 5], key = 4))