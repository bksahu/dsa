"""
Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, 
find if a given ‘key’ is present in it.

Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. 
You can assume that the given array does not have any duplicates.

Input: [10, 15, 1, 3, 8], key = 15
Output: 1
Explanation: '15' is present in the array at index '1'.

Input: [4, 5, 7, 9, 10, -1, 2], key = 10
Output: 4
Explanation: '10' is present in the array at index '4'.
"""

# def search_rotated_array(nums, key):
#     left, right = 0, len(nums)-1

#     if nums[left] < nums[right]:
#         return binary_search(nums, left, right, key)
#     else:
#         while left <= right:
#             mid = left + (right - left)//2
#             if nums[mid] > nums[mid+1]: # mid is pivot
#                 break

#             if nums[mid] < nums[mid-1]: # mid - 1 is pivot
#                 mid = mid - 1
#                 break

#             if nums[mid] < nums[left]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
        
#         if nums[mid] == key:
#             return mid
#         elif nums[mid] > key:
#             return binary_search(nums, mid+1, right, key)
#         else:
#             return binary_search(nums, left, mid-1, key)

# def binary_search(nums, left, right, key):

#     while left <= right:
#         mid = left + (right - left)//2
#         if nums[mid] == key:
#             return mid
#         elif nums[mid] < key:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1

def search_rotated_array(nums, key):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = left + (right - left)//2

        if nums[mid] == key:
            return mid

        if nums[left] < nums[mid]: # first half is sorted
            if nums[left] <= key < nums[mid]:
                right = mid - 1
            else: # key is in the second half
                left = mid + 1
        else: # right half is sorted
            if nums[mid] < key <= nums[right]:
                left = mid + 1
            else: # key is in the first half
                right = mid - 1
        
    return -1



if __name__ == "__main__":
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))

