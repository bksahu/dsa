"""
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Example 1:
Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.

Example 2:
Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.
"""

from heapq import heapify, heappush, heappop
from collections import Counter

def top_k_freq_numbers(nums, k):
    # TC: O(nlogn)
    # SP: O(n)
    freq = Counter(nums)

    freq = sorted(freq, key=lambda x: freq[x], reverse=True) # Can be done using heap but TC remains same
    return freq[:k]
    

if __name__ == "__main__":
    print(top_k_freq_numbers([1, 3, 5, 12, 11, 12, 11], 2))
    print(top_k_freq_numbers([5, 12, 11, 3, 11], 2))