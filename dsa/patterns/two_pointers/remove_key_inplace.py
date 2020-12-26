"""
Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ 
in-place and return the new length of the array.

Example 1:
Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].

Example 2:
Input: [2, 11, 2, 2, 1], Key=2
Output: 2
Explanation: The first two elements after removing every 'Key' will be [11, 1].
"""

# def solution(nums, k):
#     key_count = 0

#     for num in nums:
#         if num == k:
#             key_count += 1

#     return len(nums) - key_count
    
def solution(nums, k):
    final_len, i = 0, 0

    while i < len(nums):
        if nums[i] != k:
            final_len += 1
        i += 1
    return final_len

if __name__ == "__main__":
    print(solution([3, 2, 3, 6, 3, 10, 9, 3], 3))
    print(solution([2, 11, 2, 2, 1], 2))
    print(solution([2,1], 2))