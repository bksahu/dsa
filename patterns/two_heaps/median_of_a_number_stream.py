"""
Design a class to calculate the median of a number stream. The class should have the following two methods:

insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.
"""

from heapq import heappush, heappop

class MedianOfAStream:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def insertNum(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self):
        if len(self.minHeap) == len(self.maxHeap):
            return self.minHeap[0] / 2.0 + -self.maxHeap[0] / 2.0
        return -self.maxHeap[0]/1.0
 
if __name__ == "__main__":
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insertNum(3)
    medianOfAStream.insertNum(1)
    print("The median is: " + str(medianOfAStream.findMedian()))
    medianOfAStream.insertNum(5)
    print("The median is: " + str(medianOfAStream.findMedian()))
    medianOfAStream.insertNum(4)
    print("The median is: " + str(medianOfAStream.findMedian()))
