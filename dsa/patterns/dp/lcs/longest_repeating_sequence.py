"""
Longest Repeating Subsequence
Given a string, print the longest repeating subsequence such that the two subsequence don’t have same 
string character at same position, i.e., any i’th character in the two subsequences shouldn’t have the 
same index in the original string.

Example:
Input: str = "aab"
Output: "a"
The two subsequence are 'a'(first) and 'a' 
(second). Note that 'b' cannot be considered 
as part of subsequence as it would be at same
index in both.
"""

def longest_repeating_sequence(s):
    n = len(s)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == s[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    m, n = n, n
    lrs = ""
    while n != 0 and m != 0:
        # if s[n-1] == s[m-1] and m != n:
        if dp[n][m] == dp[n-1][m-1] + 1:
            lrs = s[n-1] + lrs
            n -= 1
            m -= 1
        elif dp[n-1][m] == dp[n-1][m]:
            n -= 1
        else:
            m -= 1

    return lrs

if __name__ == "__main__":
    print(longest_repeating_sequence("aab"))
    print(longest_repeating_sequence("aabbebbcc"))