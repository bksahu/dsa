"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""

from collections import defaultdict

def solution(s, k):
    winStart, maxLen = 0, 0
    seenCh = defaultdict(int)

    for winEnd in range(len(s)):
        endCh = s[winEnd]
        seenCh[endCh] += 1

        if len(seenCh) > k:
            startCh = s[winStart]
            seenCh[startCh] -= 1
            if seenCh[startCh] == 0:
                seenCh.pop(startCh)
            winStart += 1

        maxLen = max(maxLen, winEnd - winStart + 1)
        winEnd += 1

    return maxLen



if __name__ == "__main__":
    print(solution("araaci", 2))
    print(solution("araaci", 1))
    print(solution("cbbebi", 3))