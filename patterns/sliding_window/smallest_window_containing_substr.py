"""
Given a string and a pattern, find the smallest substring in the given string which has all 
the characters of the given pattern.

Example 1:
Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Example 2:
Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".

Example 3:
Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
"""

from collections import Counter

def solution(s, p):
    window_start, min_len, substr_start = 0, len(s)+1, 0
    char_frequency, matched = Counter(p), 0

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1


        while matched == len(char_frequency):
            if matched == len(char_frequency):
                curr_len = window_end - window_start + 1
                if min_len > curr_len:
                    min_len = curr_len
                    substr_start = window_start
            left_char = s[window_start]

            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
            window_start += 1

    return s[substr_start:substr_start+len(p)+1] if min_len != len(s)+1 else ""



if __name__ == "__main__":
    print(solution("aabdec", "abc"))
    print(solution("abdabca", "abc"))
    print(solution("adcad", "abc"))
