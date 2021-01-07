"""
Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

Example 1:
Input: "aappp"
Output: "papap"
Explanation: In "papap", none of the repeating characters come next to each other.

Example 2:
Input: "Programming"
Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
Explanation: None of the repeating characters come next to each other.

Example 3:
Input: "aapa"
Output: ""
Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".
"""

from collections import deque, Counter
from heapq import heappush, heappop


def rearrangedString(S):
    charFreq = Counter(S)
    maxHeap = []

    for ch, freq in charFreq.items():
        heappush(maxHeap, (-freq, ch))

    reorgStr = ""
    prevCh = None
    while maxHeap:
        freq, currCh = heappop(maxHeap)
        if currCh == prevCh:
            break
        reorgStr += currCh
        charFreq[currCh] -= 1
        if prevCh:
            heappush(maxHeap, (-charFreq[prevCh], prevCh))
        if charFreq[currCh] > 0:
            prevCh = currCh
        else:
            prevCh = None
    return "" if len(reorgStr) != len(S) else reorgStr


if __name__ == "__main__":
    print(rearrangedString("aappp"))
    print(rearrangedString("Programming"))
    print(rearrangedString("aapa"))
