'''
Given two strings, print the length of shortest common supersequence

x = "geek"
y = "eke"
LCS = 5 ie. "geeke"
'''

def shortest_common_supersequence(x, y, n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i][j-1]
                )

    return n + m - dp[-1][-1]

if __name__ == "__main__":
    x = "geek"
    y = "eke"
    n, m = len(x), len(y)
    print(shortest_common_supersequence(x, y, n, m))
