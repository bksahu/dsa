"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
"""

def search_pair(nums, target, left, triplets):
    right = len(nums)-1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            triplets.append([-target, nums[left], nums[right]])
            right -= 1
            left += 1
            while left < right and nums[left] == nums[left-1]: left+= 1
            while left < right and nums[right] == nums[right-1]: right-= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return triplets


def solution(nums):
    nums.sort()
    triplets = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        search_pair(nums, -nums[i], i+1, triplets)

    return triplets

if __name__ == "__main__":
    print(solution([-3, 0, 1, 2, -1, 1, -2]))
    print(solution([-5, 2, -1, -2, 3]))
    print(solution([-2,0,1,1,2]))
    