"""
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

Example 2:
Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".

Example 3:
Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
"""
from collections import defaultdict

# def solution(s):
#     winStart, maxLen = 0, 0
#     uniqueCh = defaultdict(int)

#     for winEnd in range(len(s)):
#         winEndCh = s[winEnd]
#         uniqueCh[winEndCh] += 1

#         while uniqueCh[winEndCh] > 1:
#             winStartCh = s[winStart]
#             uniqueCh[winStartCh] -= 1
#             if uniqueCh[winStartCh] == 0: 
#                 uniqueCh.pop(winStartCh)
#             winStart += 1
#         maxLen = max(maxLen, winEnd - winStart + 1)
#     return maxLen

def solution(s):
    win_start, max_len = 0, 0
    char_index_map = {}

    for win_end in range(len(s)):
        right_char = s[win_end]

        if right_char in char_index_map:
            win_start = max(win_start, char_index_map[right_char]+1)

        char_index_map[right_char] = win_end
        max_len = max(max_len, win_end - win_start + 1)
    return max_len

    return max_len


if __name__ == "__main__":
    print(solution("aabccbb"))
    print(solution("abbbb"))
    print(solution("abccde"))