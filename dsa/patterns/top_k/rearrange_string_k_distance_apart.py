"""
Given a string and a number ‘K’, find if the string can be rearranged such that the same characters 
are at least ‘K’ distance apart from each other.

Example 1:
Input: "mmpp", K=2
Output: "mpmp" or "pmpm"
Explanation: All same characters are 2 distance apart.

Example 2:
Input: "Programming", K=3
Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more
Explanation: All same characters are 3 distance apart.

Programming
{'P': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}


Example 3:
Input: "aab", K=2
Output: "aba"
Explanation: All same characters are 2 distance apart.

Example 4:
Input: "aappa", K=3
Output: ""
Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.
"""

from collections import Counter, deque
from heapq import heappush, heappop, heapify

def rearrangedStringKDistanceApart(s, k):
    charFreq = Counter(s)
    if len(charFreq) < k: return ""

    maxHeap = [(-freq, ch) for ch, freq in charFreq.items()]
    heapify(maxHeap)

    q = deque([]) # q = [(ch, freq)]
    rearrangedStr = ""

    while maxHeap:
        currFreq, currCh = heappop(maxHeap)
        rearrangedStr += currCh
        q.append((currCh, currFreq+1))
        if len(q) == k:
            prevCh, prevFreq = q.popleft()           
            if prevFreq < 0:    
                heappush(maxHeap, (prevFreq, prevCh))

    return rearrangedStr if len(rearrangedStr) == len(s) else ""



if __name__ == "__main__":
    print(rearrangedStringKDistanceApart("mmpp",2))
    print(rearrangedStringKDistanceApart("Programming",3))
    print(rearrangedStringKDistanceApart("aab",2))
    print(rearrangedStringKDistanceApart("aappa",3))