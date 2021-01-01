"""
Design a class to efficiently find the Kth largest element in a stream of numbers.

The class should have the following two things:

The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
The class should expose a function add(int num) which will store the given number and return the Kth largest number.

Example 1:
Input: [3, 1, 5, 12, 2, 11], K = 4
1. Calling add(6) should return '5'.
2. Calling add(13) should return '6'.
2. Calling add(4) should still return '6'.
"""

from heapq import heappush, heappop

# class KthLargestNumberInStream:
#     def __init__(self, nums, k):
#         self.k = k
#         self.maxHeap = []
#         self._heapify(nums)

#     def _heapify(self, nums):
#         for num in nums:
#             heappush(self.maxHeap, -num)

#     def add(self, num):
#         heappush(self.maxHeap, -num)
#         return self._getKthLargestNumber()

#     def _getKthLargestNumber(self):
#         tempHeap = self.maxHeap.copy()
#         k = self.k

#         kthLargestNumber = -1
#         while tempHeap and k:
#             kthLargestNumber = heappop(tempHeap)
#             k -= 1

#         return -kthLargestNumber
            
class KthLargestNumberInStream:
    minHeap = []
    def __init__(self, nums, k):
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, num):
        heappush(self.minHeap, num)

        if len(self.minHeap) > self.k:
            heappop(self.minHeap)

        return self.minHeap[0]


if __name__ == "__main__":
    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print(kthLargestNumber.add(6))
    print(kthLargestNumber.add(13))
    print(kthLargestNumber.add(4))
