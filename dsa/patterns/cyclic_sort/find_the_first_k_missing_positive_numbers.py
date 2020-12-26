"""
Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

Example 1:
Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.

Example 2:
Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.

Example 3:
Input: [-2, -3, 4], k=2
Output: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2.
"""
def find_first_k_missing_positive(nums, k):
    missingNumbers = []
    i = 0
    while i < len(nums):
        idx = nums[i]-1
        if 0 < idx < len(nums) and nums[i] != nums[idx]:
            nums[i], nums[idx] = nums[idx], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i+1 and k > 0:
            missingNumbers.append(i+1)
            k -= 1
    j = 1
    while k > 0:
        candidateNum = len(nums)+j
        if candidateNum not in nums:
            missingNumbers.append(candidateNum)
            k -= 1

        j += 1
    
    return missingNumbers


if __name__ == "__main__":
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))