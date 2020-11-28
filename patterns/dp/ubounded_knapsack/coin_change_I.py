"""
Coin Change Problem Maximum Number of ways
===========================================
Given a value N, if we want to make change for N cents, and we have infinite supply of each of 
S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins 
doesn’t matter.

Example:
for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
"""


def count(arr, m, n):
    dp = [[0 if x == 0 else 1 for y in range(n+1)] for x in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]


if __name__ == "__main__":
    # Driver program to test above function 
    arr = [1, 2, 3] 
    m = len(arr) 
    n = 5
    x = count(arr, m, n) 
    print(x) 
  