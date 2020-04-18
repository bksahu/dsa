"""
Coin Change Problem Minimum Numbers of coins
============================================
Given a value V, if we want to make change for V cents, and we have infinite supply 
of each of C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins 
to make the change?

Example:
Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents 
"""


def count(arr, m, n):
    dp = [[float("inf") if x == 0 else 0 for y in range(n+1)] for x in range(m+1)]
    
    for j in range(1, n+1):
        if j%arr[0] == 0:
            dp[1][j] = j//arr[0]
        else:
            dp[1][j] = float("inf")

    # print(dp)

    for i in range(1, m+1):
        for j in range(1, n+1):
            if arr[i-1] <= j:
                dp[i][j] = min(dp[i-1][j], dp[i][j-arr[i-1]] + 1)
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
  