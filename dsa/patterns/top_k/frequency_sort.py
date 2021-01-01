"""
Given a string, sort it based on the decreasing frequency of its characters.

Example 1:
Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

Example 2:
Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
"""

from heapq import heapify, heappush, heappop

def frequency_sort(s):
    # TC: O(nlogn)
    # SP: O(n)
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    maxHeap = []
    for ch, f in freq.items():
        heappush(maxHeap, (-f, ch))

    sorted_s = ""
    while maxHeap:
        f, ch = heappop(maxHeap)
        sorted_s += ch*-f
    
    return sorted_s
     

    
        


if __name__ == "__main__":
    print(frequency_sort("Programming"))
    print(frequency_sort("abcbab"))