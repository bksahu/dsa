"""
Given an array of unsorted numbers and a target number, find a triplet in the array 
whose sum is as close to the target number as possible, return the sum of the triplet. 
If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Example 2:
Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Example 3:
Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
"""
def search_closes(nums, first, left, triplets, target):
    right = len(nums)-1
    triplets_sum = sum(triplets)
    triplets_diff = abs(triplets_sum - target)
    while left < right:
        current_sum = first + nums[left] + nums[right]
        current_diff = abs(current_sum - target)
        if current_diff < triplets_diff or (current_diff == triplets_diff and current_sum < triplets_sum):
            triplets = [first, nums[left], nums[right]]
            triplets_diff = current_diff
            triplets_sum = current_sum
        
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return triplets    

def solution(nums, target):
    nums.sort()
    triplets = [float("inf"), float("inf"), float("inf")]
    for i in range(len(nums)):
        triplets = search_closes(nums, nums[i], i+1, triplets, target)
    return triplets


if __name__ == "__main__":
    print(solution([-2, 0, 1, 2], 2))
    print(solution([-3, -1, 1, 2], 1))
    print(solution([1, 0, 1, 1], 100))