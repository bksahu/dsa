"""
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Example 1:
Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]

Example 2:
Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]
"""
from heapq import heappush, heappop

# def top_k_numbers(nums, k):
#     heap = []
#     for num in nums:
#         heappush(heap, -num)
#     res = []
#     while k:
#         res += -heappop(heap),
#         k -= 1
#     return res

# def top_k_numbers(nums, k):
#     heap = []
#     for num in nums:
#         heappush(heap, num)
    
#     while len(heap) != k:
#         heappop(heap)
    
#     return heap

def top_k_numbers(nums, k):
    heap = []
    for i in range(k):
        heappush(heap, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heappop(heap)
            heappush(heap, nums[i])
    return heap

if __name__ == "__main__":
    print(top_k_numbers([3, 1, 5, 12, 2, 11], 3))
    print(top_k_numbers([5, 12, 11, -1, 12], 3))