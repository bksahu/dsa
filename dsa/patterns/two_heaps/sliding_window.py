"""
Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.
"""

import heapq

class SlidingWindowMedian:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for x in range(len(nums) - k + 1)]

        for i in range(len(nums)):
            if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
                heapq.heappush(self.maxHeap, -nums[i])
            else:
                heapq.heappush(self.minHeap, nums[i])

            self.rebalance_heaps()

            if i - k + 1 >= 0:
                if len(self.maxHeap) == len(self.minHeap):
                    result[i - k + 1] = -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0 
                else:
                    result[i - k + 1] = -self.maxHeap[0] / 1.0

                elementToRemoved = nums[i - k + 1]
                if elementToRemoved <= -self.maxHeap[0]:
                    self.remove(self.maxHeap, -elementToRemoved)
                else:
                    self.remove(self.minHeap, elementToRemoved)

                self.rebalance_heaps()

        return result

    def remove(self, heap, element):
        ind = heap.index(element)
        heap[ind] = heap[-1]
        del heap[-1]

        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)

    def rebalance_heaps(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

if __name__ == "__main__":
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2
    )
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3
    )
    print("Sliding window medians are: " + str(result))
