'''
Given two strings, print the length of longest common subsequence

x = "abcdgh"
y = "aebdghr"
LCS = 5 ie. "abdgh"
'''

from functools import lru_cache

@lru_cache(maxsize=None) # to memorize
def lcs_recursive(x, y, n, m): # n & m are length of x & y respectively
    if n == 0 or m == 0:
        return 0

    if x[n-1] == y[m-1]:
        return 1+lcs_recursive(x, y, n-1, m-1)
    else:
        return max(
            lcs_recursive(x, y, n-1, m),
            lcs_recursive(x, y, n, m-1)
        )

def lcs_memorize(x, y, n, m):
    if cache[n][m] == -1:
        if n == 0 and m == 0:
            cache[n][m] = 0

        if x[n-1] == y[m-1]:
            cache[n][m] = 1 + lcs_recursive(x, y, n-1, m-1)
        else:
            cache[n][m] = max(
                lcs_recursive(x, y, n-1, m),
                lcs_recursive(x, y, n, m-1)
            )        
    return cache[n][m]

def lcs_tabluarize(x, y, n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return dp[-1][-1]


if __name__ == "__main__":
    x, y = "abcdgh", "aebdghr"
    n, m = len(x), len(y)
    global cache
    cache = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    # print(lcs_recursive(x, y, n, m))
    # print(lcs_memorize(x, y, n, m))
    print(lcs_tabluarize(x, y, n, m))