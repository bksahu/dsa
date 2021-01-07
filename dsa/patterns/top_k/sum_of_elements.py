"""
Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

Example 1:
Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
Output: 23
Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
between 5 and 15 is 23 (11+12).

Example 2:
Input: [3, 5, 8, 7], and K1=1, K2=4
Output: 12
Explanation: The sum of the numbers between the 1st smallest number (3) and the 4th smallest 
number (8) is 12 (5+7).
"""

from heapq import heappop, heapify

def sumOfElements(nums, k1, k2):
    if not nums or k2 < k1: return -1
    sum = 0
    minHeap = nums.copy()
    heapify(minHeap)

    currIndex = 1
    while minHeap and currIndex < k2:
        num = heappop(minHeap)
        if currIndex > k1:
            sum += num
        currIndex += 1

    return sum



if __name__ == "__main__":
    print(sumOfElements([1, 3, 12, 5, 15, 11], 3, 6))
    print(sumOfElements([3, 5, 8, 7], 1, 4))