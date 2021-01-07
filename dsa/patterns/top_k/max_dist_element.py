"""
Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the array such that we are left with maximum distinct numbers.

Example 1:
Input: [7, 3, 5, 8, 5, 3, 3], and K=2 
freq: {7:1, 3:3, 5:2, 8:1}
Output: 3
Explanation: We can remove two occurrences of 3 to be left with 3 distinct numbers [7, 3, 8], we have 
to skip 5 because it is not distinct and occurred twice. 
Another solution could be to remove one instance of '5' and '3' each to be left with three 
distinct numbers [7, 5, 8], in this case, we have to skip 3 because it occurred twice.

Example 2:
Input: [3, 5, 12, 11, 12], and K=3
Output: 2
Explanation: We can remove one occurrence of 12, after which all numbers will become distinct. Then 
we can delete any two numbers which will leave us 2 distinct numbers in the result.

Example 3:
Input: [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], and K=2
Output: 3
Explanation: We can remove one occurrence of '4' to get three distinct numbers.
"""

from collections import Counter
from heapq import heappop, heappush

# TC: O(nlogn) SP: O(n)
def maxDistinctNumbers(nums, k):
    maxDistinctNumbers = 0
    if len(nums) < k:
        return maxDistinctNumbers
    numsFreq = Counter(nums)
    minHeap = []

    for num, freq in numsFreq.items():
        if freq == 1:
            maxDistinctNumbers += 1
        else:
            heappush(minHeap, (freq, num))

    while k and minHeap:
        freq, num = heappop(minHeap)
        freq -= 1
        if freq == 1:
            maxDistinctNumbers += 1
        else:
            heappush(minHeap, (freq-1, num))

        k -= 1

    if k > 0:
        maxDistinctNumbers -= k

    return maxDistinctNumbers

if __name__ == "__main__":
    print(maxDistinctNumbers([7, 3, 5, 8, 5, 3, 3], 2))
    print(maxDistinctNumbers([3, 5, 12, 11, 12], 3))
    print(maxDistinctNumbers([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2))