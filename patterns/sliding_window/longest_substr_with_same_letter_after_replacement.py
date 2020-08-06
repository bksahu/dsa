"""
Given a string with lowercase letters only, if you are allowed to replace no more than 
‘k’ letters with any letter, find the length of the longest substring having the same 
letters after replacement.

Example 1:
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Example 2:
Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Example 3:
Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""

from collections import defaultdict

def solution(s, k):
    win_start, max_len, max_repeat_letter_count = 0, 0, 0
    frequency_count = defaultdict(int)

    for win_end in range(len(s)):
        right_char = s[win_end]
        frequency_count[right_char] += 1
        max_repeat_letter_count = max(
            max_repeat_letter_count, frequency_count[right_char])

        if (win_end - win_start + 1 - max_repeat_letter_count) > k:
            left_char = s[win_start]
            frequency_count[left_char] -= 1
            win_start += 1

        max_len = max(max_len, win_end - win_start + 1)
    return max_len


if __name__ == "__main__":
    print(solution("aabccbb", 2))
    print(solution("abbcb", 1))
    print(solution("abccde", 1))
