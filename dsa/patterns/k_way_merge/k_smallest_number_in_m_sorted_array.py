"""
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Example 1:
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged 
list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Example 2:
Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7.
"""
from heapq import heappush, heappop

def find_kth_smallest(lists, k):
    minHeap = []
    for i, l in enumerate(lists):
        heappush(minHeap, (l[0], 0, i))

    while minHeap and k:
        currNum, currNumIdx, currListIdx = heappop(minHeap)
        k -= 1
        if currNumIdx+1 < len(lists[currListIdx]):
            heappush(minHeap, (lists[currListIdx][currNumIdx+1], currNumIdx+1, currListIdx))

    return currNum

if __name__ == "__main__":
    print(find_kth_smallest([[2,6,8], [3,6,7], [1,3,4]], 5))
    print(find_kth_smallest([[5,8,9], [1,7]], 3))