"""
Longest Palindromic Subsequence

Given a sequence, find the length of the longest palindromic subsequence in it.
Example :
Input:"bbbab"
Output:4
"""


def lps(s):
    r = s[::-1]
    n = len(s)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == r[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


if __name__ == "__main__":
    print(lps("bbbab"))
    print(lps("BBABCBCAB"))
