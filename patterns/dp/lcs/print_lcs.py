'''
Given two strings, print the longest common subsequence

x = "abcdgh"
y = "aebdghr"
LCS = 5 ie. "abdgh"
'''

def print_lcs(x, y, n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    lcs = ""
    while n != 0 and m != 0:
        if x[n-1] == y[m-1]:
            lcs = x[n-1] + lcs
            n -= 1
            m -= 1
        else:
            if dp[n-1][m] > dp[n][m-1]:
                n -= 1
            else:
                m -= 1

    return lcs

if __name__ == "__main__":
    x, y = "abcdgh", "aebdghr"
    n, m = len(x), len(y)
    cache = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    print(print_lcs(x, y, n, m))