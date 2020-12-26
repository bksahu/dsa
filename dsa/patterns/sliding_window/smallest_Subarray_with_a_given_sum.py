"""
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest 
contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Example 2:
Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Example 3:
Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
"""

def smallest_sub_sum(nums, s):
    winStart, winEnd = 0, 0
    minLen = float("inf")
    currSum = 0

    while winEnd < len(nums):
        currSum += nums[winEnd]

        while currSum >= s:
            minLen = min(minLen, winEnd - winStart + 1)
            currSum -= nums[winStart]
            winStart += 1

        winEnd += 1
    
    return 0 if minLen == float("inf") else minLen 

if __name__ == "__main__":
    print(smallest_sub_sum([2, 1, 5, 2, 3, 2], 7))
    print(smallest_sub_sum([2, 1, 5, 2, 8], 7))
    print(smallest_sub_sum([3, 4, 1, 1, 6], 16))

