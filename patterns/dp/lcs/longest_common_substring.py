'''
Given two strings, print the length of longest common substring

x = "abcde"
y = "abfce"
LCS = 2 ie. "ab"
'''

def longest_common_substring_tabluarize(x, y, n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    longest_substring = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                longest_substring = max(longest_substring, dp[i][j])
            else:
                dp[i][j] = 0

    return longest_substring


if __name__ == "__main__":
    x, y = "abcde", "abcfce"
    n, m = len(x), len(y)
    cache = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    print(longest_common_substring_tabluarize(x, y, n, m))