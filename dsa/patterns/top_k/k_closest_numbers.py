"""
Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. 
Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

Example 1:
Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]

Example 2:
Input: [2, 4, 5, 6, 9], K = 3, X = 6
Output: [4, 5, 6]

Example 3:
Input: [2, 4, 5, 6, 9], K = 3, X = 10
Output: [5, 6, 9]
"""

from heapq import heappush, heappop

# TC: O(nlogn) SP: O(k)
# def kClosestNumbers(nums, k, x):
#     if x <= nums[0]: return nums[:k]
#     if x >= nums[-1]: return nums[len(nums) - k:]

#     minHeap = []
#     for num in nums:
#         if len(minHeap) == k:
#             if abs(x - minHeap[0]) > abs(x - num):
#                 heappop(minHeap)
#             else:
#                 continue
#         heappush(minHeap, num)

#     return minHeap

# TC: O(n) SP: O(1)
def kClosestNumbers(nums, k, x):
    left, right = 0, len(nums)-1
    while (right - left >= k):
        if abs(nums[left] - x) > abs(nums[right] - x):
            left += 1
        else:
            right -= 1

    return [nums[i] for i in range(left, right+1)]

if __name__ == "__main__":
    print(kClosestNumbers([5, 6, 7, 8, 9], 3, 7))
    print(kClosestNumbers([2, 4, 5, 6, 9], 3, 6))
    print(kClosestNumbers([2, 4, 5, 6, 9], 3, 10))
    print(kClosestNumbers([2, 4, 5, 10, 11], 3, 5))
    print(kClosestNumbers([2, 4, 5, 6, 9], 3, 1))
    print(kClosestNumbers([1,2,5,5,6,6,7,7,8,9], 7, 7))
    
