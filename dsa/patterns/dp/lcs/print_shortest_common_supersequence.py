"""
Given two strings X and Y, print the shortest string that has both X and Y as subsequences. 
If multiple shortest supersequence exists, print any one of them.

Examples:
Input: X = "AGGTAB",  Y = "GXTXAYB"
Output: "AGXGTXAYB" OR "AGGXTXAYB" 
OR Any string that represents shortest
supersequence of X and Y

Input: X = "HELLO",  Y = "GEEK"
Output: "GEHEKLLO" OR "GHEEKLLO"
OR Any string that represents shortest 
supersequence of X and Y
"""

def printSCS(x, y):
    n, m = len(x), len(y)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    scs = ""
    while n > 0 and m > 0:
        if x[n-1] == y[m-1]:
            scs = x[n-1] + scs
            n -= 1
            m -= 1
        else:
            if dp[n-1][m] > dp[n][m-1]:  
                scs = x[n-1] + scs
                n -= 1
            else:
                scs = y[m-1] + scs
                m -= 1
        # print(scs)

    while n > 0: 
        scs = x[n-1] + scs
        n -= 1

    while m > 0:
        scs = y[m-1] + scs
        m -= 1

    return scs

if __name__ == "__main__":
    print(printSCS("cab", "abac"))
    print(printSCS("AGGTAB", "GXTXAYB"))
    print(printSCS("HELLO", "GEEK"))