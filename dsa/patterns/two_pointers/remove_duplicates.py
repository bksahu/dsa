"""
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; 
after removing the duplicates in-place return the new length of the array.

Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
"""
# def solution(nums):
#     first, second = 0, 1

#     while second < len(nums):
#         if nums[first] == nums[second]:
#             del nums[second]
#         else:
#             first += 1
#             second += 1
#     return len(nums)

def solution(nums):
    nextNonDuplicate = 1

    i = 1
    while i < len(nums):
        if nums[nextNonDuplicate-1] != nums[i]:
            nums[nextNonDuplicate] = nums[i]
            nextNonDuplicate += 1
        i += 1
    return nextNonDuplicate

if __name__ == "__main__":
    print(solution([2, 3, 3, 3, 6, 9, 9]))
    print(solution([2, 2, 2, 11]))