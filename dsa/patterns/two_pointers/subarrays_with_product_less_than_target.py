"""
Given an array with positive numbers and a target number, find all of its contiguous 
subarrays whose product is less than the target number.

Example 1:

Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.
Example 2:

Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.
"""

def solution(arr, target):
    left = 0
    product = 1
    res = []
    for right in range(len(arr)):
        product *= arr[right]

        while product >= target and left < len(arr):
            product /= arr[left]
            left += 1

        temp = []
        for num in range(right, left-1, -1):
            temp.insert(0, arr[num])
            res.append(temp.copy())

    return res

if __name__ == "__main__":
    print(solution([2, 5, 3, 10], 30))
    print(solution([8, 2, 6, 5], 50))