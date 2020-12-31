"""
Given an unsorted array of numbers, find Kth smallest number in it.
Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

Example 1:
Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

Example 2:
Input: [1, 5, 12, 2, 11, 5], K = 4
Output: 5
Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].

Example 3:
Input: [5, 12, 11, -1, 12], K = 3
Output: 11
Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].
"""

from heapq import heappush, heappop

# def kth_smallest_number(nums, k): 
#     # TC: O(n + klogn)
#     # SC: O(n)
#     heap = []
#     for num in nums:
#         heappush(heap, num)
    
#     return heap[k-1]

def kth_smallest_number(nums, k):
    # TC: O(nlogk)
    # SC: O(k) 
    heap = []
    for i in range(k):
        heappush(heap, -nums[i])

    for i in range(k, len(nums)):
        if nums[i] < -heap[0]:
            heappop(heap)
            heappush(heap, -nums[i])
    
    return -heap[0]

if __name__ == "__main__":
    print(kth_smallest_number([1, 5, 12, 2, 11, 5], 3))
    print(kth_smallest_number([1, 5, 12, 2, 11, 5], 4))
    print(kth_smallest_number([5, 12, 11, -1, 12], 3))