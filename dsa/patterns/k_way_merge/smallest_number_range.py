"""
Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.

Example 1:
Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
Output: [4, 7]
Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.

Example 2:
Input: L1=[1, 9], L2=[4, 12], L3=[7, 10, 16]
Output: [9, 12]
Explanation: The range [9, 12] includes 9 from L1, 12 from L2 and 10 from L3.
"""

from heapq import heappush, heappop

def find_smallest_range(nums):
    rangeStart, rangeEnd = 0, float('inf')
    currMaxNum = float("-inf")
    minHeap = []
    
    for i, num in enumerate(nums):
        heappush(minHeap, (num[0], 0, nums[i]))
        currMaxNum = max(currMaxNum, num[0])
        
    while len(minHeap) == len(nums):
        num, i, arr = heappop(minHeap)
        if rangeEnd - rangeStart > currMaxNum - num:
            rangeEnd = currMaxNum
            rangeStart = num
            
        if len(arr) > i+1:
            heappush(minHeap, (arr[i+1], i+1, arr))
            currMaxNum = max(currMaxNum, arr[i+1])
            
    return [rangeStart, rangeEnd]

if __name__ == "__main__":
    print(find_smallest_range([[1,5,8], [4,12], [7,8,10]]))