"""
Permutation in a String
#######################

Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” 
has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have n! permutations.

Example 1:
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Example 4:
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""

from collections import Counter

def solution(s, p):
    if len(p) > len(s):
        return False

    window_start, matched, pattern_frequency = 0, 0, Counter(p)

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in pattern_frequency:
            pattern_frequency[right_char] -= 1
            if pattern_frequency[right_char] == 0:
                matched += 1
        
        if matched == len(pattern_frequency):
            return True

        if window_end >= len(p) - 1:
            left_char = s[window_start]
            if left_char in pattern_frequency:
                if pattern_frequency[left_char] == 0:
                    matched -= 1
                pattern_frequency[left_char] += 1
            window_start += 1

    return False


if __name__ == "__main__":
    print(solution("oidbcaf", "abc"))
    print(solution("odicf", "dc"))
    print(solution("bcdxabcdy", "bcdyabcdx"))
    print(solution("aaacb", "abc"))
