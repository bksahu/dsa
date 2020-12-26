"""
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Example 1:

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'
Example 2:

Input: [3, -2, 0, 1, 2]
Output: 4
Example 3:

Input: [3, 2, 5, 1]
Output: 4
"""

def find_first_missing_positive(nums):
    i, n = 0, len(nums)
    while i < n:
        idx = nums[i]-1
        if 0 < nums[i] < n and nums[i] != nums[idx]:
            nums[i], nums[idx] = nums[idx], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i+1:
            return i+1
    return n+1
        

if __name__ == "__main__":
    print(find_first_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_missing_positive([3, 2, 5, 1]))
    print(find_first_missing_positive([1,2]))